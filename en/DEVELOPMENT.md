---
title: Current capabilities
description: Features, online limitations, compatibility, and store availability for the Narrafield Studio development alpha.
---

# Current capabilities

Narrafield Studio is a **TRPG engine developed by sortie**. It is currently a development alpha. Samples and guides help you build worlds, scenes, and choices step by step.

This website provides product information and complete Korean and English guides. It does not distribute executable files. Purchases and installation will be handled through official stores.

{% include stores.html %}

## Guide baseline

The detailed guides follow the **runtime 0.4 development-alpha** menu structure. Older builds may differ in Game data, Factions, and individual forms. Find the relevant task in the [editor menu guide](EDITOR.md).

## Available features

| Area | Features | Guide |
| --- | --- | --- |
| World building | Places, characters, relations, map pins, chronology, scene connections | [Worlds and scenes](WORLD_BUILDING.md) |
| Stories and rules | Choices, conditions, effects, dice checks, items, quests, attributes | [Rules and catalogs](RULES.md) |
| Game data | Resources, abilities, spells, statuses, characters, combat definitions and assignments | [Game data](GAME_DATA.md) |
| Factions | Organization, members, diplomacy, places, reputation, goals and scene connections | [Factions](FACTION_GUIDE.md) |
| Components | Add narrative, d20 checks, and combat to a project | [Component templates](TEMPLATES.md) |
| Play and export | Preview, local save slots, standalone game export | [Play and export](PLAY_AND_EXPORT.md) |
| Team creation | Git cloning, branches, merges, conflict resolution, LFS | [Git collaboration](COLLABORATION.md) |
| Translation | Korean/English editing for supported content, JSON exchange, review tracking | [Translation workspace](LOCALIZATION.md) |

## Online and translation scope

Online play currently **shares one party character**. Individual invitations, revocation, and session persistence are supported, but per-player character ownership and the complete multiplayer feature set are not finished. External connections require a separate HTTPS server setup.

The translation workspace handles Korean source and English translations for world names and bodies, scene titles and bodies, and action labels. It does not cover every content type or language.

## Release and compatibility

Multi-platform support remains a development goal. Supported operating systems and installation requirements will be listed on official store product pages at release. A store release date has not been announced. Development features and test results are not a guarantee of final release quality. Display scaling, input, networking, and other real-world environments need further validation.

The current runtime compatibility version is **0.4.0**. Game packages, saves, and server sessions from earlier runtimes are incompatible. Export again from the source project using the new runtime. See [Troubleshooting](TROUBLESHOOTING.md).

The harbor image is conceptual world art. The editor image is an actual development-alpha screenshot; its layout may differ from the current build.

## Where should I start?

- Explore the [creation workflow](EXPERIENCE.md) for the overall product experience.
- Use the [editor menu guide](EDITOR.md) to find a specific editor task.
- Read [Troubleshooting](TROUBLESHOOTING.md) for launch, save, and compatibility issues.

Official store links will be added to the store section when available.
