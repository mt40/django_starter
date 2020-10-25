set -e

rm -rf venv
virtualenv -p python3 venv
source venv/bin/activate
python --version
pip install -r requirements.txt