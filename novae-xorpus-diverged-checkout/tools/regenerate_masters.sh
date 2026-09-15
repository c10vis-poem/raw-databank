#!/data/data/com.termux/files/usr/bin/bash
# Regenerates novae-xorpus's MASTER-*.md overview files by concatenating every
# attached project's own file (via the projects/<name>/ symlinks) into one.
# Run manually, or via a project repo's post-commit hook (see AGENTS.md).
# Renamed from regenerate_master_resume.sh 2026-08-31 when CLAUDE.md aggregation
# was added alongside RESUME.md.

set -euo pipefail
cd "$(dirname "$0")/.."

regenerate() {
  local source_file="$1" out="$2" label="$3"
  {
    echo "# Master $label overview (auto-generated — do not hand-edit)"
    echo ""
    echo "Regenerated: $(date -u '+%Y-%m-%dT%H:%M:%SZ')"
    echo "Source: novae-xorpus/tools/regenerate_masters.sh"
    echo ""
    echo "One overview across every attached project. Edit each project's own"
    echo "$source_file, not this file — it's rebuilt from those every time."
    echo ""
    for dir in projects/*/; do
      name=$(basename "$dir")
      if [ -f "$dir/$source_file" ]; then
        echo "---"
        echo ""
        echo "## $name"
        echo ""
        cat "$dir/$source_file"
        echo ""
      fi
    done
  } > "$out"
  echo "Regenerated $out ($(wc -l < "$out") lines) from: $(ls projects/)"
}

regenerate "RESUME.md" "MASTER-RESUME.md" "RESUME"
regenerate "CLAUDE.md" "MASTER-CLAUDE.md" "CLAUDE.md"
