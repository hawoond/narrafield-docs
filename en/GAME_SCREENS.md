---
title: Game screens and customization
description: Scene-focused play, creator-controlled layouts and themes, and separate player preferences.
content_status: planned
---

# Game screens and customization

Players should see the story and their next action. Creators need a separate workspace for composing that experience. The Dark Lighthouse concepts explore both sides.

{% include screenshot.html kind="concept" file="e7869ac5f22deef5b30e.jpg" width="1424" height="634" alt="Lighthouse play concept with location and objective above dialogue and choices, and compact status and inventory controls below" caption="Scenes, dialogue, and choices take priority, with details opened when needed. The background is concept art prepared for this preview." %}

## The player's screen

Location and objectives sit above the scene; speaker, dialogue, and choices form a readable area below. Abilities, inventory, journal, map, and character sheets open on demand. Closing them returns to the scene. Games without HP or MP should not display empty resource bars.

Exploration, conversation, checks, combat, and another player's turn call for different information. Online actions should distinguish processing, approval, result lookup, confirmation, and reselection. Success effects should follow confirmed results.

This scene view is not the game's initial entry point. The planned flow is **Title → New game / Load → Required preparation → Play**. See [Starting a game and character creation](PLAYER_START.md).

## The creator's screen editor

{% include screenshot.html kind="concept" file="d4d9e0bd7682cfdd2f97.jpg" width="1424" height="673" alt="Creator properties beside a play preview, with dialogue layout, theme, text size, resource, and objective controls" caption="Creator controls stay outside the player's screen. The concept demonstrates selected layout, theme, and information-density adjustments." %}

| Area | Planned controls |
| --- | --- |
| Screen template | Text-led, cinematic, or tactical starting layouts |
| Layout and widgets | Dialogue, choices, objectives, resources, sheets, inventory, and menus |
| Theme | Colors, fonts, backgrounds, spacing, and reduced-motion alternatives |
| Data binding | Connect widgets to public names, values, objectives, and actions |
| Context | Adapt to exploration, combat, waiting, and reconnection |

The planned editor lives in **Game screens**, including title, character creation, game information, and credits. Free placement, complete binding tools, screen-pack sharing, and export integration are not implemented by this limited concept.

## Creator controls and player preferences

Creators define the game's layout and theme. Players use the text, input, audio, and motion preferences that the game provides. Display preferences do not change game rules or grant access to hidden information.

## Difference from the current demo

The demo supports scene backgrounds, portraits, choices, abilities, items, and saves. Its current menu and information-panel interface is covered in [Play and export](PLAY_AND_EXPORT.md). The scene-focused design and general screen composer above remain planned features.

[New workspace](DESIGN.md) · [Starting a game](PLAYER_START.md) · [Online party design](PARTY_PLAY.md)
