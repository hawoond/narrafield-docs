---
title: Worlds and scenes
---

# Worlds and scenes

World records organize the setting. Scenes and actions define what players read, choose, and experience.

## Organize places and characters

Create places, characters, and other records in **World**, then connect them through **Relations**, **Map**, and **Chronology**. Drag relation nodes and map pins into place. Personal layouts and shared team layouts are kept separate.

Start with the opening location and main characters, then connect the records your scenes need. After changing a name or body, choose **Apply**, then **Save**.

## Connect scenes and choices

Write scene text and choices in **Scenes and actions**, and select each next scene. Check that the starting scene ID in **Project** points to an existing scene.

For example, give an opening scene two actions and connect each to a next scene. Follow both paths through to an ending. **Validate** and **Preview** help find broken connections.

Scenes added through components are not connected automatically if the project already has a starting scene. Connect an existing action to an added scene, or change the project's starting scene.

## Backgrounds and portraits

Import backgrounds and portraits through the editor. Verified images are included in exported game packages and displayed by the player. Online access requires authentication and is limited to the current scene for players.

## Conditions and checks

Use **Expression composition** in the action editor to combine attributes, variables, and inventory values in conditions, checks, and effects. Dice are supported only in check expressions. Existing simple conditions, effects, and dice settings remain available.

Edit items, quests, attributes, and initial inventory in **Items and quests**. Remove references before deleting definitions that scenes or expressions use. See [Rules and catalogs](RULES.md) for supported operations.

## Translation and teamwork

The **Translation workspace** edits Korean source and English translations for world names and bodies, scene titles and bodies, and action labels. It supports JSON exchange. Save the project before translating. Not every content type is supported yet.

Share team projects through Git in **Collaboration and extensions** and **Merge and conflicts**. Save and review edits before committing and pushing. After switching branches or merging, use **Reload project** and **Validate**. Authors using teamwork need Git installed; projects with LFS assets also need Git LFS.

## Related guides

- [Component templates](TEMPLATES.md): add narrative, checks, and combat.
- [Rules and catalogs](RULES.md): define conditions, expressions, and game data.
- [Translation workspace](LOCALIZATION.md): check translation coverage and review tracking.
- [Git collaboration](COLLABORATION.md): fetch team changes and resolve conflicts.
- [Play and export](PLAY_AND_EXPORT.md): play your finished story.
