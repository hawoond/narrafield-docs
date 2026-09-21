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

1. Select a component in the **Components** tab.
2. Choose **Preview addition**. Review the item counts, new ID prefix, and notes.
3. Confirm the addition.
4. If you already have a starting scene, use scene actions to connect the new scenes. To start at a new scene instead, change the starting scene in **Project**.
5. **Validate**, **Play**, and **Save**.

One **Undo** reverses the whole addition. If the project changes after you open the preview, open a new preview before applying it.

## How components fit into a project

Added scenes are not connected automatically when a starting scene already exists. You choose where they belong in your story.

Each addition uses an unused `tpl_<component>_<number>_` ID prefix. IDs and references are updated together, including world entries, relations, map pins, timeline entries, scenes, actions, checks, quest and item effects, nested conditions, characters, attributes, and inventory. You can add the same component more than once without linking the copies to each other.

The combined project must pass validation before the addition is applied. If validation fails, nothing is added.

## Current limits

The demo provides bundled components without external assets or scripts. It cannot import arbitrary third-party templates.

You can edit added content, but those edits do not update the original template. Template updates also leave content already added to a project unchanged.

## Coming later

We are bringing default templates into one catalog. **New project → Start from template** will open the same list, where you can browse story, combat, and other template types.

You will be able to remove defaults you do not need. Removed entries will stay removed after updates, and you can choose which ones to restore. Removing a catalog entry will leave existing projects intact. Copies in a project can be edited or deleted after checking their connections to other content.

The 20 starter images and their usage terms are ready. Bundling them with the editor and letting creators copy selected images into a project are still in development. See [Starter images and templates](STARTER_CONTENT.md).

The new quick-start story will begin without dice or SRD content. Add the optional 20-sided Die (d20) Check when you need it. See [Choose only the rules you need](RULE_PACKS.md) for rule packs and attribution.

The planned [Free content stores](CONTENT_STORES.md) will offer external templates. A whole template will create a new project; a component will add content to an existing one. **These features are not yet included in the demo.**

**Related:** [Quick start](QUICKSTART.md) · [Worlds and scenes](WORLD_BUILDING.md) · [Rules and expressions](RULES.md)
