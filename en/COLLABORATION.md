---
title: Git collaboration
---

# Git collaboration

Git lets you keep a history of your project and share changes with collaborators. Use **Tools & extensions** to stage, commit, and push changes. Use **Merge and conflicts** to clone projects, switch branches, and merge work. Git must be installed on your computer.

## Bring in team changes

1. Enter an HTTPS/SSH URL or an existing local repository path and an empty destination folder. After cloning, open that folder as a project. Authentication uses the installed Git credential integration.
2. Save, review, and commit your edits. Uncommitted or untracked files block branch switches and merges. The editor does not automatically stash changes, force a switch, or push.
3. After Fetch, refresh branches and conflicts to see local and remote branches. You can switch to a local branch or an origin branch.
4. If your branch can move directly to the incoming commit, the merge finishes immediately. If both sides have separate changes, the merge stops before committing, even when there are no conflicts. Review the result, then commit it yourself.
5. Select a conflicted file to see the common base, your changes, and team changes. For JSON, edit manually or choose a side; only valid JSON can be saved. If one side deleted a file, explicitly choose deletion or restore the remaining version. For binary files, compare sizes and blob IDs and select a side. Confirm the selected file and resolution before saving and staging.
6. Reload the project and validate references and rules before committing and sharing. A successful Git merge does not guarantee a valid game.

Unresolved conflicts remain available after you restart the app. If another tool changes the conflict, refresh the list before saving a resolution. Avoid saving or merging in the editor while an external Git tool is changing the repository.

## Abort a merge and recover edits

**Abort merge and back up edits** first copies all tracked files that differ from HEAD and all untracked file contents to `.git/narrafield-recovery/<UTC timestamp>/files/`. Deleted-file states are recorded in `manifest.json`.

After a successful backup, it runs `git merge --abort`. If abort fails, the backup location and error are shown. Review files before restoring them; no automatic overwrite occurs. A clean working tree is required before starting a merge, so existing edits are not automatically discarded. Symlink and submodule conflicts cannot be resolved in the app.

## Advanced: Git execution and authentication

Git arguments are passed directly without a shell command string. Hooks are disabled per command. Custom merge drivers and content filters are blocked; only standard `git-lfs` filter commands are allowed. Global Git settings and existing hook files are left unchanged.

Raw network-command output and failure stderr can contain credentials, so they are not displayed in the app. Interactive authentication waits are disabled and commands have a 30-second limit.

## Git LFS

The LFS screen shows the installed Git LFS version and `git lfs status`. If LFS is not installed, the screen reports that it is unavailable.

For repositories tracking LFS files, Push explicitly runs the standard `git lfs push origin HEAD` before the ordinary Git push. This prevents missing uploads when hooks are disabled. LFS downloads during clone depend on the remote, credentials, and installed tools.

Remote LFS support and transfers between two physical computers need further testing. Export blocking for missing assets and an LFS locking interface also need further work. After cloning, check that the project’s images open correctly.

## Verification scope

Automated checks use a temporary bare remote and two local clones. They cover Korean and space-containing paths, Fetch, changes to JSON on both sides, three-way reads, manual resolution, explicit commit and push, abort backups after conflict resolution, protection for uncommitted changes, rejection of path/option injection, suppression of credential output, and shared repository locks.

## Planned workspace location

The new design groups GitHub connections, branches, commits, and merges under **Project settings → Version control**. The [workspace concept](DESIGN.md) is a planned layout; the demo still uses **Merge & conflicts / Tools & extensions**.

## Coming later: testing merged changes

The planned [Test and release](TEST_AND_RELEASE.md) tools will help check that merged changes work in scenes, screens, saves, and exported games. Moving an active campaign to a new version will require a separate review.
