---
title: Free plugin, template, and asset stores
description: Planned discovery, one local library, type-specific application, publishing, and independent operation for free creation content.
content_status: planned
---

# Free plugin, template, and asset stores

The goal is to find content inside the editor and continue through **download → application review → editing → preview → game export**. Plan 1.31 adopts three stores, a shared library, and an independent service. App integration and official public operation are not complete.

These stores share **free creation content**. They are distinct from official stores selling Narrafield Studio, stores publishing creators' games, and player mod stores. Payments, orders, paid subscriptions, settlement, and a paid transition roadmap are outside this content-store scope. Free downloads do not automatically grant commercial-use or source-redistribution rights.

## Find three kinds of content together

| Area | Initial supported scope | Use in a project |
| --- | --- | --- |
| Plugins | Editor commands, validators, rules, and supported play-UI extensions | Review permissions and exact versions before activation |
| Templates | Whole projects and story, world, or game-data components | Create a new project or add editable content to an existing project |
| Assets | PNG/JPEG backgrounds, maps, portraits, creatures, items, abilities, and status images | Copy selected images into the project and connect display slots |

The planned app provides **Store → Templates / Assets / Plugins**, plus shared **My library / My submissions**. Screen/theme templates, audio, animation, tiles, and fonts follow when their editing, playback, and export capabilities are supported. Unsupported formats are not presented as installable content.

Public browsing, downloads, and the local library should work without signing up. The initial library is device-local, without cloud or favorite synchronization. Publishing and submission management use separate publisher authentication.

## Find content from your current task

- **Start screen:** browse whole templates and create a new project.
- **Default templates / Start from template:** use the same catalog, prioritizing bundled and installed entries. Removed defaults do not silently return.
- **Add components:** review additions and where they connect to the current project.
- **Assets and image selection:** preview at the actual portrait, background, or icon proportions before adding or replacing.
- **Project settings → Plugins:** review active versions, permissions, missing files, updates, and recovery.

Closing the store should return to the original document, selection, unsaved input, and position. [Offline use and selective restoration](STARTER_CONTENT.md) of the 20 starter images and bundled templates remain available in the plan.

## Separate downloading from applying

Downloading alone does not change a project, starting scene, or execution permissions. Planned states distinguish **Downloaded / Check failed / Applicable / In use / Update candidate / Recovery needed**. With no project selected, choose a destination before applying.

A whole template creates a new project in a new path. It does not copy accounts, Git connections, secrets, or play saves, or overwrite an existing project. Components preview additions, references, conflicts, and global setting changes for selective review. Only after preparation and validation succeed should one undoable edit apply the changes.

Assets are selected from a downloaded pack and copied into the project. Preview portraits in dialogue/sheet proportions, backgrounds behind dialogue, and icons at small sizes. Selecting an image does not add statistics, effects, or hostility. Removing the original pack from the library preserves copied project assets.

Plugins need a separate activation decision after reviewing dependencies, permissions, and runtime inclusion. Templates disclose executable plugin requirements; code-free content must not conceal executable modules. Updates require review. Opening a project or receiving team changes does not automatically change pinned runtime versions. Automatic merging of edited template copies is also outside the first scope.

## What content details should show

Review descriptions, samples, publisher, source, exact version, change history, tested engine version, dependencies, total size, and usage terms. Assets add purpose, style, proportions, resolution, transparency, and AI-generation status. Plugins add execution permissions and save compatibility.

Official authorship, verified publisher identity, functional review, and file-check success are separate signals. Initial recommendations use task-based collections and recently reviewed entries. Comments, ratings, public popularity rankings, and personalized recommendations are outside the first scope. Preview images are distinct from playable samples.

Check commercial game use, modification, game inclusion, team sharing, editable-source redistribution, channels, and notices separately. **Distributing a game containing artwork may have different conditions from republishing that artwork in a template.** [Rule-pack and source conditions](RULE_PACKS.md) connect to the same review flow.

## Share what you make

The first public service is planned for invited publishers and review before publication. Select only intended definitions and assets for local validation and submission; do not upload the entire project directory. Content starts private and follows **Submission → File checks → Review → Approval → Publisher chooses public visibility**.

Content licenses and the free distribution service's publishing terms remain separate. Planned review covers AI-generation status, rights, and content, with rejection reasons, revised submissions, reports, and appeals. Withdrawing a publication stops new discovery/downloads without remotely deleting existing projects. Confirmed malicious executable content has a separate restriction and recovery path.

## Keep creation and play independent of service availability

The three stores share one service, operated independently from the editor and game servers. With required content and approved permissions already present, signing out or a store outage should not block local creation. Missing files for a new application are explained while preserving the existing project.

Permitted runtime components and required assets are included in game distributions. Players should not need the editor, a content-store account, or separate content downloads. Games are planned to run without contacting this store service. Publisher accounts, credentials, and personal caches stay out of game files and team projects.

## Current demo and release preparation

[Tools and extensions](TOOLS.md) describes current restricted plugins, content packs, and configured hub access. Whole external project templates, standalone asset packs, the shared library, and official public operation require separate development and verification. Later mystery and horror packs are plans, not completed artwork releases.

Store preparation proceeds through common foundations → discovery/application for all three types → publishing/review → external-creator, distribution-channel, failure, and recovery verification. Service readiness and actual public-operation conditions must be checked before availability. Dates and supported scale are not announced.

[Starter images and templates](STARTER_CONTENT.md) · [New workspace](DESIGN.md) · [Test and release](TEST_AND_RELEASE.md)
