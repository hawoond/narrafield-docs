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

The current demo uses runtime **{{ site.data.demo.version }}**. Packages, saves, and server snapshots are checked against their runtime and content. Keep source projects and original saves, then export with the matching player. There is no general automatic migration to 0.6. Use an explicit migration tool only when its exact source-runtime, content, and plugin requirements are satisfied, and retain the original file.

When changing online content or runtime versions, preserve the existing state file and give `--state` a new path outside the project. See [Online sessions](ONLINE.md) for restart and state-file restrictions.

## Can each online player own a separate character?

Individual invitations and character assignment are separate. Player control depends on the server’s character assignments and permissions. An invitation alone does not automatically create a new player character.

## A translation cannot be applied

Save the project first. JSON import validates project, locale, string keys, source changes, placeholders, and locked terms. Any error rejects the whole import. Correct the reported issues and import again. See [Translation workspace](LOCALIZATION.md).

## The concept menus are missing

Pages marked **In development** show planned workflows, including the new workspace, screen composer, character creation, and party rules. The downloadable demo still uses the [current editor menus](EDITOR.md).

## I can join but cannot act

An invitation without a character assignment joins as a spectator. Ask the GM to review the participant assignment and current turn. See [Online sessions](ONLINE.md).

## Features described only in development plans

If the new sidebar, unified template catalog, starter image pack, or integrated RP chat is absent from your demo, check [current, first-release, and later stages](DEVELOPMENT.md). A planned-feature guide does not mean those features ship in the demo.
