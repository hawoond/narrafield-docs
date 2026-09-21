---
title: Current capabilities and development plans
description: Compare the public 0.8.0 demo with future plans, and remaining release work.
---

# Current capabilities and development plans

Narrafield Studio is a TRPG engine developed by **sortie**. Start with a sample, connect worlds, scenes, and rules, and export your own game.

## Guide baseline

The guides were reviewed on **{{ site.data.review.date }}** against the source and capabilities of **public demo {{ site.data.review.demo_version }}**. Pages marked **In development** describe plan **{{ site.data.review.plan_version }}**. They include features that are not yet available in the demo.

[Download demo](DEMO.md) · [Current editor menus](EDITOR.md) · [Current creation workspace](DESIGN.md)

## Available in the demo

| Area | Current scope | Guide |
| --- | --- | --- |
| Workspace | Creation sidebar, separate project/app settings, search, and preserved drafts | [Workspace](DESIGN.md) |
| Starter content | Twenty images, one removable/restorable template catalog, and A Small Errand | [Starter content](STARTER_CONTENT.md) |
| World | Documents, relations, map pins, timelines, visibility, and scene references | [World](WORLD_BUILDING.md) |
| Story and rules | Scenes, choices, conditions, effects, optional dice, branches, and endings | [Rules](RULES.md) |
| Game data | Characters, enemies, abilities, spells, statuses, equipment, resources, compound costs, optional proficiency, growth, and encounters | [Game data](GAME_DATA.md) |
| Factions | Organizations, members, diplomacy, bases, personal reputation, goals, and rewards | [Factions](FACTION_GUIDE.md) |
| Play and export | Title, New game, Load, scene-focused preview, save slots, backgrounds/portraits, standalone ZIPs, separate online client/server packages | [Play and export](PLAY_AND_EXPORT.md) |
| Online | Personal invitations, character assignments, private notes, GM NPC control, WebSocket synchronization, reconnect, and persisted sessions | [Online](ONLINE.md) |
| Roleplay chat | Speech, actions, OOC, GM/NPC and certified results; authorized speakers/recipients, records, reconnect | [Roleplay chat](ROLEPLAY_CHAT.md) |
| Collaboration | Git changes, merge/conflict tools, LFS integration, and optional scoped LLM proposals | [Tools](TOOLS.md) |
| Extensions | Restricted WASM, pinned versions, permissions, runtime bindings, content packs, and configured hub access | [Plugins](TOOLS.md) |
| Translation | Paired Korean/English fields, JSON exchange, source-change tracking, review, and glossary | [Translation](LOCALIZATION.md) |

The demo is still an alpha. It has passed automated checks, but real play environments need more testing. Online play requires a separate server and external connection setup. Connecting to a configured hub does not imply that an official public catalog is operating.

## Features we are working on

The features below are in development. The following section explains what comes in the first release and what will follow later.

| Experience | Planned journey | Details |
| --- | --- | --- |
| A first story | One world detail → an action → a consequential choice → testing and export; dice, combat, characters, and LLMs are optional | [Your first story](CREATION_JOURNEY.md) |
| Free creation content | Shared discovery, library, type-specific application, and reviewed publication for plugins, templates, and assets | [Free content stores](CONTENT_STORES.md) |
| World and story | World laws, relationships, promises, chosen costs, and legacies affect later scenes and campaigns | [A world that remembers](WORLD_STORIES.md) |
| Game-specific screens | Freeform layouts, game themes, widget bindings, tactical screens, and screen packs | [Game screens](GAME_SCREENS.md) |
| Starting and parties | Character-creation editing, personal/shared parties, delegation, and split exploration | [Starting a game](PLAYER_START.md) · [Parties](PARTY_PLAY.md) |
| Continuing play | Lobby preparation, session endings, chapters, campaign completion, migration, and recovery | [Campaign continuity](CAMPAIGN_FLOW.md) |
| Rules and publishing | Source-aware packs, game identity, credits, permitted formats, and separate game store profiles | [Rule packs](RULE_PACKS.md) · [Publishing](PUBLISHING_GAME.md) |
| Testing from creation to release | Follow one version through creation, play, saving, translation, team changes, and release | [Test and release](TEST_AND_RELEASE.md) |

## Current demo, first release, and later stages

The first release includes verification of existing creation, play, and export capabilities alongside the essential experiences below.

| Stage | Scope |
| --- | --- |
| Current public demo 0.8.0 | Creation sidebar, twenty images and templates, Title/New game/Load, and basic roleplay chat |
| First-release verification · P0 | Test and refine the implemented creation, startup, content, and chat flows on actual devices and with multiple participants |
| Later R1 | Recommended configurations and change impact; consistent world, party, permissions, and cost handling; foundations for later experiences such as action requests |
| Later R2 | World laws, relationships, story checks, richer editing, and advanced chat presentation, communication, channels, and search |
| Later R3 | Integration testing and refinement across creation, play, long campaigns, updates, and publishing |

R1–R3 describe development and verification stages, not announced release dates or shipped versions. Features may span stages. Advanced chat, action requests, summaries, and operations tools are planned for later releases. Current basic chat works without an LLM or optional operations module.

The editor includes all twenty original images and their terms. Selected assets are copied into projects; exports include the images actually used. Previous site concepts have been replaced with screens from this demo.

## Broader creation goals

- **Choose needed rules:** different checks and graded outcomes, reactions and waiting, GM free actions, growth, equipment, resources, and economies.
- **Choose suitable spaces:** narrative, zones, grids, or free maps, with decks, tables, handouts, and progress clocks.
- **Reuse creative work:** reusable events, prototypes, bulk editing, visuals, audio, accessibility, public extension tools, and restricted plugin execution.
- **Explain and recover play:** rule traces, reproducible tests, performance checks, campaign saves and migration, and optional reviewed LLM proposals.

Some of these features already have a foundation, but the complete workflows are still being built. You do not need every option for a first project. Start by organizing your world if that is what you need.

## Free content-service preparation

We are preparing stores for free plugins, templates, and assets with one shared library. The service will run separately from the editor and game servers. Before opening it, we will test finding and applying content, publishing and review, use by external creators, distribution, and recovery from outages. There are no plans for paid content or a transition to it. See [Free content stores](CONTENT_STORES.md).

## Product use and consent

The planned policy preserves rights to a version bought with a one-time purchase and keeps product consent separate from agreements for individual commercial games. Regional documents, explicit acceptance, and offline copies are also planned. [Product use and game agreements](PRODUCT_TERMS.md) explains planned royalties and the distinction between creators and players. Documents for seven regions remain review drafts; sales, effective terms, consent UI, and contract services are not complete.

Sales readiness and future subscription requirements are separate release conditions. This plan alone does not restrict current demo use, free tests, or project backups.

## Remaining release checks

Real devices and networks, long projects and campaigns, input/scaling/accessibility, official code signing, actual store SDKs and achievements, Workshop integration, and an external creator's publication journey still need verification. Automated checks and screen captures alone do not complete those checks.

The current demo runtime is **{{ site.data.demo.version }}**. Source projects, play saves, and server sessions are separate. Keep copies before changes and review [Compatibility](TROUBLESHOOTING.md).

## Store availability

The full Narrafield Studio product will be offered through official stores. The [download page](DEMO.md) provides the demo. Follow each distribution's environment requirements.

{% include stores.html %}

The homepage harbor is concept art. Editor and player images are rendered from the current demo UI with example data. Appearance may vary with theme, scale, and project content.
