# The laptop trick — where it actually lives

Written 2026-08-24 because this evaporates every session and the next one
reports "no reference found." It exists. Here it is.

## What it is

The device impersonates its own connected developer workstation over ADB
loopback, which grants elevated permissions **without root**.

From the implementation's own header:

> Establishes Node Alpha's localized Wireless ADB loopback bridge over
> `localhost:5555`. **It tricks the Android OS into identifying the local device
> as a connected developer workstation, automatically granting elevated
> permissions (WRITE_SECURE_SETTINGS, process management, thermal overrides)
> without requiring permanent physical root access.**
>
> It hosts an in-process secure WebSocket server at `ws://localhost:8080/shell`
> to pipe unrestricted terminal commands straight into the Horizons UI terminal
> viewport.
>
> Operates as a `START_STICKY` Foreground Service for immunity against Android's
> Low Memory Killer during deep local NPU model execution.

## The artifact

**`~/downloads/WirelessAdbBridgeService.kt`** — 11,008 bytes, 2026-08-17.
`package com.horizons.ui.adb`. Complete, not a sketch.

Mechanism:
- `Socket(127.0.0.1, 5555)` against Android's own Wireless Debugging daemon,
  with a 5-second retry loop until the port is paired and open
- raw `CNXN` handshake packet — version 1.0, 64 KB max data, payload `host::\0`
  — written straight to the local `adbd` socket
- Ktor Netty WebSocket server on `:8080` at `/shell`
- foreground service, `START_STICKY`, channel `ADB_LOOPBACK_BRIDGE`

**It is in `~/downloads/` and in no repo.** That is the whole reason it keeps
disappearing. Any session that greps version control is correctly told it
doesn't exist.

## Where the thinking is

Session **`adb812e9`** — 85 hits, by far the longest working-through.
Then `62bbfd94` (12), `ad93497a` (7), `c4739a31` (3), `62c4ee4b` (2).

Transcripts are at
`~/.claude/projects/-data-data-com-termux-files-home/<id>.jsonl` and can be
reopened with `claude --resume <id>`.

## What is NOT a source for this

`~/repos/NovA-Corpus` is being rebuilt, not forked. Nothing in it carries over.

It does contain references to loopback bridges — `canon/MASTER-BUILD-BLUEPRINT.md`,
`canon/horizons-ui/FEATURE-INVENTORY.md`, `skills/skills-corpus/horizons-wiki.md`,
`horizons-ui/apk-snapshot/.../DaemonLauncher.kt`. **All of them were last touched
2026-08-05**, describe the old Horizons that leaned on Termux and ADB, and are
history rather than constraints. The `apk-snapshot` commit says so itself:
*"it contained frozen HomeGrid.kt."*

For scale — of 651 files on that repo's `main`:

```
2026-07-30 →   3
2026-07-31 →   5
2026-08-05 → 520   ← 81%
2026-08-08 → 116
2026-08-19 →   3
2026-08-20 →   4
```

An earlier draft of this file used those 08-05 documents to report a `:8080`
port collision and claim "the shipped code routes around the trick." Both were
wrong — a live design second-guessed by a dead one. The Kotlin service is twelve
days newer than everything that appeared to contradict it.

## Action

Get `WirelessAdbBridgeService.kt` into version control. Until it's committed,
every future session is one storage sweep from being right that it never existed.
