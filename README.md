Clone this repo, then execute this workflow:

```
python3 -m venv venv
source venv/bin/activate
pip install pip==20.1.1
pip install pip-tools==5.2.1
pip-compile requirements.in > requirements.txt
pip install -e .
```

The last command will exit with this error:

```
    error in pkg setup command: 'install_requires' must be a string or list of
    strings containing valid project/version requirement specifiers; Invalid
    requirement, parse error at "'+https:/'"
    ----------------------------------------
ERROR: Command errored out with exit status 1: python setup.py egg_info Check
the logs for full command output.
```

The same workflow with pip 20.0.2 works without errors.

The created `requirements.txt` includes 

```
git+https://github.com/gtaylor/python-colormath.git@6cb12bf#egg=colormath@https://github.com/gtaylor/python-colormath/tarball/6cb12bf  # via -r requirements.in
```

Compared to the `requirements.in`, the name `colormath` at the beginning was removed.

If I manually modify this line in `requirements.txt` to include the name

```
colormath @ git+https://github.com/gtaylor/python-colormath.git@6cb12bf#egg=colormath@https://github.com/gtaylor/python-colormath/tarball/6cb12bf  # via -r requirements.in
```

then `pip install -e .` runs fine in pip 20.1.1 (and this still works with pip 20.0.2).

Does that mean that `pip-compile` should include the package name when generating a VCS-url requirement? Need to check [PEP 440](https://www.python.org/dev/peps/pep-0440/) and [PEP 508](https://www.python.org/dev/peps/pep-0508/)
