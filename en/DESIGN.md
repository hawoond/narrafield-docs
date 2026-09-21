---
title: A new creation workspace
description: Preview Narrafield Studio's planned workspace for worlds, stories, and game screens, with separate project settings.
content_status: planned
---

# A new creation workspace

The planned workspace keeps creative content in focus, with a separate place for collaboration and publishing settings. These captures come from the latest interactive concept, rather than the downloadable demo.

{% include screenshot.html kind="concept" file="e3d2ede897558165f3f7.jpg" width="1265" height="737" alt="Workspace concept with creation navigation on the left, a timeline in the center, and selected-record properties on the right" caption="Documents, relations, and the timeline refer to the same world records. The selected record stays available in the properties panel." %}

## Find what you want to create

| Workspace | Content |
| --- | --- |
| World | People, places, factions, documents, relations, maps, and timelines |
| Game data | Characters, enemies, skills, spells, items, statuses, creation, party, and check rules |
| Story | Scenes, dialogue, quests, reusable events, and campaigns |
| Game screens | Title, character creation, dialogue, sheets, inventory, and credits |
| Assets | Images, audio, fonts, and attribution |
| Translation | Korean and English content and review status |
| Testing | Play previews, rule checks, and multiple participant viewpoints |

The design reuses a record across views instead of requiring repeated entry. A visibility switch helps review what players can see. The interactive concept does not implement every planned view or campaign feature.

## Separate project and app settings

**Project settings** cover game identity, modules, version control, plugins, online operations, language policy, and publishing. **App settings** cover personal themes, text size, shortcuts, connected accounts, and local tools. Shared project settings should not replace personal accounts or display preferences.

{% include screenshot.html kind="concept" file="d91b5ef3bf952f24193f.jpg" width="1265" height="739" alt="Version-control concept comparing local changes, team changes, and the final merge result" caption="GitHub connections, commits, branches, and merges are grouped under project version control, with a return path to the original creative context." %}

Saving, committing, and sharing remotely remain distinct actions. The planned merge flow compares the common base, local edits, team edits, and final result before validation. The concept's merge controls only change sample state; they do not connect to a repository.

## Choose the depth of editing

- **Guided:** start with a template and a short sequence of steps.
- **Composed:** connect conditions, effects, costs, and widgets.
- **Direct:** edit the detailed definitions behind the same data.

These are editing approaches, not separate project formats. LLM assistance remains optional, with proposals reviewed before application.

## One starting catalog, reviewable changes

Begin with **New project / Default templates / Open project**. Blank projects and template starts have equal entry points. Recommended configurations, starter images, removal, and restoration use [the same catalog](STARTER_CONTENT.md). [Three recommended configurations](CREATION_JOURNEY.md)—solo narrative, GM cooperation, and automated parties—propose related settings together.

Direct edits, template additions, LLM proposals, and Git merges should use the same project source and references. Partial application still requires renewed impact, source, and conflict checks. Previews identify current edits or a saved revision; export freezes the chosen revision in the planned [test and release journey](TEST_AND_RELEASE.md).

## Where to work in the current demo

The demo uses top-level tabs. World, Relations, Maps, and Timeline have separate tabs; Git lives in **Tools & extensions / Merge & conflicts**, and display preferences live in **App settings**. The new sidebar and unified project settings are planned.

[Current editor menus](EDITOR.md) · [Game-screen design](GAME_SCREENS.md) · [Git collaboration](COLLABORATION.md)
