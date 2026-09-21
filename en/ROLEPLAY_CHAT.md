---
title: Roleplay together through conversation
description: Speak as a character, describe actions, and keep track of conversations with the demo’s online roleplay chat.
content_status: mixed
---

# Roleplay together through conversation

Demo 0.8.0 lets a GM and players run an online session through dialogue and written actions. Chat does not require an LLM. See [Online sessions](ONLINE.md) for server setup and joining.

{% include screenshot.html file="e9ddc6952273bdd18ce4.png" alt="Conversation history with speaker and recipient controls" caption="Character speech, player conversation, and certified game results are distinct. The capture uses example messages." width="1140" height="900" %}

## Configure chat as a creator

Open **Project settings → Online & operations** to enable chat and choose a layout. **Text roleplay** emphasizes conversation; **Scene with chat panel** keeps it alongside the scene.

Choose permitted recipients—current scene, party, all participants, whispers, GM, or spectators—and retention settings. If GMs may read whispers, they are disclosed as recipients before sending. Apply and save before exporting the game.

## Send a message

1. Check the message type, speaker, and recipients in the composer.
2. Choose character speech, an action description, or out-of-character (OOC) conversation. GM narration and NPC speech require the corresponding permissions.
3. Write the message and choose **Send**. Enter inserts a new line. Ctrl+Enter sending is an optional personal preference.
4. Reconfirm recipients after a scene or speaker change. Retrying a failed pending request does not create a duplicate message.

Writing an action in chat does not roll dice or change HP or items. Engine-certified results are distinct from ordinary messages. Character control and speaking rights are checked separately.

## Records and session progress

Conversation supports replies, author edits/deletions, GM pins, unread positions, and returning to recent messages. Personal blocks/mutes and room speech limits are available. Exports contain only the records the participant may read.

With history saving enabled, records are kept with the server campaign. GMs can create and restore game checkpoints without deleting human conversation or earlier certified results. Game state and conversation are separate records.

The current scope is one session with a shared party/scene and one GM. Independent parties, joint GMs, advanced action proposals, and advanced search remain planned below.

## Features planned for later

| Feature | Planned experience |
| --- | --- |
| Action proposals / check requests | Propose intent and targets from a message, then use GM review or a registered action with visible costs and linked results |
| Speech bubbles, dialogue effects, speaker styles | Configure public portraits, colors, fonts, and effects with immediate record reading, skipping, and reduced motion |
| Special communications | Model messengers, radios, and magic through distance, costs, delays, blocking, failures, and refunds |
| Detailed channels | Scene-, party-, or role-based creation, invitation, speech, reading, and retention policies |
| Advanced search | Filter by session, scene, speaker, type, or event and open permitted originals |
| Session editing | Create readable excerpts, sections, annotations, and contents without rewriting original messages or results |
| Source-linked summaries | Build return summaries from messages and confirmed events; review optional LLM drafts against originals |
| Optional reporting / operations | Preview selected messages and context, then manage role-based review, actions, appeals, and retention |

Writing an action in chat does not execute a game rule. Without a GM, proposals connect only to creator-registered actions. Editing, deleting, or resending a message must not reroll a check or duplicate a reward. Reference rolls remain distinct from confirmed checks. Special communications preserve the original recipients and costs and recheck delivery permissions.

Edited session records and summaries do not turn false dialogue or OOC remarks into world facts. LLM summaries use only content permitted for transmission. If generation fails, players can still catch up using the original records. Actual conversations, private drafts, and participant identities are not automatically included in creation projects or public game packages. Voice, video, and asynchronous services remain separate longer-term goals.

[Parties and permissions](PARTY_PLAY.md) · [Lobbies, sessions, and return](CAMPAIGN_FLOW.md) · [Game screens](GAME_SCREENS.md) · [Current online guide](ONLINE.md)
