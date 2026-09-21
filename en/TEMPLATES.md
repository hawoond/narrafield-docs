---
title: Component templates
---

# Optional component templates

The editor's component templates add content to either a new blank project or an existing project. The sample project remains a separate complete example. Adding a component never replaces the current project, existing scenes, start scene, world records or player statistics.

Available built-ins:

- **Narrative**: a village, guide, arrival event, relation, map pin, chronology entry and two connected scenes.
- **d20**: an independent insight attribute, a quest, a d20 check and success/failure endings.
- **Combat**: a sparring enemy, healing item definition and victory/defeat/escape endings. A blank player receives combat statistics and one healing item. Existing characters retain statistics and inventory; invalid combat statistics must be corrected explicitly before adding this component.

Choose **Preview addition** and inspect counts, generated ID namespace and behavior notices before confirming. The addition is one Undo operation. A preview is rejected if the project changes before confirmation. If a project already has a starting scene, the added scenes are deliberately unconnected: connect them using scene actions, or explicitly select the new start scene in project settings.

Every instance uses a deterministic unused `tpl_<component>_<number>_` namespace. All component IDs and internal references are rewritten together, including entities, relations, map pins, chronology entries, scenes, actions, checks, quest/item effects, nested conditions, characters, attributes and inventory. Repeated additions create independent instances. The merged candidate passes project validation before it can be applied; validation errors do not partially change the project.

Scope: these are bundled components, not an arbitrary third-party template importer. They have no external assets or scripts. Template updates do not modify previously added content. The current editor supports additive composition; it does not synchronize edited instances back to a shared template definition.

## Planned unified templates and starter images

Plan {{ site.data.review.plan_version }} uses one **Default templates** entry. Story, combat, and sample entries are filtered within that catalog; **New project → Start from template** opens the same list. Built-in templates can be removed without changing existing projects. Removal persists through updates; selected defaults can be restored. Copied project content can be edited, replaced, or deleted after checking references.

The plan bundles 20 map, background, portrait, creature, item, ability, and status images with the editor, adding only chosen copies to a project. Original images and usage terms are ready, while installer and catalog integration remain separate development work. See [Starter images and templates](STARTER_CONTENT.md). This does not change the current alpha instructions above.

## Basic stories and optional rule packs

The d20 check is an optional component. The latest plan uses a basic quick-start story without automatically adding d20 or SRD content. [Choose only the rules you need](RULE_PACKS.md) describes planned official packs and source/notice management. The demo samples and components have not been replaced by that catalog.

## Planned external templates

[Free content stores](CONTENT_STORES.md) distinguish creating a new project from a whole template and adding components to the current project. Download, review, application, editable copies, and update policies are development goals, not current demo support for external templates.
