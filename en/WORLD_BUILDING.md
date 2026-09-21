---
title: Worlds and scenes
---

# Worlds and scenes

World records organize the setting. Scenes and actions define what players read, choose, and experience.

## Create a world entry

1. Choose **World → + Entity**.
2. Set a name and type: **place** for a location, **person / npc** for a character, or **event** for history.
3. Write a summary and body, and separate tags with commas.
4. Set visibility, then **Apply changes** and **Save**.
5. Find the entry again through name, type, or tag search.

The name is a display label. The **ID** connects entries and scenes. Reference one place record instead of creating duplicate versions of the same location.

## Choose visibility

| Value | Meaning | Example |
| --- | --- | --- |
| public | Player-facing lore | Harbor name and description |
| conditional | Lore revealed through an unlock | A secret passage discovered through a clue |
| secret | Hidden information | The force behind the incident |
| gm | Information for the GM | Session notes |

Connect conditional lore to actual scene or ability reveal effects. Check the result in the player views of [Relations](RELATIONS.md) and [Maps](MAPS.md).

## Organize places and characters

Detailed instructions are available for [Relations](RELATIONS.md), [Maps](MAPS.md), and [Timeline](TIMELINE.md). Use [Factions](FACTION_GUIDE.md) for organization membership and reputation.

Create places, characters, and other records in **World**, then connect them through **Relations**, **Map**, and **Chronology**. Drag relation nodes and map pins into place. Personal layouts and shared team layouts are kept separate.

Start with the opening location and main characters, then connect the records your scenes need. After changing a name or body, choose **Apply**, then **Save**.

## Connect scenes and choices

Use a world's **Create scene** action to start a scene linked to that entry. See [Scenes and actions](SCENES.md) for detailed editing and branching.

Write scene text and choices in **Scenes and actions**, and select each next scene. Check that the starting scene ID in **Project** points to an existing scene.

For example, give an opening scene two actions and connect each to a next scene. Follow both paths through to an ending. **Validate** and **Preview** help find broken connections.

Scenes added through components are not connected automatically if the project already has a starting scene. Connect an existing action to an added scene, or change the project's starting scene.

## Backgrounds and portraits

Import backgrounds and portraits through the editor. Verified images are included in exported game packages and displayed by the player. Online access requires authentication and is limited to the current scene for players.

## Conditions and checks

Use **Expression composition** in the action editor to combine attributes, variables, and inventory values in conditions, checks, and effects. Dice are supported only in check expressions. Existing simple conditions, effects, and dice settings remain available.

Edit items, quests, attributes, and initial inventory in **Game data → Items & quests**. Remove references before deleting definitions that scenes or expressions use. See [Rules and catalogs](RULES.md) for supported operations.

## Translation and teamwork

The **Translation workspace** edits Korean source and English translations for world names and bodies, scene titles and bodies, and action labels. It supports JSON exchange. Save the project before translating. Not every content type is supported yet.

Share team projects through Git in **Collaboration and extensions** and **Merge and conflicts**. Save and review edits before committing and pushing. After switching branches or merging, use **Reload project** and **Validate**. Authors using teamwork need Git installed; projects with LFS assets also need Git LFS.

## Related guides

- [Component templates](TEMPLATES.md): add narrative, checks, and combat.
- [Rules and catalogs](RULES.md): define conditions, expressions, and game data.
- [Translation workspace](LOCALIZATION.md): check translation coverage and review tracking.
- [Git collaboration](COLLABORATION.md): fetch team changes and resolve conflicts.
- [Play and export](PLAY_AND_EXPORT.md): play your finished story.

## Planned consequences for world details

[A world that remembers](WORLD_STORIES.md) connects laws, promises, relationships, and legacies to actions while separating facts, rumors, beliefs, and visibility. Current document editing is distinct from the complete planned story-checking tools.
