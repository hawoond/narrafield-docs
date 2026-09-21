---
title: Troubleshooting
---

# Troubleshooting and compatibility

## Preview or export fails

Resolve starting-scene, reference, and branching errors in **Validate** first. If export cannot find the runtime, check that the matching player executable (`player.exe` in the current development build) is beside the editor.

If you received a game, extract every file from the ZIP before launching its executable (`game.exe` in the current build). See [Play and export](PLAY_AND_EXPORT.md) for the steps.

## An added component does not appear in play

If a starting scene already exists, added scenes remain independent. Connect an action in an existing scene to an added scene, or change the starting scene. See [Component templates](TEMPLATES.md).

## My edits are not saved to files

**Apply** and **Save** are separate actions. Apply the form changes, then save the project. After Git changes, use **Reload project** to refresh the editor. See [Quick start](QUICKSTART.md) and [Git collaboration](COLLABORATION.md).

## I cannot delete an item, quest, or attribute

Deletion is rejected while scene conditions, effects, expressions, or characters reference that definition. Remove references first. See [Rules and catalogs](RULES.md).

## An older game or save will not open

The current demo uses runtime compatibility version **{{ site.data.demo.version }}**. Game packages, saves, and server session snapshots from earlier runtimes are incompatible. Schema 1 source projects can still be opened; export them again with the new player. Play progress is not migrated automatically.

When changing online content or runtime versions, preserve the existing state file and give `--state` a new path outside the project. See [Online sessions](ONLINE.md) for restart and state-file restrictions.

## Can each online player own a separate character?

Individual invitations and character assignment are separate. Player control depends on the server’s character assignments and permissions. An invitation alone does not automatically create a new player character.

## A translation cannot be applied

Save the project first. JSON import validates project, locale, string keys, source changes, placeholders, and locked terms. Any error rejects the whole import. Correct the reported issues and import again. See [Translation workspace](LOCALIZATION.md).
