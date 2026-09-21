---
title: Factions
description: Author nations and guilds with organizations, members, diplomacy, places, reputation and goals.
---

# Factions

**Factions** describes nations, guilds, and secret societies. Extend their world names and descriptions with organizational structure and reputation or goals that change during play. This guide follows the runtime {{ site.data.review.demo_version }} development alpha.

## Create a first faction

1. Choose **Factions → + Faction / template** and select an empty faction, nation, guild, or secret society.
2. Set its name, description, ideology, and visibility.
3. Apply and select the faction from the list.
4. Add units, ranks, roles, and members as needed.
5. Save and check the setup through **Sandbox state test**.

A named empty faction is a valid starting point. You do not need to fill every organizational field.

## Submenus explained

| Menu | What to author | Keep in mind |
| --- | --- | --- |
| Organization / Units | Branches, departments, and hierarchy | Keep a non-cyclic tree within the same faction. |
| Ranks / Roles | Rank order, responsibilities, and role capacities | These are game settings, not server privileges. |
| Members | Membership and unit, rank, or role assignments | Initial world membership differs from joining during play. |
| Diplomacy | Direction, relations, states, and history | Diplomacy does not automatically change combat teams. |
| Places | Presence and influence at a place | Changing a relation does not move a map pin. |
| Hierarchy | Relationships between parent and subordinate factions | This differs from departments inside one faction. |
| Metrics & reputation | Faction values, personal or party reputation, and bands | Personal and party tracks are separate. |
| Goals | Targets, progress, and completion rewards | Initial completion differs from completion during play. |
| References | Content that uses the faction | Inspect connections before editing. |

## Reuse existing membership lore

If [Relations](RELATIONS.md) contains a generic membership relation, choose **Convert existing relation** in the members view. Conversion is explicit and preserves the description. It does not invent ranks or reputation.

## Connect reputation and goals to a story

For a route that unlocks guild records at higher reputation:

1. Set a reputation track's bounds, starting value, and bands in **Metrics & reputation**.
2. Reference the faction and reputation track in a [scene condition](SCENES.md).
3. Add a reputation increase to the mission-completion action.
4. Preview the choice before and after the requirement is met.

Passing a reputation threshold does not automatically join a faction. Add explicit joining or promotion actions when required.

Goal completion rewards are protected against repeated issuance. An initially completed goal is not a way to grant its reward again; test a new goal through actual progress and completion.

## Trials and visibility

**Sandbox state test** checks a copy of initial state. Also test the full scene flow when game variables or joining conditions matter.

Check that private organizations and members remain hidden from players. A guild leader does not gain GM or server-operator credentials.

Territory polygons and automatic war, economy, or diplomacy simulation are outside the current scope.

**Related:** [World building](WORLD_BUILDING.md) · [Relations](RELATIONS.md) · [Game data](GAME_DATA.md)

## Later goals for relationships and shared worlds

[World stories](WORLD_STORIES.md) distinguish personal and party reputation while connecting promises, conflicts, and faction changes to later scenes. [Campaign continuity](CAMPAIGN_FLOW.md) covers single application of shared events and persistence between sessions.
