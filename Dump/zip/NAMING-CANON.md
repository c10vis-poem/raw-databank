# Naming canon

Operator-stated, 2026-08-24. This supersedes every earlier variant in every
document. Where a source document disagrees, the source is preserved verbatim
and this file is the resolution.

| Name | What it is |
|---|---|
| **NovÆxorpus** | The vault repo / universal Data Bank |
| **NovÆxenti** | Agent logic |
| **NovÆxopia** | Agent tools, harness, engine — the "claw" aspect |
| **Æsop-Xi** | Memory layer, context formatting, tool and context orchestration, and protocols — ethical operations and agent protocols |
| **Horizons-Ui** | The UI |
| **Æsc** | Terminal daemon |
| **Æyre** | Voice layer / vision — STT and TTS |

## URL and repo names

Anything that becomes a URL, a repo, a package, or a path uses the **lowercase
single-letter form** — `Æ` becomes `ae`.

| Canon | URL / repo |
|---|---|
| NovÆxorpus | `novae-xorpus` |
| NovÆxenti | `novaexenti` |
| NovÆxopia | `novaexopia` |
| Æsop-Xi | `aesop-xi` |
| Horizons-Ui | `horizons-ui` |
| Æsc | `aesc` |
| Æyre | `aeyre` |

Display names keep the ligature. Only the machine-readable form flattens it.

## Why `x`, and why the one hyphen

Operator-stated, 2026-08-26. In the ligature form the **`x` carries the hard `k`
sound** — `NovÆxorpus`, `NovÆxopia` — and it stays findable there. Flattened to
two separated words the `c` reads as a `z` instead, which is what the `x` fixes.

The vault repo **keeps its hyphen**: `novae-xorpus`. This is deliberate and is
not an inconsistency to be tidied away. The others run together —
`novaexenti`, `novaexopia` — and `aesop-xi` keeps the hyphen its display name
already has.

## Superseded spellings

Found across the corpus and in existing repos. Preserve them where they appear
in a source; do not use them going forward.

| Found as | Canon |
|---|---|
| `NovA-Corpus`, `Nova Corpus`, `NÆX`, `NovÆcorpus` | **NovÆxorpus** |
| `NovÆgenti`, `Novus Agenti`, `NovusÆxenti`, `Novæ-Corpus` | **NovÆxenti** |
| `NovÆcopia Vincet`, `Omni Claw`, `OMNI.CLAW`, `NovÆcopia` | **NovÆxopia** |
| `AESOP XI`, `AESOP_XI`, `aesop`, `Agentic Executions Split Operations Protocol` | **Æsop-Xi** |
| `Horizons UI`, `horizons-ui`, `com.horizons.ui` | **Horizons-Ui** |
| `Æsh`, `daemon.aexenti` | **Æsc** |
| `Æyræ`, `daemon.vocal` | **Æyre** |

## The daemon names are settled

Earlier sources disagreed — `Æsc`/`Æyræ` in one, `Æsh`/`Æyre` in another, and a
third argued the names couldn't be trusted at all. They are now **Æsc** and
**Æyre**, and the logic behind them holds: one is terminal access, one is voice
and vision.

## Structure

The three components run **independently**. Horizons-Ui is the most independent
of them, not the least — it has its own browser, file pickers, chat interface
and model loading, and does not require either daemon to function. Any document
claiming the UI "cannot function without" the daemons is superseded by this.
