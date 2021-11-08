#!/usr/bin/env python3
# Standard Library
import os
import sys
import shlex
from subprocess import run

# NOTE:
# 1. python ./tasks.py
#    - Bootstrap venv and install invoke and create dummy decorator in interim
# 2. invoke <name of task>
#    - This should successfully import invoke and task decorator
try:
    from invoke import task
except ImportError:
    task = lambda x: x


@task
def lint(c):
    print("lint task")


def _shcmd(command, args=[], **kwargs):
    if "shell" in kwargs and kwargs["shell"]:
        return run(command, **kwargs)
    else:
        cmd_parts = command if type(command) == list else shlex.split(command)
        cmd_parts = cmd_parts + args
        return run(cmd_parts + args, **kwargs)


if __name__ == "__main__":

    if len(sys.argv) >= 2 and sys.argv[1] in ["init"]:
        _shcmd("rm -rfv .venv")
        _shcmd("python3 -m venv .venv")
        _shcmd(".venv/bin/python3 -m pip install --upgrade pip")

        if os.path.isfile("requirements.txt"):
            _shcmd(".venv/bin/python3 -m pip install --upgrade -r requirements.txt")

        # TODO: Bootstrap black, flake8, isort config files
        if os.path.isfile("requirements-dev.txt"):
            _shcmd(".venv/bin/python3 -m pip install --upgrade -r requirements-dev.txt")
    else:
        print(f"This script should be run as:\n\n./tasks.py init\n\n")
        print("This will self bootstrap a virtual environment but then use:\n\n")
        print(". ./.venv/bin/activate")
        print("invoke --list")
