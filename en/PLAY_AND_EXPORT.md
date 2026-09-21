---
title: Play and export
---

# Play and export

This guide explains how creators validate and export their own games. Purchases and installation of Narrafield Studio will be handled through [official stores](DEVELOPMENT.md#stores). This website does not distribute executable files.

The `.exe` names below are examples from the current development build. The engine is being developed toward multi-platform support. Check the instructions for your build or game for supported environments and launch methods.

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

The current online model shares one party character. Server sessions and credentials are stored in a private file outside the project. See [Online sessions](ONLINE.md) for startup, restart, invitations, and backup limitations.

## Related guides

- [Quick start](QUICKSTART.md): learn the flow with the sample.
- [Online sessions](ONLINE.md): manage servers and access credentials.
- [Troubleshooting](TROUBLESHOOTING.md): resolve launch, export, and save problems.
