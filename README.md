# DevelopmentSetup for Mac OS X
This python script works to install homebrew, pyenv, pyenv-virtualenv, direnv, pythonrc, and update user's bash_profile.

##Features:##
- Installs Homebrew, pyenv, Pyenv-virtualenv, direnv
    - This sets up your python dev environments
- Creates pythonrc.py file (simlinked to automatically receive
    updates when github repo pulled)
    - Python history, tab completion, pretty printing, and color
- Updates .bash_profile with necessary hooks (Bash history, tab completion, python environment)

##Note:##
- Old bash profile will be copied and saved to $HOME/.bash_profile<date> and then will
be replaced by bash_profile_template.txt

##To Run:##
code(
cd /path_to/DevelopmentSetup
./comp_dev_setup_Py2      (for mac)
)

Enviornment Pages/Repos within script:

Homebrew: https://brew.sh/
Pyenv: https://github.com/pyenv/pyenv
Pyenv-virtualenv: https://github.com/pyenv/pyenv-virtualenv
direnv: https://github.com/direnv/direnv
