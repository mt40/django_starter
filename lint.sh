set -e

source venv/bin/activate

current_branch=$(git branch --show-current)
printf "lint files in branch %s\n" "$current_branch"
pylint $(git ls-tree -r --name-only "$current_branch" | grep .py)