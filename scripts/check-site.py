"""Check the actual Jekyll output before GitHub Pages deployment (stdlib only)."""
import argparse
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class Page(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.ids = set()
        self.links = []
        self.headings = 0
        self.language = None
        self.anchors = []
        self.source = source
        self.feed(source)

    def handle_starttag(self, tag, pairs):
        attrs = dict(pairs)
        if tag == "html":
            self.language = attrs.get("lang")
        if tag == "a":
            self.anchors.append(attrs)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag == "h1":
            self.headings += 1
        for attribute in ("href", "src"):
            if attrs.get(attribute):
                self.links.append(attrs[attribute])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", type=Path)
    parser.add_argument("--base-path", default="")
    args = parser.parse_args()
    root = args.directory.resolve()
    base = args.base_path.rstrip("/")
    expected = {"index.html", "WIKI.html", "QUICKSTART.html", "WORLD_BUILDING.html",
                "TEMPLATES.html", "RULES.html", "PLAY_AND_EXPORT.html", "ONLINE.html",
                "COLLABORATION.html", "LOCALIZATION.html", "TROUBLESHOOTING.html",
                "DEVELOPMENT.html",
                "EXPERIENCE.html", "EDITOR.html", "PROJECT.html", "RELATIONS.html", "MAPS.html", "TIMELINE.html", "SCENES.html", "GAME_DATA.html", "FACTION_GUIDE.html", "TOOLS.html"}
    expected |= {"en/" + name for name in list(expected)}
    pages = {path.resolve(): Page(path.read_text(encoding="utf-8"))
             for path in root.rglob("*.html")}
    errors = []
    for name in expected:
        path = root / name
        if path not in pages:
            errors.append(f"Missing page: {name}")
        else:
            page = pages[path]
            language = "en" if name.startswith("en/") else "ko"
            counterpart = name.removeprefix("en/")
            if page.headings != 1:
                errors.append(f"Expected one main heading: {name}")
            if page.language != language:
                errors.append(f"Wrong document language: {name}")
            for lang, prefix in (("ko", ""), ("en", "en/")):
                route = prefix + counterpart
                if route.endswith("index.html"):
                    route = route.removesuffix("index.html")
                expected_url = base + "/" + route
                matching = [a for a in page.anchors if a.get("hreflang") == lang]
                if len(matching) != 1 or matching[0].get("href") != expected_url:
                    errors.append(f"Wrong {lang} language switch: {name}")
                elif (matching[0].get("aria-current") == "page") != (lang == language):
                    errors.append(f"Wrong active language tab: {name}")
            if re.search(r"Windows|윈도우|\(영문\)", page.source, re.IGNORECASE):
                errors.append(f"Outdated platform or translation copy: {name}")
            for anchor in page.anchors:
                url = urlsplit(anchor.get("href", ""))
                if anchor.get("hreflang") or url.scheme or url.netloc or not url.path:
                    continue
                route = url.path
                if route.startswith(base + "/"):
                    route = route[len(base) + 1:]
                    if route.endswith((".html", "/")) and route.startswith("en/") != (language == "en"):
                        errors.append(f"Navigation changes language unexpectedly: {name} -> {url.path}")
    links = 0
    for path, page in pages.items():
        for reference in page.links:
            url = urlsplit(reference)
            if url.scheme or url.netloc:
                continue
            target_path = unquote(url.path)
            if not target_path:
                target = path
            elif target_path.startswith("/"):
                if base and target_path != base and not target_path.startswith(base + "/"):
                    errors.append(f"Wrong base path: {path.name} -> {reference}")
                    continue
                target = root / target_path[len(base):].lstrip("/")
            else:
                target = path.parent / target_path
            target = target.resolve()
            if not target.is_relative_to(root):
                errors.append(f"Link leaves site: {path.name} -> {reference}")
                continue
            if target.is_dir():
                target /= "index.html"
            if not target.is_file():
                errors.append(f"Missing target: {path.name} -> {reference}")
            elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
                errors.append(f"Missing anchor: {path.name} -> {reference}")
            links += 1
    forbidden = {"IMPLEMENTATION_STATUS", "VERIFICATION", "DATA_FORMAT", "PUBLISHING", "SITE_DESIGN"}
    for path in root.rglob("*"):
        if path.is_file() and (path.stem in forbidden or path.suffix == ".md"
                              or path.relative_to(root).parts[0] in {"scripts", "internal", "cmd", ".git"}):
            errors.append(f"Unexpected non-site output: {path.relative_to(root)}")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Verified {len(pages)} pages, {links} local references, and public output boundaries.")


if __name__ == "__main__":
    main()
