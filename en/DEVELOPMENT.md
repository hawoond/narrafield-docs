---
title: Current capabilities and development plans
description: Compare the public 0.6 demo with the latest plans, concept screens, and remaining release work.
---

# Current capabilities and development plans

Narrafield Studio is a TRPG engine developed by **sortie**. Start with a sample, connect worlds, scenes, and rules, and export your own game.

## Guide baseline

The guides were reviewed on **{{ site.data.review.date }}** against the source and capabilities of **public demo {{ site.data.review.demo_version }}**. Pages marked **In development** describe plan **{{ site.data.review.plan_version }}**. They include features that are not yet available in the demo.

[Download demo](DEMO.md) · [Current editor menus](EDITOR.md) · [Latest workspace concept](DESIGN.md)

## Available in the demo

| Area | Current scope | Guide |
| --- | --- | --- |
| World | Documents, relations, map pins, timelines, visibility, and scene references | [World](WORLD_BUILDING.md) |
| Story and rules | Scenes, choices, conditions, effects, optional dice, branches, and endings | [Rules](RULES.md) |
| Game data | Characters, enemies, abilities, spells, statuses, equipment, resources, compound costs, optional proficiency, growth, and encounters | [Game data](GAME_DATA.md) |
| Factions | Organizations, members, diplomacy, bases, personal reputation, goals, and rewards | [Factions](FACTION_GUIDE.md) |
| Play and export | Preview, save slots, backgrounds/portraits, standalone ZIPs, separate online client/server packages | [Play and export](PLAY_AND_EXPORT.md) |
| Online | Personal invitations, character assignments, private notes, GM NPC control, WebSocket synchronization, reconnect, and persisted sessions | [Online](ONLINE.md) |
| Collaboration | Git changes, merge/conflict tools, LFS integration, and optional scoped LLM proposals | [Tools](TOOLS.md) |
| Extensions | Restricted WASM, pinned versions, permissions, runtime bindings, content packs, and configured hub access | [Plugins](TOOLS.md) |
| Translation | Paired Korean/English fields, JSON exchange, source-change tracking, review, and glossary | [Translation](LOCALIZATION.md) |

The demo is still an alpha. It has passed automated checks, but real play environments need more testing. Online play requires a separate server and external connection setup. Connecting to a configured hub does not imply that an official public catalog is operating.

## Features we are working on

The features below are in development. The following section explains what comes in the first release and what will follow later.

| Experience | Planned journey | Details |
| --- | --- | --- |
| A first story | One world detail → an action → a consequential choice → testing and export; dice, combat, characters, and LLMs are optional | [Your first story](CREATION_JOURNEY.md) |
| Starting content | 20 starter images, a blank project and one template catalog, removal and restoration | [Starter content](STARTER_CONTENT.md) |
| Free creation content | Shared discovery, library, type-specific application, and reviewed publication for plugins, templates, and assets | [Free content stores](CONTENT_STORES.md) |
| Creation workspace | Separate creative navigation, project settings, and personal preferences; multiple views of the same source | [Workspace concept](DESIGN.md) |
| World and story | World laws, relationships, promises, chosen costs, and legacies affect later scenes and campaigns | [A world that remembers](WORLD_STORIES.md) |
| Game-specific screens | Text RP, scene-led, and tactical layouts, themes and bindings with essential controls preserved | [Game screens](GAME_SCREENS.md) |
| Starting and parties | Title, New game, Load, character preparation, personal/shared parties, delegation, and split exploration | [Starting a game](PLAYER_START.md) · [Parties](PARTY_PLAY.md) |
| Shared conversation | Character speech, action descriptions, OOC, GM narration, confirmed results, speakers and recipients | [Roleplay chat](ROLEPLAY_CHAT.md) |
| Continuing play | Lobby preparation, session endings, chapters, campaign completion, migration, and recovery | [Campaign continuity](CAMPAIGN_FLOW.md) |
| Rules and publishing | Source-aware packs, game identity, credits, permitted formats, and separate game store profiles | [Rule packs](RULE_PACKS.md) · [Publishing](PUBLISHING_GAME.md) |
| Testing from creation to release | Follow one version through creation, play, saving, translation, team changes, and release | [Test and release](TEST_AND_RELEASE.md) |

## Current demo, first release, and later stages

The first release includes verification of existing creation, play, and export capabilities alongside the essential experiences below.

| Stage | Scope |
| --- | --- |
| Current public demo 0.6.0 | The capability table above and current demo guides; the integrated workspace and basic RP chat are not already included |
| First-release essentials · P0 | New project, title, New game, Load and save protection; editor slots for 20 starter images; one default template catalog with removal/restoration; basic roleplay chat |
| Later R1 | Recommended configurations and change impact; consistent world, party, permissions, and cost handling; foundations for later experiences such as action requests |
| Later R2 | World laws, relationships, story checks, richer editing, and advanced chat presentation, communication, channels, and search |
| Later R3 | Integration testing and refinement across creation, play, long campaigns, updates, and publishing |

R1–R3 describe development and verification stages, not announced release dates or shipped versions. Features may span stages. Advanced chat, action requests, summaries, and operations tools are planned for later releases. Basic chat should work without an LLM or optional operations module.

The 20 original images and their usage terms are ready. Installer bundling, catalog integration, project import, and runtime verification remain separate work. The four UI concepts show the proposed layouts; they are not screenshots of a finished product.

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

Real devices and networks, long projects and campaigns, input/scaling/accessibility, official code signing, actual store SDKs and achievements, Workshop integration, and an external creator's publication journey still need verification. Builds and interactive concepts alone do not complete those checks.

The current demo runtime is **{{ site.data.demo.version }}**. Source projects, play saves, and server sessions are separate. Keep copies before changes and review [Compatibility](TROUBLESHOOTING.md).

## Store availability

The full Narrafield Studio product will be offered through official stores. The [download page](DEMO.md) provides the demo. Follow each distribution's environment requirements.

{% include stores.html %}

The homepage harbor is conceptual art. New workspace and play images are labeled **concept screens**; older application captures are labeled **earlier development-alpha screens**.
