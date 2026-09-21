---
title: Game data
description: Define and assign items, quests, attributes, resources, skills, spells, characters and combat.
---

# Game data

**Game data** is where you create items, attributes, and abilities, then assign them to characters. This guide follows the **demo {{ site.data.review.demo_version }}**; older builds have different menus and capabilities.

Defining an item does not give it to a character. Abilities also need the appropriate assignment and usage conditions before appearing in play.

## Find a submenu

| Submenu | What to author |
| --- | --- |
| Items & quests | Item definitions, quest objectives and completion text, starting inventory |
| Attributes & derived values | Base attributes and calculated values |
| Resources | Bounds and starting values for mana, focus, or other resources |
| Skills · Active / Skills · Passive | Directly used abilities and event-driven abilities |
| Spells | Effects, school, element, and spell rank |
| Item abilities | Abilities that require a particular owned item |
| Statuses | Persistent states and their behavior |
| Characters & enemies / Encounters | Character definitions, enemies, and combat participants |
| Progression & XP | Growth stages and experience settings |
| Equipment slots & policies | Equipment slots and equipping rules |
| Character resources & cost eligibility | Initial resource overrides and attributes allowed as costs |
| Check & combat rules | Checks and basic combat settings |

## Start with items and quests

1. Define an item and its properties in **Items & quests → Items**.
2. Assign starting items and quantities in **Starting inventory**.
3. Write a quest's title, objectives, and completion text in **Quests**.
4. Reference items or quests from [scene conditions and effects](SCENES.md).
5. Save and preview changes to inventory and quest state.

Item, quest, and attribute IDs are used by references after creation. Renaming an entry differs from changing its ID. If deletion is blocked, first remove or change the scenes and abilities referencing it.

## Build an ability that spends a resource

For an ability that spends focus to reveal a clue:

1. Add focus in **Resources** and set its minimum, maximum, and initial value.
2. Enable **Allow cost use** if it can be spent.
3. Create a definition in **Skills · Active** and set its name, description, mode, and target.
4. Add the resource and amount to a cost bundle, then define success and failure effects.
5. Check character assignment and select **Apply definition & assignment**.
6. **Validate**, **Test applied ability**, and check the real preview.

**Draft** stores an unfinished definition. Before play or export, complete a supported definition, clear its draft status, and validate.

## Costs, proficiency, and spell rank

Costs can combine resources, items, and eligible attributes, with alternative bundles. Check the post-payment floor and refund-on-failure behavior. Base attributes allowed as costs may be permanently reduced in runtime state.

Proficiency is optional: enable it when needed and set its experience and growth rules. **Spell rank** classifies a spell; **proficiency** measures growth in that ability. Configure them separately.

## Connect characters and combat

After creating shared definitions, assign them in **Characters & enemies** and configure participants in **Encounters**. World guild membership and combat team membership are separate settings.

For statuses, equipment, and passives, check triggers, maintenance conditions, and targets. Not every TRPG rule can be implemented here. If validation finds an unsupported combination, adjust the settings before continuing.

## Test an ability

**Test applied ability** uses an isolated state and the definition already applied to the project. It does not test unapplied form edits or modify actual play saves.

Check sufficient and insufficient resources, success and failure, and unavailable targets. Save the project and preview the complete scene flow afterward.

**Related:** [Rules and expressions](RULES.md) · [Scenes and actions](SCENES.md) · [Current capabilities](DEVELOPMENT.md)

## Character creation and parties

Characters created from the same definition keep their own equipment, resources, and progress during play. See [Online sessions](ONLINE.md) for GM character assignment in the current demo.

Planned features will let creators choose character-creation steps and let players form personal or shared parties. Permission to control a character, permission to speak for them, and consent to pay a cost will remain separate. See [Starting a game](PLAYER_START.md), [Online parties](PARTY_PLAY.md), and [A world that remembers](WORLD_STORIES.md).
