---
title: Git collaboration
---

# Git collaboration

Use **Merge and conflicts** for cloning, branch lists, Fetch, switching existing branches, merges, conflict resolution, and LFS status. Use these alongside the explicit Stage / Commit / Push controls in the services screen.

1. Enter an HTTPS/SSH URL or an existing local repository path and an empty destination folder. After cloning, open that folder as a project. Authentication uses the installed Git credential integration.
2. Save, review, and commit your edits. Uncommitted or untracked files block branch switches and merges. The editor does not automatically stash changes, force a switch, or push.
3. After Fetch, refresh branches and conflicts to see local and remote branches. You can switch to a local branch or an origin branch.
4. A fast-forward merge moves to that commit. A merge of diverged history stops with `--no-commit`; review and an explicit commit are required even without conflicts.
5. Select a conflicted file to see the common base, your changes, and team changes. For JSON, edit manually or choose a side; only valid JSON can be saved. If one side deleted a file, explicitly choose deletion or restore the remaining version. For binary files, compare sizes and blob IDs and select a side. Confirm the selected file and resolution before saving and staging.
6. Reload the project and validate references and rules before committing and sharing. A successful Git merge does not guarantee a valid game.

Conflict data comes from Git index stages 1/2/3, so it can be restored after restarting the app. Saving a resolution is rejected if the conflict stages have changed since the screen was loaded. Editor saves and Git mutations share a lock per repository path. External Git processes do not use that lock, so avoid simultaneous editing while an external tool is changing the repository.

## Abort a merge and recover edits

**Abort merge and back up edits** first copies all tracked files that differ from HEAD and all untracked file contents to `.git/narrafield-recovery/<UTC timestamp>/files/`. Deleted-file states are recorded in `manifest.json`.

After a successful backup, it runs `git merge --abort`. If abort fails, the backup location and error are shown. Review files before restoring them; no automatic overwrite occurs. A clean working tree is required before starting a merge, so existing edits are not automatically discarded. Symlink and submodule conflicts cannot be resolved in the app.

## Git execution and authentication

Git arguments are passed directly without a shell command string. Hooks are disabled per command. Custom merge drivers and content filters are blocked; only standard `git-lfs` filter commands are allowed. Global Git settings and existing hook files are left unchanged.

Raw network-command output and failure stderr can contain credentials, so they are not displayed in the app. Interactive authentication waits are disabled and commands have a 30-second limit.

## Git LFS

The LFS screen shows the installed Git LFS version and `git lfs status`. If LFS is not installed, the screen reports that it is unavailable.

For repositories tracking LFS files, Push explicitly runs the standard `git lfs push origin HEAD` before the ordinary Git push. This prevents missing uploads when hooks are disabled. LFS downloads during clone depend on the remote, credentials, and installed tools.

Remote LFS availability, blocking exports with missing assets, an LFS locking UI, and authentication and LFS reception on two physical computers remain separate validation areas.

## Verification scope

Automated checks use a temporary bare remote and two local clones. They cover Korean and space-containing paths, Fetch, changes to JSON on both sides, three-way reads, manual resolution, explicit commit and push, abort backups after conflict resolution, protection for uncommitted changes, rejection of path/option injection, suppression of credential output, and shared repository locks.

## Planned workspace location

The new design groups GitHub connections, branches, commits, and merges under **Project settings → Version control**. The [workspace concept](DESIGN.md) is a planned layout; the demo still uses **Merge & conflicts / Tools & extensions**.
