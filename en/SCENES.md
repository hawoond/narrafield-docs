---
title: Scenes and actions
description: Write scenes and choices, then connect conditions, checks, effects and success or failure routes.
---

# Scenes and actions

A **scene** is a passage the player reads. An **action** is a choice they select. Actions lead to other scenes and can change the outcome through checks and effects.

## Create a first scene

1. Choose **Scenes & actions → + New scene**.
2. Enter a title, type, and body.
3. Link relevant lore through **World IDs**, separated by commas.
4. Select **Apply**, then **Set as start** if this is the opening scene.
5. Save and create the other scenes and endings.

Scene titles and IDs are different. Use the **ID** displayed in the scene editor when entering an action's destination.

## Make a two-choice branch

Create an arrival scene and separate lighthouse and channel routes.

1. Choose **+ Add action** in the arrival scene.
2. Enter “Head toward the lighthouse” and the lighthouse route's next scene ID.
3. Apply, then add “Inspect the channel” pointing to the other route.
4. Validate that each route leads to an ending or another valid scene.

Use the same method to connect [components](TEMPLATES.md) added to an existing story.

## Conditions, checks, and effects

| Part | Question | Example |
| --- | --- | --- |
| Condition | Can this action be selected? | Does the player have at least one key? |
| Check | Did the action succeed? | Is d20 plus persuasion at least the target? |
| Effect | What changes as a result? | Give an item, advance a quest, change a variable |

The action form provides **Check dice**, **Attribute**, **Target**, and **Failure scene ID**. Use the **Expression builder** for compound conditions and calculations. Apply a new action, then reopen it to access the builder.

Conditions do not roll dice. Use checks for random outcomes, and test both success and failure destinations.

## Images and combat

Import backgrounds and portraits through the scene's image controls. Valid imported project images are included when exporting.

Use **Advanced · translations · combat** and the combat settings in [Game data](GAME_DATA.md) when adding combat. A combat component is a useful starting point for checking victory, defeat, and escape routes before replacing the content.

## Check through play

{% include screenshot.html file="player.png" width="1120" height="800" alt="Player showing a persuasion check and character attributes" caption="Read the scene and select actions to verify the actual flow." %}

- The correct scene starts, and its text and images appear as intended.
- Choices behave correctly when conditions are met and unmet.
- Success, failure, and post-combat routes remain connected.
- Endings are reachable, and item and quest changes are correct.

**Next:** [Rules and expressions](RULES.md) · [Play and export](PLAY_AND_EXPORT.md)
