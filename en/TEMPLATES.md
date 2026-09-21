---
title: Component templates
---

# Add content with component templates

Component templates add a small set of scenes, rules, and world entries to a new or existing project. They leave your existing scenes, starting scene, world entries, and player-character attributes in place. The sample project is a separate, complete example.

## Available components

| Component | What it adds |
| --- | --- |
| Narrative | A village, a guide, an arrival event, a relation, a map pin, a timeline entry, and two connected scenes |
| d20 | An insight attribute, a quest, a d20 check, and success and failure endings |
| Combat | A sparring enemy, a healing item, and victory, defeat, and escape endings |

For a character without combat settings, the combat component supplies starting combat statistics and one healing item. Existing characters keep their statistics and inventory. If existing combat statistics are invalid, correct them before adding the component.

## Add a component

1. Select a component in the **Resources → Components**.
2. Choose **Preview addition**. Review the item counts, new ID prefix, and notes.
3. Confirm the addition.
4. If you already have a starting scene, use scene actions to connect the new scenes. To start at a new scene instead, change the starting scene in **Project settings → General**.
5. **Validate**, **Preview**, and **Save**.

One **Undo** reverses the whole addition. If the project changes after you open the preview, open a new preview before applying it.

## How components fit into a project

Added scenes are not connected automatically when a starting scene already exists. You choose where they belong in your story.

Each addition uses an unused `tpl_<component>_<number>_` ID prefix. IDs and references are updated together, including world entries, relations, map pins, timeline entries, scenes, actions, checks, quest and item effects, nested conditions, characters, attributes, and inventory. You can add the same component more than once without linking the copies to each other.

The combined project must pass validation before the addition is applied. If validation fails, nothing is added.

## Current limits

The demo provides bundled components without external assets or scripts. It cannot import arbitrary third-party templates.

You can edit added content, but those edits do not update the original template. Template updates also leave content already added to a project unchanged.

## Starter template catalog

Open **Starter Templates** from the launcher or project-name menu. **New project → Start from a template** opens the same catalog. Full-project templates create new projects; components add content to the current project.

Removing a catalog entry preserves projects already created from it. Removed templates stay removed after restarts and updates. Use **Restore deleted templates** to bring them back.

**A Small Errand** starts without dice or combat. Include its five images or play the same story as text. See [Starter content](STARTER_CONTENT.md) for the 20 bundled images.

The [Free content stores](CONTENT_STORES.md) and official [rule-pack](RULE_PACKS.md) catalog remain in development.
