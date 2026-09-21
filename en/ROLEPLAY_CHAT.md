---
title: Roleplay together through conversation
description: Speak as a character, describe actions, and keep track of conversations with the planned roleplay chat.
content_status: planned
---

# Roleplay together through conversation

We are building chat that lets a GM and players run a session through dialogue and written actions. **Basic RP chat is planned for the first release.** Action proposals, dialogue effects, special communications, and advanced record tools will follow. Integrated chat is not yet available in demo {{ site.data.review.demo_version }}.

## Who is speaking, and to whom?

| Mode | Meaning |
| --- | --- |
| Character dialogue | Speak with an assigned character's public name and portrait |
| Action description | Describe roleplay such as unfolding a map, without confirming numerical effects or another character's action |
| Player conversation (OOC) | Breaks, schedules, and conversation outside character knowledge |
| GM narration / NPC dialogue | Narrate events or speak for an authorized NPC using its public identity or alias |
| Checks / game results | Engine-confirmed events, visually distinct from ordinary messages |

The message box will always show **how you are speaking, who you are speaking as, and who will receive the message**. Current-scene, party, all-participant, individual whisper, and GM recipients are separate. Spectator speech follows the game's policy. Games without characters can use OOC conversation and GM narration.

If a configuration allows GMs to read whispers, it should disclose that before sending. A GM channel identifies which GMs receive it. Joining later or changing roles must not automatically reveal earlier private messages.

## Separate control, speech, and consent

Delegated combat or movement control does not automatically grant RP speech rights. When delegating speech, choose the character, who may speak for them, what is allowed, how long it lasts, and how to revoke it. Consent to relationships, promises, and sacrifices remains separate.

A dialogue choice that changes rules checks decision authority; free dialogue checks speech permission. A choice combining both requires both. Changing character or scene should not silently replace a draft's speaker or recipients. Permissions are checked again when the message is sent.

## A chat layout for the game

- **Text roleplay:** central RP, descriptions, narration, results, and input, with OOC and whispers in distinct views.
- **Scene-focused:** open or pin a chat panel while viewing the scene.
- **Tabletop / tactical:** chat beside the map, with essential checks and choices separately accessible.

New messages should not force readers away from older records. Unread positions and return-to-current controls are planned, together with large text, keyboard operation, Korean IME handling, and draft/focus preservation through notifications and reconnection. Basic chat should work without the advanced screen editor, an LLM, or the optional operations console.

## Records and personal protection

Basic goals include sending/sent/failed states, duplicate-free retries, reconnection, replies, quotations, pinned messages, and edit/delete indicators. Retention, backups, and export policies should be visible. Rolling back a game save must not secretly delete or resend people's conversations.

Personal blocking/muting and room speech limits are basic online protections. They should preserve essential choices, recovery, and help. When a GM's absence pauses play, authenticated player conversation and recovery guidance should remain available while the server is reachable.

A player reading a clue and a character acquiring it are different. Only an explicitly connected knowledge-transfer action changes character knowledge. Search, quotations, summaries, and exports use the same visibility rules. [Facts, rumors, and knowledge](WORLD_STORIES.md)

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

[Parties and permissions](PARTY_PLAY.md) · [Lobbies, sessions, and return](CAMPAIGN_FLOW.md) · [Screen concepts](GAME_SCREENS.md) · [Current online guide](ONLINE.md)
