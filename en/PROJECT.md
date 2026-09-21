---
title: Project settings
description: Create or open a project and configure its title, start scene, content version and save folder.
---

# Project settings

The **Project** menu defines the title and starting point of your story. The project folder contains editable source material. Use **Export** to create the separate package players receive.

## Start a project

1. Choose **New**, or use **Sample** to explore an existing setup.
2. Enter a title and content version in **Project**.
3. Select **Apply**, then **Save** and choose a project folder.
4. Create the first scene in [Scenes & actions](SCENES.md), then select **Set as start**.
5. Save again and **Validate** the start scene and ending routes.

You can save a draft without scenes. A successful save does not mean the project is ready to preview or export.

## Settings explained

| Setting | What to enter | Check |
| --- | --- | --- |
| Title | The name of your game | Use your own work's title. |
| Content version | A value identifying a revision of your work | This is separate from the engine runtime version. |
| Start scene ID | The first scene's ID | Use an existing scene ID, not its title. |
| Include local GM controls | Whether the exported game permits local GM intervention | Choose explicitly for your game's intended use. |

## Apply, save, and save a copy

**Apply** changes the project being edited. **Save** writes those changes to the project folder. **Save as** lets you work in another folder while keeping the original.

Save the sample to your own folder before editing. Check the bottom status for **Unsaved changes** or **No project folder**.

## Publish a revised game

1. **Open** the original project folder.
2. Make changes and distinguish the revision with a content version.
3. **Validate** and **Play** the changed routes.
4. Export a new package and check it runs.

Content or runtime changes can invalidate old saves. Online sessions are also tied to content: preserve the existing state file and use a new state path. Read [compatibility guidance](TROUBLESHOOTING.md).

## Common questions

- **Start scene not found:** Check for a title entered instead of an ID, or a reference to a deleted scene.
- **Saved but cannot play:** Resolve reference and ending-route errors reported by validation.
- **Must I edit JSON?** Use the forms for ordinary work. Full project JSON editing is an advanced option for users who understand the structure.

**Next:** [Scenes and actions](SCENES.md) · [Play and export](PLAY_AND_EXPORT.md)
