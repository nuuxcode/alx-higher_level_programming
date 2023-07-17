Readme

python3 -m unittest discover -v tests
python3 -m unittest discover tests
python3 -m unittest tests/test_models/test_base.py
find . -name "*.py" -execdir pycodestyle {} +
find . -name "*.py" -print0 | xargs -0 pycodestyle
