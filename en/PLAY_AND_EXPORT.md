---
title: Play and export
---

# Play and export

This guide explains how creators validate and export their own games. Try the editor from [Download the demo](DEMO.md); the full product will be offered through [official stores](DEVELOPMENT.md#stores).

The `.exe` names below are examples from the current development build. Check the instructions for your build or game for supported environments and launch methods.

## Run a game you received

Extract the creator's entire game ZIP into a folder, then run the game executable, named `game.exe` in the current build. Do not run directly from inside the ZIP; extract all accompanying files. Players do not need the editor or a compiler.

For an online game, also obtain the server address and player token from the creator. The token is your access credential.

## Validate and preview while creating

**Apply** form changes, **Save** the project, and check **Validate** results. Resolve starting-scene, reference, and branching errors, then use **Preview** to play each choice and ending.

Check backgrounds, portraits, conditional choices, successful and failed checks, and branches after combat. Passing automatic validation does not mean every route has been played through.

## Save a game

The local player provides five manual and three automatic save slots. Preview saves and exported-game saves are separate.

Packages and saves must be compatible with the current runtime. See [Troubleshooting](TROUBLESHOOTING.md) for older versions.

## Export an offline game

1. Keep the matching player runtime (`player.exe` in the current build) beside the editor.
2. Resolve project errors reported by **Validate**.
3. Choose offline play and an output folder in **Export**.
4. Give players the complete generated ZIP.
5. Extract it and verify that the game starts and displays its images and choices.

The current default package is an unsigned development build.

## Export an online game

Online export creates separate `client` and `server` folders. **Give players only the client folder.** The server operator runs the server executable (`server.exe` in the current build). Players connect with the server address and a player token. External connections require an HTTPS proxy.

Packages with the optional operations module include the operator console (`operator.exe`). Use **Server operations** in the editor or the console with the GM token to manage invitations, revocation, announcements, and restrictions.

The online demo assigns characters to personal invitations and checks control on the server. Unassigned participants join as spectators. Keep server state and credentials outside the project; see [Online sessions](ONLINE.md) for startup, restart, assignment, and backup limitations.

## Related guides

- [Quick start](QUICKSTART.md): learn the flow with the sample.
- [Online sessions](ONLINE.md): manage servers and access credentials.
- [Troubleshooting](TROUBLESHOOTING.md): resolve launch, export, and save problems.

## Planned game screens and publishing

[Scene-focused screens and customization](GAME_SCREENS.md), [Title, New game, and character creation](PLAYER_START.md), and [Creator identity, credits, and store profiles](PUBLISHING_GAME.md) are planned beyond the current player interface. Their complete workflows are not included in the demo.

## Planned creation and long-term play

The instructions above cover current demo play, saves, and ZIP exports. [Title and New game](PLAYER_START.md), [session endings and recovery](CAMPAIGN_FLOW.md), and [test and release](TEST_AND_RELEASE.md) are separate development goals. [Game identity and output formats](PUBLISHING_GAME.md) also distinguish plans from available capabilities.
