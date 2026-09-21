---
title: Translation workspace
---

# Content translation workspace

This feature translates the game content you are creating. To change the language of this user guide, use the **한국어 / English** tabs at the top of the site.

The native editor's translation tab lists stable string IDs for entity names/bodies, scene titles/bodies and action labels. It shows Korean source beside English translation, with search and missing/draft/reviewed/source-changed filters. A saved project is required before applying translations.

Applying one translation or importing a JSON exchange validates every entry before changing content. Unknown and duplicate keys, another project/locale, changed source text or hash, mismatched placeholder names/counts/types and locked glossary violations reject the whole import. Keys use entity/scene/action IDs, so reordering actions cannot redirect translations. Imports are bounded to 4 MiB and reject unknown JSON fields and trailing data.

Translation content remains in the existing per-ID entity and scene JSON files and uses existing runtime English fallback. `localization/review.json` holds source and target hashes, review flags and a glossary. It is authoring-only and is not copied into game packages. Source edits mark existing translations as source-changed; target edits invalidate review. Applying translation content is one normal editor undo step. Review metadata saves separately immediately; hashes ensure undo or discarded unsaved content cannot incorrectly inherit a reviewed state. Glossary edits save immediately and do not participate in project undo.

The glossary editor accepts an array such as `[{"source":"마라","target":"Mara","locked":true}]`. Locked terms use literal case-sensitive containment. Empty or duplicate source terms are rejected. Empty translations remain missing and are allowed for incremental work. Placeholder checking supports named `{actor}` and typed `{amount:int}` tokens, including repeated occurrences. Translation import is a trusted-authoring action, not an automatic runtime update.

Current limitations: the source column assumes Korean and targets English; bidirectional authoring, locale catalogs replacing inline fields, project/item/quest/summary/relation translations, automatic plural rules, language completeness export gates and full Unicode/IME/font accessibility QA remain separate work. Supported UI languages do not imply all game content has been translated. Source-hash review history is local to this authoring metadata file; it is not a translation service or machine translation API.
