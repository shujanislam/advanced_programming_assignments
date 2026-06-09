#!/usr/bin/env bash
set -euo pipefail

remote="${1:-origin}"

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  printf 'Error: this script must be run inside a Git repository.\n' >&2
  exit 1
fi

if ! git remote get-url "$remote" >/dev/null 2>&1; then
  printf 'Error: remote "%s" does not exist.\n' "$remote" >&2
  exit 1
fi

remote_url=$(git remote get-url "$remote")
askpass_file=""

cleanup() {
  if [ -n "$askpass_file" ] && [ -f "$askpass_file" ]; then
    rm -f "$askpass_file"
  fi
}
trap cleanup EXIT

case "$remote_url" in
  http://*|https://*)
    printf 'Git username: '
    read -r git_username
    printf 'Git password or personal access token: '
    stty -echo
    read -r git_password
    stty echo
    printf '\n'

    askpass_file=$(mktemp)
    chmod 700 "$askpass_file"
    cat >"$askpass_file" <<'ASKPASS'
#!/usr/bin/env bash
case "$1" in
  *Username*) printf '%s\n' "$GIT_PUSH_USERNAME" ;;
  *Password*) printf '%s\n' "$GIT_PUSH_PASSWORD" ;;
  *) printf '\n' ;;
esac
ASKPASS

    export GIT_ASKPASS="$askpass_file"
    export GIT_PUSH_USERNAME="$git_username"
    export GIT_PUSH_PASSWORD="$git_password"
    export GIT_TERMINAL_PROMPT=0
    ;;
  *)
    printf 'Remote uses SSH or local URL; Git will use your configured authentication.\n'
    ;;
esac

current_branch=$(git branch --show-current)
branches=$(git for-each-ref --format='%(refname:short)' refs/heads/main refs/heads/assign* | sort -V)

if [ -z "$branches" ]; then
  printf 'No main or assign* branches found to push.\n'
  exit 0
fi

printf 'Pushing branches to %s:\n' "$remote"
printf '%s\n' "$branches"

while IFS= read -r branch; do
  [ -n "$branch" ] || continue
  printf '\n==> Pushing %s\n' "$branch"
  git push -u "$remote" "$branch"
done <<EOF
$branches
EOF

if [ -n "$current_branch" ]; then
  git switch "$current_branch" >/dev/null
fi

printf '\nAll requested branches were pushed.\n'
