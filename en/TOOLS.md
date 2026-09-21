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

The current screen can verify the hash and permissions of a local extension package, install it, and run a test. Check the archive path, designated SHA-256, and allowed capabilities, then choose **Verify package**.

Review the result and permissions before installing and pinning the project version. Running a test function does not automatically integrate it into every game rule. This area is under development and is not required to start authoring.

Store authentication, achievement synchronization, and workshop integration are not complete. Official purchase and installation links will appear in [Development](DEVELOPMENT.md#stores); **store pages are coming soon**.

## Check after working

- Only intended files are staged for sharing.
- AI proposal targets and changes match your intent.
- Extension test results are not treated as full game compatibility or release support.
- After applying team changes or proposals, preview the affected play routes.

**Related:** [Git collaboration](COLLABORATION.md) · [Translation](LOCALIZATION.md) · [Development](DEVELOPMENT.md)
