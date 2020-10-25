set -e

source venv/bin/activate

pylint $(git ls-files --full-name | grep .py)