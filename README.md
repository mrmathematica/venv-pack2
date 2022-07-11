# Venv-Pack

This is based on [venv-pack](https://github.com/jcrist/venv-pack) but with Windows support and Linux long path support
added by [mrmathematica](https://github.com/mrmathematica/)

Venv-pack is a command-line tool for packaging virtual environments for distribution. This is useful for deploying code
in a consistent environment.

Supports virtual environments created using python3/venv. Venv is part of the python standard library.

## Install from source

venv-pack is available on github and can always be installed from source.

```
pip install git+https://github.com/mrmathematica/venv-pack.git
```

## Command-line Usage

One common use case is packing an environment on one machine to distribute to other machines as part of a deployment
process.

### On the source machine

Create venv, and then upgrade pip + setuptools first:
```
python -m venv venv
venv\Scripts\activate
python -m pip install -U pip setuptools
```

Python generates Windows .exe file such as pip.exe on the fly, so on Windows there is restriction that you want to fix a
version of pip and setuptools at the beginning and stick with it. If needed, re-create new venv from a lock file. See
[pip-tools](https://github.com/jazzband/pip-tools).   

Install all your python packages, for example
```
pip install -r requirements.txt
```

Pack the current environment into my_env.zip
```
venv-pack -o env.zip
```

Pack an environment located at an explicit path into my_env.zip
```
venv-pack -p explicit\path\to\env -o env.zip 
```

### On the target machine

Unpack environment into directory `my_env`
```
md my_env
python -m zipfile -e venv.zip my_env\ 
```

Use python without activating the environment. Most python
libraries will work fine, but scripts (e.g. ipython) will fail.
```
my_env\Scripts\python
```

Activate the environment. This adds `my_env\Scripts` to your path
```
my_venv\Scripts\activate
```

Run python from in the environment
```
python
```

Scripts now work fine
```
ipython --version
```

Deactivate the environment to remove it from your path
```
deactivate
```

Finally, there is one trick to run say ipython without activate venv
```
my_venv\Scripts\python my_venv\Scripts\ipython.exe
```
