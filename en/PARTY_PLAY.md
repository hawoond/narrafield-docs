---
title: Online parties and campaigns
description: Planned personal and shared parties, action order, split exploration, lobbies, reconnection, and campaign recovery.
content_status: planned
---

# Online parties and campaigns

Different games need different ways to share a world. The latest design lets creators combine party structure, control, action order, and exploration rules.

## Starting party templates

| Template | Control model |
| --- | --- |
| Individual-character cooperation | Each player controls one character in a shared party |
| Personal-party cooperation | Each player builds and controls a party of several characters |
| Shared-party assignments | Characters from a shared roster are assigned to different players |
| Mixed | Players control different numbers of characters |

**Ownership**, active **control**, **party membership**, **combat side**, and the **conversation representative** are separate concepts. Being the representative or party leader does not automatically grant control over another player's characters, equipment, or funds.

Planned rules cover roster and active-party limits, formation changes, shared storage, rewards, absence, GM substitution, and agreed delegation. Character count is distinct from player count. Supported scale will depend on verified server configurations.

## Define action order and exploration separately

Planned combat templates include **character turns, player turns, side turns, and simultaneous planning followed by resolution**. In simultaneous planning, game rules should determine resolution order rather than network arrival time.

Exploration can use **shared travel, individual exploration, or party splitting and reunion**. Separate scenes must respect information visibility, shared world time, and single execution of common events.

## From joining to the next session

1. **Host or join:** identify player hosting, a dedicated server, or a creator-operated service.
2. **Prepare in the lobby:** review roles, characters, parties, approvals, readiness, and blocking conditions.
3. **Play:** distinguish the selected character, action target, and pending request. Pings, shared plans, chat, and conversation catch-up are planned collaboration tools.
4. **Leave and return:** preserve control and progress, then review permitted events and objectives.
5. **Resume or recover a campaign:** handle session saves, updates, server transfer, and recovery separately. An individual player's Load action should not roll back shared progress.

Basic access and command checks should remain active when optional operations modules are disabled. Room owner, host, GM, and operator have distinct responsibilities.

## Check control, speech, and consent separately

Permission to move a character, speak as that character, and spend another player's resources or share their information are distinct. Delegation has a subject, scope, duration, and revocation conditions. Leadership or majority voting cannot replace personal consent. [Roleplay chat](ROLEPLAY_CHAT.md) follows the same rules for speaker selection.

GM-free shared proposals follow the game's proposal, voting, and execution rules, with cancellation or reselection for ties, refusal, timeouts, or absence. Shared pauses and session endings also need explicit policies. See [Campaign continuity](CAMPAIGN_FLOW.md).

Party information, each character's knowledge and beliefs, and what a player has read remain distinct. Events in another party are not automatically known, and personal reputation is not silently merged into party reputation. See [world information](WORLD_STORIES.md).

## Test the time spent waiting

Mixed character counts, split scenes, and GM approval queues need checks for waiting and participation opportunities. Optional turn reminders, time limits, and return summaries should help without forcing quieter players to speak. These belong to [multi-participant testing](TEST_AND_RELEASE.md).

## Compare with the current demo

The demo includes personal invitations and character assignment, private notes and lore visibility, GM NPC control and AI pause, WebSocket state synchronization and reconnect, and persisted server state. Multiple personal parties, unrestricted split scenes, integrated lobbies, chat, and complete server-transfer and recovery flows are not finished.

Use [Online sessions](ONLINE.md) for current instructions. Release dates and supported concurrent player counts for these planned workflows are not announced.

[Starting a game](PLAYER_START.md) · [Game screens](GAME_SCREENS.md) · [Current capabilities](DEVELOPMENT.md)
