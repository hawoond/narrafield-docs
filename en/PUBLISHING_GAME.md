---
title: Publish under your game's identity
description: Planned creator information, credits, game branding, general distribution, and store-specific publishing.
content_status: planned
---

# Publish under your game's identity

We are preparing tools to publish games under **their own titles, logos, and creator names**. Narrafield Studio is the tool, and using it does not make sortie the creator of your game.

## Choose what to publish

The planned location is **Project settings → Game and creator information**. Set the title, public creator or team name, publisher when relevant, contributors and roles, logos, support links, and credits. Account details, Git authorship, and login names should not become public credits automatically.

Author the information once, then arrange it in **Game screens → Title / Game information / Credits**. Credits should remain accessible from menus without a persistent creator banner over gameplay.

## The tool and the game are separate products

The store used to buy the editor should be independent of the store chosen for a game. The design covers general distribution and separate Steam, STOVE, and Epic publishing profiles, each with that game's product and service settings.

| Stage | What to review |
| --- | --- |
| Identity | Title, creator, credits, and public support information |
| Destination | General distribution or a game-specific store profile |
| Included features | Online play, operations, saves, and game achievements |
| Preview | Title, icon, game information, notices, and listing material |
| Release | Package creation, upload, review, and launch as separate states |

Creating a ZIP does not mean a store upload or review has succeeded. Actual platform integration and account-level verification are still required; universal one-click publishing is not a current feature.

## Notices for included material

Track sources and conditions for the images, music, fonts, plugins, and rule content actually included. Collecting rule-pack notices into exported files and an offline in-game view is part of the [rule-pack design](RULE_PACKS.md).

The latest plan makes `Made with Narrafield Studio` optional and separates product use from agreements for specific commercial works. [Product use and game agreements](PRODUCT_TERMS.md) explains the planned digital and physical royalty bases, preservation of one-time purchase rights, and explicit consent. Effective terms, local review, and contract screens are not complete; reading this guide does not create an agreement.

## Check the format and version before release

Standalone games, online servers, PDF/print documents, target VTT modules, character tools, and content packs are different outputs. We are preparing checks for permitted uses and required notices in each format. The demo currently exports ZIP packages; the other exporters are planned for later.

Removing unused image files from a build is separate from determining the work-level disclosure and notice scope of a rule license. The 20 starter images have [finalized separate usage terms](STARTER_CONTENT.md), which do not replace engine or external rule-content terms.

Make sure the files you release match the version you tested. If you change the project, plugins, language, or participant roles, test the affected parts again. Checks and achievements from an earlier version are not enough. See [Test and release](TEST_AND_RELEASE.md). Private session conversations and account information should not be automatically included in source projects or release packages.

## In the current demo

You can set the game title and export a standalone ZIP or separate online client/server package. Complete creator profiles, integrated credits editing, and store-specific release workspaces remain planned. Follow [Project settings](PROJECT.md) and [Play and export](PLAY_AND_EXPORT.md) for current steps.

[Game screens](GAME_SCREENS.md) · [Rule packs and attribution](RULE_PACKS.md) · [Current capabilities](DEVELOPMENT.md)
