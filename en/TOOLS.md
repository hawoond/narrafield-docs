---
title: Tools and extensions
description: Share changes through Git, review AI proposals and understand extension-package capabilities.
---

# Tools and extensions

**Tools & extensions** groups Git, LLM, and plugin/store options. Basic world building and local play do not require an external service connection.

## Git — share saved changes

Save the project to a folder and prepare Git in your authoring environment.

1. Use **Git init** for a new repository. For an existing team repository, follow [cloning instructions](COLLABORATION.md).
2. Set the team repository URL with **Connect origin**.
3. Save the project and inspect **Status** and **Diff**.
4. Specify files in **Stage paths** and select **Stage selected paths**.
5. Write a useful commit message and **Commit**.
6. **Push** to share. Retrieve teammates' changes through fetch and merge.

Saving writes project files, committing records Git history, and pushing shares it remotely. These are separate, explicit actions.

[Git collaboration](COLLABORATION.md) covers branch switching, conflicts, and merge cancellation.

## LLM — generate a proposal from selected context

This feature uses a compatible API endpoint and model you configure. Real-provider integration must be checked in your environment.

1. Enter the **Endpoint**, model, and any required API key.
2. Specify only the world or scene IDs to include in **Context IDs**.
3. Write the request and review what will be sent.
4. If it contains private or GM information, give consent for that request.
5. Select **Generate with selected context**, read the proposal JSON, and remove unwanted changes.
6. **Apply reviewed proposal**, then validate and save.

Your prompt and selected entries are sent to the provider. The response is not applied automatically. If source content changes after generation, the stale proposal is blocked; review a proposal based on the current content.

## Plugins and stores

Demo 0.6 includes **Project extensions**, **Common hub**, **Dependencies / transfer / trust**, **Save migration**, and **Create content pack** tabs. Extensions are optional; ordinary authoring does not require them.

1. Choose a local archive in **Project extensions** and use **Inspect package / permissions / activate**.
2. Review the source, hash, exact version, dependencies, and requested permissions, then activate only the permissions you approve.
3. Open **Components** to inspect available templates, editor commands, settings, or validators. Review proposed edits before applying them.
4. For a supported runtime extension, configure **Runtime binding** and check where the scene or rule invokes it. Installation alone does not wire every action into a game.
5. Validate and preview, save the project, then inspect the exported game with the same pinned modules and required notices.

The runtime executes restricted WASM extensions. Supported declared effects and state use the shared engine; this is not unrestricted native code or a complete arbitrary-widget editor. Changes, dependency updates, removal, and save migration require review. Available migration tools write a separate copy under their exact compatibility requirements, not a universal engine-version conversion.

Content packs can select supported definitions and managed images with license information. The **Common hub** interface uses a configured service. A runnable self-hosted hub is separate from an officially operated public catalog. Real Steam Workshop subscription and Steam/STOVE/Epic service integration are not verified as complete. Official store pages remain [coming soon](DEVELOPMENT.md#stores).

## Planned workspace location

Project plugin policy and Git will move into [Project settings](DESIGN.md); creative content and optional LLM assistance remain close to the item being edited. This is a planned reorganization of the current menus.

## Check after working

- Only intended files are staged for sharing.
- AI proposal targets and changes match your intent.
- Extension test results are not treated as full game compatibility or release support.
- After applying team changes or proposals, preview the affected play routes.

**Related:** [Git collaboration](COLLABORATION.md) · [Translation](LOCALIZATION.md) · [Development](DEVELOPMENT.md)

## Multiple ways to change the same source

The planned [creation and testing journey](TEST_AND_RELEASE.md) keeps direct edits, templates, LLM proposals, and Git merges on the same source and references, with revalidation after partial application. LLMs remain optional; proposals do not automatically change world truth or confirmed game results.

## Planned free content stores

[Free content stores](CONTENT_STORES.md) connect plugins, templates, and assets through one discovery experience and library. Downloading remains separate from project application and execution permissions. Current hub capabilities above do not mean an official public store is operating.
