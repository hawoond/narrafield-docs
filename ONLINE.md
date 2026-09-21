# Online session persistence and access

The self-hosted server remains a **shared-party development alpha**. Every player controls the same party character. Individual credentials do not add multiple character ownership, private player notes, chat, owner/operator role separation, or the full seven-person multiplayer specification.

## Starting and restarting

`server.exe -project <project-folder> -operations` loads or creates a session under the operating system's user configuration directory: `Narrafield/server/<hash-of-project-ID>/session.dat`. Use `-state <absolute-private-file>` to select a different session. State files must be outside the project directory. A second process cannot open the same session until the first releases its lock. Normal exit releases the lock; the OS also releases it after process termination.

The session contains game state, the command journal, reconnect credentials, individual credential expirations/revocations, announcements, restrictions and audit history. Successful commands and operations are acknowledged only after a replacement snapshot has been written and synchronized. Write failures return HTTP 503 and leave the in-memory state and committed file unchanged. Restart restores the last committed state, including random state and processed command IDs. Reusing a command ID with a different payload or actor returns HTTP 409; exact retries return the current authoritative projection without applying the action again.

Snapshots are tied to project ID, full content hash, engine version and storage schema. Changed content or corrupt state prevents startup and preserves the original file. Make a backup before changing content; use a new state path for a new session. No automatic migration or content hot reload is provided.

This implementation uses an atomic whole-file snapshot rather than the plan's proposed SQLite database. It targets one local server process and a local filesystem. It does not claim database scaling, network-filesystem locking, automatic backups, or power-loss guarantees beyond OS file synchronization and replacement semantics.

## Protecting server data

On Windows the complete snapshot is encrypted and authenticated with user-bound DPAPI. Run and restore it as the same Windows account; copying the file to a different account or machine is not a portable backup. On Unix, snapshots are owner-readable/writable (0600), and existing files with group/other access are rejected. Symlink state files/parents are rejected. Keep the state directory private and back up its contents separately from distributable game packages. Use an encrypted volume if Unix encryption at rest is required.

The initial GM and legacy shared-player credentials are displayed in the server console, including after a restart; protect the terminal and its logs. They are never included in player state, public packages, participant listings or operation audits. Future random state and internal processed command data are omitted from **both** GM and player HTTP responses. Persistent sessions draw fresh cryptographic entropy before each new command; individual rolls still use the engine's deterministic stream within that command. A fully pluggable cryptographic per-roll provider remains future work.

Serve remote connections through a TLS reverse proxy. The default listener is localhost. This version uses authenticated HTTP snapshots/commands, not the planned WebSocket incremental protocol.

## Individual expiring credentials

Open the maker's GM operations window, or run `operator.exe -server <HTTPS-URL>`. Enter the GM token from the protected server console. The native console keeps it in memory only and provides participant refresh, invitation creation, revocation, announcements, party restrictions and audit history. Invitation tokens appear only in their creation result dialog; copy and share them deliberately with the intended recipient. Close that dialog to clear its token field. The console rejects remote plaintext HTTP and redirects, and applies request deadlines and response size limits.

All endpoints require `Authorization: Bearer <credential>`. Only the GM may manage participants, independently of whether the optional operations module is enabled.

| Endpoint | Request / response |
| --- | --- |
| `POST /participants/invite` | JSON `{"id":"alice","expires":"2030-01-01T00:00:00Z"}`; choose a real expiry after now and within 30 days. HTTP 201 returns the credential once. |
| `GET /participants` | IDs, expiration times and revoked flags; no credentials. |
| `POST /participants/revoke` | JSON `{"id":"alice"}`; HTTP 204. Further requests with that credential return HTTP 401, including after restart. |

There can be up to six active individual credentials. IDs cannot be reused; use a new ID for a replacement invitation. These credentials can be passed directly to the existing player's token field. An expired credential is rejected on every request. The legacy shared-player token remains available for backward compatibility and is not individually revocable; do not distribute it when individual revocation is needed. Party restrictions apply to all player credentials. Identity management records persist even when optional operations endpoints are disabled.

## Runtime images

`GET /media?path=<URL-encoded-managed-image-path>` serves previously verified project image bytes after normal authentication/restriction checks. Players can request only the current scene's background and portrait; future-scene images return HTTP 404. GM access is limited to loaded referenced project images. Responses disable caching and MIME sniffing. Scene state carries the current background and portrait references.

## Verification

`go test ./internal/networking ./internal/operations ./cmd/server` covers restart equivalence, credential continuity, replay and payload conflicts, exclusive opening, content mismatch/corrupt-state preservation, persistence rollback for commands/operations/invitations, revocation after restart, persisted bans and audit history, GM/player authorization and secret filtering. Network latency/load, certificate deployment, per-character ownership and disconnect grace handling remain separate acceptance work.
