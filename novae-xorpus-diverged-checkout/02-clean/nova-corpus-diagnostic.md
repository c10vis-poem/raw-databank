---
source: NovA-Corpus Diagnostic.pdf
cleaned: 2026-08-26
converter: pymupdf get_text()
source_pages: 9
---
D E V I C E & V A U L T F I N D I N G S
NovA-Corpus Diagnostic
Everything found while looking into remote control, the dropped session,
and why the Obsidian master wiki keeps falling apart — written out plainly,
with the evidence behind each claim.
12 AUG 2026
MOTOROLA RAZR ULTRA 2025 · ANDROID 16
TERMUX · CLAUDE CODE 2.1.228
Act on this now
One item. It has nothing to do with the wiki, and it doesn't keep.
CRITICAL
git / credentials
A live GitHub token is sitting in a config file in plaintext
Your obsidian-skills fork has a personal access token baked dire
URL, stored unencrypted in ~/repos/obsidian-skills/.git/config
https://c10vis-poem:ghp_PZUS
@github.com/c10vis-poem/
Anything that can read your home directory can read that token an
GitHub. It was also pulled into a chat transcript when the repo con
In plain terms: that string is a password for your GitHub account, wri
ordinary text file instead of a vault. Go to github.com/settings/tokens,
one, and store it with a credential helper rather than pasting it into the
in this report can wait. This shouldn't.
Why your sessions keep dying
You were right that something killed it. You were watching the wrong indicator.
••••••••••••••••••

DIAGNOSED
android / power
The wake lock was held. It was never going to save you.
A Termux wake lock is a partial wake lock: it stops the CPU
from going to sleep. It does nothing to stop Android from killing
the process outright. Those are two separate mechanisms, and
it was the second one that ate your session when you switched
to the tablet and Termux dropped into the background.
Two likely killers, both consistent with what happened:
CAUSE
FIX
REACHABLE FROM
HERE?
Motorola battery
management —
aggressive by default on
this device
Settings → Apps → Termux
→ Battery → Unrestricted
No — GUI only
Phantom process killer
(Android 12+) reaping
Termux child processes
settings put global
settings_enable_monitor_ph
antom_procs false via adb
or Shizuku
No — blocked
Both settings were probed and both refused:
SecurityException , because getCurrentUser() requires the
INTERACT_ACROSS_USERS permission that Termux doesn't hold.
So the current state of either one is genuinely unknown.
Being straight about confidence: which one killed it has not been
proven. What has been proven is that "wake lock is held" can be
true while the session still dies — so that notification isn't the
reassurance it looks like. Battery management is the likelier culprit
on a Razr and the easier fix, so start there.
RECOVERABLE
session 136ea897
The session that dropped is not gone
Claude Code writes every conversation to disk as it happens. A
kill costs you the connection, never the conversation. The one

that died is 914 KB of transcript in ~/.claude/projects/…/ ,
covering 02:06 → 02:29 UTC.
claude --resume 136ea897-fae7-4217-b685-78109cbd63ec
For the record, it died mid-sentence hunting your handoff file.
Its last words were "there's both a Download and a Downloads
folder — two different places, classic trap. Searching all of it:" —
and then Android reaped it. It was searching the wrong place
regardless; see below.
Where your things actually are
Two searches that had failed repeatedly, now closed out.
FOUND & SECURED
handoff files
The handoffs were in a temp folder that wipes itself
Both exist and are intact. They were written to Termux's $TMPDIR —
home directory, not shared storage — which is exactly why every p
search missed them:
/data/data/com.termux/files/usr/tmp/handoff-nova-corpus-2026-08-10.md 
/data/data/com.termux/files/usr/tmp/handoff-nova-corpus-2026-08-11.md 
Both are now copied into the vault under NovA-Corpus/ and verifie
checksum — identical bytes, nothing overwritten, originals left in p
handoff-nova-corpus-2026-08-10.md   ab83324c…   OK
handoff-nova-corpus-2026-08-11.md   f24e6bab…   OK
Why this mattered: $TMPDIR gets cleared by Android or by Termux
housekeeping, without warning. Those two files were the only survivin
a session that cost $50+ before you checkpointed it. They were one clea
from gone.

RECORDED
vault identity
There are eight Obsidian vaults on this device
You confirmed the live one is
/storage/emulated/0/OBSIDIAN_VAULT/OBSIDIAN_VAULT.md/ — a
directory literally named OBSIDIAN_VAULT.md . The other seven
are decoys, including a sibling OBSIDIAN-WIKI.md sitting in the
very same parent folder.
That's now written to memory so no future session has to guess
or ask you again. Current contents: 421 MB, 335 markdown
files, project material under NovA-Corpus/ .
The master wiki: what's wired, what isn't
Most of it is already in place. The gap is far smaller than it has been feeling.
COMPONENT
STATE
DETAIL
Obsidian app
installed
md.obsidian
Markor
installed
net.gsantner.markor
rclone + Drive remote
configured
gdrive: remote present
obsidian-skills fork
cloned
~/repos/obsidian-skills — origin your fork, upstream
kepano
Skills loaded in Claude
Code
live
obsidian-cli, markdown, bases, json-canvas, defuddle
obsidian-cli binary
MISSING
the skills call a program that isn't on the device
Vault under git
not a repo
no .git anywhere in the vault
Vault ↔ Drive sync
nothing running
no bisync configured
ROOT CAUSE
This is your "uploaded it but it never got wired up"

