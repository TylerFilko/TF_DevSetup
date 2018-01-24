# DevelopmentSetup for Mac OS X
This python script works to install homebrew, pyenv, pyenv-virtualenv, direnv, pythonrc, and update user's bash_profile.

## Features:
- Installs Homebrew, pyenv, Pyenv-virtualenv, direnv
    - This sets up your python dev environments
- Creates pythonrc.py file (simlinked to automatically receive
    updates when github repo pulled)
    - Python history, tab completion, pretty printing, and color
- Updates .bash_profile with necessary hooks (Bash history, tab completion, python environment)


## Notes:
- This runs using the users pre-installed python 2
- Old bash profile will be copied and saved to $HOME/.bash_profile<date> and then will
be replaced by bash_profile_template.txt

## To Run:

```python
cd /path_to/DevelopmentSetup
./comp_dev_setup_Py2      (for mac)
```

## Setting Up Your Python Virtual Environment(s):

### Creating Environment:
```bash
    pyenv virtual-env <python_version> <environment_name>
```

### Activating Virtual Environment:
```bash
    pyenv activate <environment_name>
```
### Deactivating Virtual Environment:
```bash
    pyenv deactivate
```


### Linking Environment To Directory:
```bash
    cd <directory_to_link_to_env>
    pyenv local <environment_name>
```

## Trouble With Python Colors?
### Don't trip Dogg, we got you!
#### Problem: when you open Python within your command window it should look like
![]

Environment Pages/Repos within script:

- Homebrew: https://brew.sh/
- Pyenv: https://github.com/pyenv/pyenv
- Pyenv-virtualenv: https://github.com/pyenv/pyenv-virtualenv
- direnv: https://github.com/direnv/direnv
