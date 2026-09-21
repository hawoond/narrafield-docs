---
title: Current capabilities and development plans
description: Compare the public 0.6 demo with the latest plans, concept screens, and remaining release work.
---

# Current capabilities and development plans

Narrafield Studio is a TRPG engine developed by **sortie**. Start with a sample, connect worlds, scenes, and rules, and export your own game.

## Guide baseline

The guides were reviewed on **{{ site.data.review.date }}** against the source and capabilities of **public demo {{ site.data.review.demo_version }}**. Pages marked **Planned features and designs** describe plan **{{ site.data.review.plan_version }}**. A feature appearing in a document or concept does not mean it is included in the demo.

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

Automated checks do not certify production quality or every possible rule. Online play requires a separate server and external connection setup. Connecting to a configured hub does not imply that an official public catalog is operating.

## Experiences in the latest plan

| Goal | Beyond the current demo | Details |
| --- | --- | --- |
| New workspace | Separate creative navigation, project settings, and personal app settings | [Workspace](DESIGN.md) |
| Game-specific screens | Scene-led play with templates, layouts, themes, and data binding | [Game screens](GAME_SCREENS.md) |
| Starting and creation | Title, New game, Load, and creator-defined character creation | [Starting a game](PLAYER_START.md) |
| Parties and campaigns | Personal/shared parties, delegation, action order, split exploration, lobbies, and recovery | [Online parties](PARTY_PLAY.md) |
| Independent publishing | Public creator identity, credits, and general/Steam/STOVE/Epic game profiles | [Publishing](PUBLISHING_GAME.md) |
| Optional rule packs | No default d20 activation, source-identified packs, and notice collection/export | [Rule packs](RULE_PACKS.md) |

Broader engine goals include richer outcomes and reactions, GM improvisation, campaign continuity, optional spatial/economy rules, reusable stories, extension APIs, rule tracing, and save migration. Existing foundations are distinct from complete workflows. Release dates are not announced.

## Remaining release checks

Real devices and networks, long projects and campaigns, input/scaling/accessibility, official code signing, actual store SDKs and achievements, Workshop integration, and an external creator's publication journey still need verification. Builds and interactive concepts alone do not complete those checks.

The current demo runtime is **{{ site.data.demo.version }}**. Source projects, play saves, and server sessions are separate. Keep copies before changes and review [Compatibility](TROUBLESHOOTING.md).

## Store availability

The full Narrafield Studio product will be offered through official stores. The [download page](DEMO.md) provides the demo. Follow each distribution's environment requirements.

{% include stores.html %}

The homepage harbor is conceptual art. New workspace and play images are labeled **concept screens**; older application captures are labeled **earlier development-alpha screens**.
