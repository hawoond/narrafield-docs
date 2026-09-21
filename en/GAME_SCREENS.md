---
title: Game screens and customization
description: Scene-focused play, creator-controlled layouts and themes, and separate player preferences.
content_status: planned
---

# Game screens and customization

Players should see the story and their next action. Creators will have tools to arrange those screens for their game. The Dark Lighthouse concepts explore both sides.

{% include screenshot.html kind="concept" file="54d886cab1c766f4c8b5.jpg" width="1280" height="720" alt="Lighthouse play concept with location and objective above dialogue and choices, and compact status and inventory controls below" caption="Scenes, dialogue, and choices take priority, with details opened when needed. The background is concept art prepared for this preview." %}

## The player's screen

Location and objectives sit above the scene; speaker, dialogue, and choices form a readable area below. Abilities, inventory, journal, map, and character sheets open on demand. Closing them returns to the scene. Games without HP or MP should not display empty resource bars.

Exploration, conversation, checks, combat, and another player's turn call for different information. Online actions should distinguish processing, approval, result lookup, confirmation, and reselection. Success effects should follow confirmed results.

This scene view is not the game's initial entry point. The planned flow is **Title → New game / Load → Required preparation → Play**. See [Starting a game and character creation](PLAYER_START.md).

## The creator's screen editor

{% include screenshot.html kind="concept" file="e93a6e0cc33a0ddfd021.jpg" width="1265" height="735" alt="Creator properties beside a play preview, with dialogue layout, theme, text size, resource, and objective controls" caption="Creator controls stay outside the player's screen. The concept demonstrates selected layout, theme, and information-density adjustments." %}

| Area | Planned controls |
| --- | --- |
| Screen template | Text-led, cinematic, or tactical starting layouts |
| Layout and widgets | Dialogue, choices, objectives, resources, sheets, inventory, and menus |
| Theme | Colors, fonts, backgrounds, spacing, and reduced-motion alternatives |
| Data binding | Connect widgets to public names, values, objectives, and actions |
| Context | Adapt to exploration, combat, waiting, and reconnection |

The planned editor lives in **Game screens**, including title, character creation, game information, and credits. Free placement, complete binding tools, screen-pack sharing, and export integration are not included in this concept.

## Creator controls and player preferences

Creators define the game's layout and theme. Players use the text, input, audio, and motion preferences that the game provides. Display preferences do not change game rules or grant access to hidden information.

## Text RP puts conversation at the center

Scene-led play is one template. Text RP puts **chat history and the message box** at the center; cinematic play uses a conversation panel and tactical play a side panel. The image above shows a scene-focused layout. It does not show the new chat feature running.

Basic chat is a first-release goal, with clear speakers, speech/action/OOC modes, recipients, and delivery state. Bubbles, dialogue effects, speaker styles, special communication, detailed channels, search, and summaries are planned for later releases. See [Roleplay chat](ROLEPLAY_CHAT.md).

## Keep essential actions reachable

Even after a creator changes widgets or modules, players need access to choices, approvals, costs, chat, saves, and required notices. If the default screen cannot provide a missing essential function, validation will explain the problem and block that combination. [Screen verification](TEST_AND_RELEASE.md) also covers large text, keyboards, IME input, and the reader's position in conversation history.

## Difference from the current demo

The demo supports scene backgrounds, portraits, choices, abilities, items, and saves. Its current menu and information-panel interface is covered in [Play and export](PLAY_AND_EXPORT.md). The scene-focused design and general screen composer above remain planned features.

[New workspace](DESIGN.md) · [Starting a game](PLAYER_START.md) · [Online party design](PARTY_PLAY.md)
