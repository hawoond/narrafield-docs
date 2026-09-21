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

Create an entry once and edit it from documents, relations, or the timeline. A visibility switch helps review what players can see. The interactive concept does not implement every planned view or campaign feature.

## Separate project and app settings

**Project settings** cover game identity, modules, version control, plugins, online operations, language policy, and publishing. **App settings** cover personal themes, text size, shortcuts, connected accounts, and local tools. Shared project settings should not replace personal accounts or display preferences.

{% include screenshot.html kind="concept" file="d91b5ef3bf952f24193f.jpg" width="1265" height="739" alt="Version-control concept comparing local changes, team changes, and the final merge result" caption="GitHub connections, commits, branches, and merges are grouped under project version control, so you can finish version-control work and return to editing." %}

Saving, committing, and sharing remotely remain distinct actions. The planned merge flow compares the common base, local edits, team edits, and final result before validation. The concept's merge controls only change sample state; they do not connect to a repository.

## Choose the depth of editing

- **Guided:** start with a template and a short sequence of steps.
- **Composed:** connect conditions, effects, costs, and widgets.
- **Direct:** edit the detailed definitions behind the same data.

These are editing approaches, not separate project formats. LLM assistance remains optional, with proposals reviewed before application.

## Start a project and review changes

Begin with **New project / Default templates / Open project**. You can start with a blank project or choose a template. Recommended configurations, starter images, removal, and restoration use [the same catalog](STARTER_CONTENT.md). [Three recommended configurations](CREATION_JOURNEY.md)—solo narrative, GM cooperation, and automated parties—propose related settings together.

You will be able to review changes made by hand, added through templates, suggested by AI, or brought in through Git. Accepting only some changes will trigger another check for broken connections and conflicts. Previews and exports will show which version they use. See [Test and release](TEST_AND_RELEASE.md).

## Where to work in the current demo

The demo uses top-level tabs. World, Relations, Maps, and Timeline have separate tabs; Git lives in **Tools & extensions / Merge & conflicts**, and display preferences live in **App settings**. The new sidebar and unified project settings are planned.

[Current editor menus](EDITOR.md) · [Game-screen design](GAME_SCREENS.md) · [Git collaboration](COLLABORATION.md)

## Find content while creating

The planned [Free content stores](CONTENT_STORES.md) will be available while choosing images, adding components, or configuring plugins. Find content, save it to your library, and return to the item you were editing.
