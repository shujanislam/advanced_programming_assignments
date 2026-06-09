#!/usr/bin/env bash
set -euo pipefail

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  printf 'Error: this script must be run inside a Git repository.\n' >&2
  exit 1
fi

if ! git diff --quiet || ! git diff --cached --quiet; then
  printf 'Error: commit or stash your current changes before running this script.\n' >&2
  exit 1
fi

current_branch=$(git branch --show-current)
branches=$(git for-each-ref --format='%(refname:short)' 'refs/heads/assign*' | sort -V)

if [ -z "$branches" ]; then
  printf 'No assign* branches found.\n'
  exit 0
fi

if [ ! -r /dev/tty ]; then
  printf 'Error: this script needs an interactive terminal.\n' >&2
  exit 1
fi

cleanup() {
  if [ -n "${current_branch:-}" ]; then
    git switch "$current_branch" >/dev/null 2>&1 || true
  fi
}
trap cleanup EXIT

printf 'This will update README.md on each assignment branch.\n'
printf 'Paste the question for each branch, then type a line containing only END.\n'
printf 'Leave the question empty to skip that branch.\n\n'

while IFS= read -r branch; do
  [ -n "$branch" ] || continue

  printf '\n==> %s\n' "$branch"
  git switch "$branch" >/dev/null

  printf 'Paste the question for %s, then type END on its own line:\n' "$branch"
  question=''
  while IFS= read -r line </dev/tty; do
    [ "$line" = 'END' ] && break
    if [ -z "$question" ]; then
      question=$line
    else
      question=$(printf '%s\n%s' "$question" "$line")
    fi
  done

  if [ -z "$question" ]; then
    printf 'Skipped %s because no question was entered.\n' "$branch"
    continue
  fi

  cat >README.md <<EOF
# $branch

## Question

$question
EOF

  git add README.md
  if git diff --cached --quiet; then
    printf 'No README changes for %s.\n' "$branch"
    continue
  fi

  git commit -m "Add question for $branch" >/dev/null
  printf 'Updated and committed README.md on %s.\n' "$branch"
done <<EOF
$branches
EOF

printf '\nFinished updating assignment branch READMEs.\n'