obsidian-cli
The skill repo is fully installed and its skills are loaded and
visible. But the one that actually manipulates the vault shells
out to an obsidian-cli binary that was never installed here.
The skill loads fine, then fails the instant it tries to do anything
real.
In plain terms: you installed the instructions but not the tool the
instructions tell it to use. That's a one-package gap, not a broken
design — which is a very different problem from the one it's been
feeling like.
DECIDED
topology
The shape you asked for
Your answer — "obviously it's the device file" — settles the
question that's been open since the folder-naming discussion.
The on-device vault is the source of truth, and everything else
hangs off it:
SOURCE OF TRUTH
/storage/…/OBSIDIAN_VAULT.md/
Obsidian
reads directly
Markor
reads directly
GitHub
git push
Google Drive
rclone bisync
DEVICE CANONICAL · FOUR CONSUMERS · NOTHING EDITS A COPY
This shape is also forced by a constraint worth knowing:
Obsidian and Markor are sandboxed Android apps and cannot
read /data/data/com.termux/files/home at all. Any design that
puts the real vault inside Termux's home directory breaks both
apps immediately. That squeeze — the apps need shared
storage, git prefers a real filesystem — is very likely what broke
the earlier attempts.
One consequence to plan around: shared storage is a fuse
filesystem. Git runs there, but there are no symlinks and no
reliable permission bits, so the repo will want core.filemode

p
p
false .
Why sync is "always a losing battle"
You called this one correctly. Here's the evidence, and why it keeps happening.
BLOCKER
81 files
The vault is already full of duplicates before any sync starts
Two files in the vault root, both 30.3 MB, same checksum — byte-fo
identical copies of one arXiv paper under two different Drive-man
names:
a62ed23df49755b60a11044706c8ad74   " Continual Harness- …2605.09998v1 
a62ed23df49755b60a11044706c8ad74   "2605.09998v1 (2) 1.pdf"
That's 60.6 MB of a 421 MB vault spent storing one document twice
leading space in the first filename — it broke one of the investigati
commands mid-run.
And it isn't isolated. 81 files in the vault carry Drive-duplication na
artifacts:
Copy of overlayd-ai-technical-guide (1) (1) (2).pdf
(Preface) Multi-Corpora Ecosystem. (1).pdf
README (1).md
…Google Search (3)-compressed (2).pdf
EXPLANATION
sequencing
The sync tool isn't broken. It's being handed 81
unanswerable questions.
Every attempt so far has switched on two-way sync across a
tree that was already duplicated. rclone bisync in particular
will either abort or start fighting itself when it meets pairs like
these, because it genuinely cannot tell which side is
authoritative. So it errors out — or it picks wrong and mints a

p
g
fresh (1) generation. Next round, there are more of them.
In plain terms: it isn't choking on a bug. It's choking on real
ambiguity it's being handed. Cleaning has to come before
connecting, and that ordering is the entire fix.
This isn't a new plan, either. Your own 2026-08-11 handoff
already lays out the correct order — and flags that the job
never started:
1
Enumerate — what belongs in each bucket (canonical,
empirical, corporate)
2
Dedup pass — collapse the identical and near-identical
copies
3
Keyword sweep — catch anything missed under similar
terms
Every failed attempt has been an attempt at what comes after
step 3, without ever doing step 2.
Still open
Nothing below has been started or decided.
AWAITING YOU
scope
How much to do in one go
Source of truth is settled; scope isn't. The options on the table:
fix obsidian-cli only, wire everything in verified stages, or
write the full plan first and change nothing. Given this has
fallen apart before, staged work with a check after each step is
the cautious read — but that's your call, not mine.

NOT STARTED
binaries in git
What to do with 421 MB of PDFs and an 81.6 MB zip
Raw binaries that large don't belong committed into a git repo.
Git LFS, a .gitignore that keeps them Drive-only, or simply
accepting the bloat are all legitimate choices with real trade-
offs. Not a decision to be made silently on your behalf.
OWED TO YOU
prompt caching
The prompt caching explanation
You said you read the handed-off caching doc and couldn't
make heads or tails of it. That's still outstanding, and
deliberately not attempted here — handing you a second dense
document about the first dense document would miss the point
entirely. When you want it, it gets read fresh from the current
official material and explained in the register of this report, not
that one.
Glossary
Every term used above that assumed knowledge it had no business assuming.
wake lock
A request that stops the phone's processor from sleeping. It
does not stop Android from killing your app — which is the
whole misunderstanding behind the dropped session.
phantom process killer
A feature in Android 12 and later that hunts down
background processes started by apps like Termux and
terminates them, wake lock or no wake lock.
$TMPDIR
A scratch folder for temporary files. Anything in it can be
deleted at any moment without warning. Your handoffs were
living there.
md5 / checksum
A short fingerprint calculated from a file's contents. Two files

with the same fingerprint are identical byte for byte — which
is how the duplicate PDFs were proven rather than guessed at.
fuse
The kind of filesystem Android uses for shared storage. It can't
store Unix permission bits or symbolic links, which is why git
needs special settings to live there.
rclone bisync
Two-way sync between a local folder and cloud storage,
changes flowing in both directions. It's the mode that breaks
when it finds files it can't tell apart.
source of truth
The one copy that wins when copies disagree. Without picking
one, every sync is a coin flip. Yours is now the on-device vault.
git LFS
An add-on that stores large binary files outside the main
repository so it doesn't balloon. The usual answer for PDFs
and zips in a repo.
spawn mode
How Remote Control handles new sessions. same-dir keeps a
server running that accepts many of them; session is single-
session and exits when that one ends.
sandboxed
Android's rule that an app may only read its own files plus
shared storage. It's why Obsidian and Markor physically
cannot see anything inside Termux's home directory.
Every claim above was verified on-device rather than assumed. Where something could not be
verified — the two Android power settings — it's stated as unverified rather than papered over.
