---
title: From the first session to the next
description: Explore planned tools for ending a session, returning at the next meeting, and recovering a campaign.
content_status: planned
---

# From the first session to the next

We are building ways to take a break and return, end a session and continue at the next meeting, or finish a campaign with an epilogue. For the demo's actual save slots and server snapshots, follow [Play and export](PLAY_AND_EXPORT.md) and [Online sessions](ONLINE.md). The integrated campaign workflow below remains a development goal.

## From a lobby to a new game

A lobby should show roles, character candidates, readiness, and reasons play cannot start. Lobby conversations are kept and linked to the campaign **when the new game is confirmed**. Linking should neither resend messages nor expand recipients. Selecting a candidate does not itself grant speech rights for that character.

A new game creates separate progress and applies initial state and grants once. Loading restores saved progress without repeating character creation or initial rewards. Late arrivals see permitted records, with preparation distinct from a confirmed character. [Starting and creating characters](PLAYER_START.md)

## Pause, end a session, or finish a campaign

| Action | Continuing state |
| --- | --- |
| Personal menu / disconnection | Changes the personal interface or connection, not the shared session or world time |
| Pause / save and stop | Preserves the current session and pending work for resumption |
| End session | Reviews unfinished work and explicit settlement before closing that session |
| Start next session | Retains characters, spent resources, relationships, and knowledge without repeating initial grants |
| Next chapter / scenario | A story transition that may happen within the same session |
| Complete campaign | Moves to epilogue and archival state; further play requires an allowed resume or branch option |
| Inherit into a new campaign | Reviews selected consequences before creating separate progress |

Ending a session does not automatically advance a day, rest, recover resources, or run faction activities. Effects follow the game's explicit time and event boundaries. Ongoing long-term promises and quests remain in the campaign.

## Handle unresolved decisions

Before ending, review pending checks, costs, trades, GM requests, and delayed communications. Depending on the game, **resolve now / cancel with the appropriate refund / carry forward**. A carried-over decision keeps a record of who must answer, how much time remains, and which resources are reserved. Saving and stopping should remain possible when resolution is unavailable. An end-session button does not provide another player's consent.

While waiting, the game will show who needs to decide and what happens if they refuse, leave, or run out of time. Shared proposals and session endings without a GM use registered rules and agreement policies rather than waiting for a nonexistent GM account. [Parties and shared decisions](PARTY_PLAY.md)

## Keep improvised clues when returning

Temporary GM NPCs, items, clues, actions, and approved world proposals are planned as **campaign-specific content**. Saves, reconnection, and recovery restore them alongside their original content version. They do not automatically modify another campaign or the creation source.

To reuse them in another work, a creator reviews a proposed change. They check the source, permission to distribute it, secrets, and conflicts with existing content, and exclude private conversations. Being a GM does not itself authorize changes to the creation project or Git repository.

## Updates and recovery

Content, plugin, and screen updates should not immediately alter an active campaign. The plan checks version and save compatibility, tests migration on a copy, and preserves the original. Server transfers and recovery also review pending choices, temporary definitions, chat branches, and external reward records.

Rewinding game state is different from deleting people's conversation. Recovery will show which point was restored and what was lost. Reconnection, opening summaries, or starting another session must not repeat confirmed rewards or messages. [Roleplay records](ROLEPLAY_CHAT.md)

[World legacies](WORLD_STORIES.md) · [Testing and release](TEST_AND_RELEASE.md) · [Current compatibility guide](TROUBLESHOOTING.md)
