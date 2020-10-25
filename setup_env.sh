set -e

rm -rf venv
virtualenv -p python3 venv
source venv/bin/activate
python --version
python -m pip install --upgrade pip
pip install -r requirements.txt