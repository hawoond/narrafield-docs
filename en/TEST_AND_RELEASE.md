---
title: Test the whole journey before release
description: Explore tools being built to test a game from start to finish and release the version you checked.
content_status: planned
---

# Test the whole journey before release

A scene that works in preview may look different in an exported game. A translation may be missing, or online play may get stuck waiting for approval. We are preparing tools to test the release version from beginning to end. This page describes those tools, not completed test results.

## Connect edits to the version tested

Direct edits, templates, content packs, LLM proposals, and Git merges should use the same source and references. Before applying a change, you will see what is added, changed, or removed, where it came from, and how it affects your own edits. Partial application rechecks remaining references.

Preview should identify whether it uses current edits or saved content. Exports use a saved, fixed version of the selected content. Subsequent edits do not silently enter an active test or campaign. Changes to translation, screens, plugins, or destinations show which tests need to run again.

## Keep essential actions reachable

When choosing a module, check whether the engine supports it, whether it is included in the exported files, and whether the campaign can use it. Turning on a setting or hiding a widget cannot make an unsupported feature work.

After changing a theme, screen pack, or module, **choices, approvals, cost confirmation, required chat, saves, notices, and keyboard navigation** must remain available. Decorations may disappear; essential actions need an equivalent basic or list view. Without one, export or campaign activation should be blocked. Basic screens and chat do not wait for the complete advanced editor.

## Seven situations to test from start to finish

| Situation | What to check |
| --- | --- |
| A first game without characters | Start from a blank project or starter template, change details and choices, and add images. Test Korean and English, export the game, start two new games, and load a save. |
| A choice that lasts into another session | Give up a memory and check the effects on promises and factions. Take another route, end the session, and see whether the consequences remain in the next session and epilogue. |
| Text play with a GM | Choose and approve characters in the lobby, then exchange dialogue, whispers, and action proposals. Share a GM-created clue privately, disconnect and return, then end the session. |
| A party without a GM | Make a shared proposal with individual characters. Test tied votes, absent players, and refused personal costs, then follow another route and end the session together. |
| Split parties and special communication | Run combat and investigation at the same time while using communication with costs and delays. Revoke speech delegation, disconnect, pause, then agree on world time and reunite. |
| A game made and released together | Accept part of a pack or AI draft and merge team changes through Git. Change modules and screens, check sources and translations, and export client/server packages and each release format. |
| Updating a long campaign | Save with decisions still pending, then move to a new version. Test both failed and successful migration on a copy, server recovery, story branches, and inherited consequences. |

These tests do not need to fit into one giant introductory sample. Choose tests for the game's configuration and development stage, and do not mark untested features as passed.

## Check the pace of participation

Check whether anyone waits too long, how much work it takes to control several characters, and how split scenes affect time spent waiting for the GM. Include players who abstain from votes or are absent, and check what people can do outside combat. Request lists, scene rotation, simultaneous planning, and optional timers may help without confirming someone else's action.

Quiet roleplay and spectating are valid participant choices. Speaking volume is not a mandatory participation score. Voluntary tests will record decision opportunities and waiting times without storing conversation text, alongside participant questionnaires. Automated tests alone cannot establish enjoyment, understanding, accessibility, or performance.

## Release the version you tested

Test results will record the game and source versions, engine, plugins, modules, and language. They will also identify the files tested, whether they are for clients or servers, and the intended release format and store. Passing preview does not replace standalone, online, or store verification. Client and server packages contain role-appropriate files while using compatible content.

Selecting used assets is distinct from a license's work-level scope. Creation achievements remain earned, but a changed game still needs to be checked before release. Untested combinations and unimplemented output formats should remain explicitly identified.

[Current capabilities and development stages](DEVELOPMENT.md) · [Publishing your game](PUBLISHING_GAME.md) · [Rule packs and distribution conditions](RULE_PACKS.md)
