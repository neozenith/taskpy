# tasks.py

**This is for me only and my toy projects. It is not for you. Fork it if you want something different.**

tasks.py is a standalone script runner to automate init, lint, test, start, build, publish steps like npm run using only standard python to bootstrap itself.

## Getting started

**Get the script**

```sh
python3 -c 'from urllib.request import urlretrieve as wget; wget("https://raw.githubusercontent.com/neozenith/taskpy/main/tasks.py", "tasks.py")'
chmod +x tasks.py
```

**Bootstrap initialise**

```sh
# Setup virtual env and default deps and config
./tasks.py init

Requirement already satisfied: pip in ./.venv/lib/python3.9/site-packages (21.3.1)
Generating requirements-dev.txt ...
Generating pyproject.toml ...
Generating .flake8 ...
Installing deps from requirements-dev.txt
```

**Activate and view life cycle tasks**

```sh
# Now activate virtual environment
. ./.venv/bin/activate

invoke --list

Available tasks:

  format
  lint
  test
```
