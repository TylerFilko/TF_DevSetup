# DevelopmentSetup for Mac OS X
This python script works to install homebrew, pyenv, pyenv-virtualenv, direnv, pythonrc, and update user's bash_profile.

## Features:
- Installs Homebrew, pyenv, Pyenv-virtualenv, direnv
    - This sets up your python dev environments
- Creates pythonrc.py file (simlinked to automatically receive
    updates when github repo pulled)
    - Python history, tab completion, pretty printing, and color
- Updates .bash_profile with necessary hooks (Bash history, tab completion, python environment)

## Requirments:
- git
- Github

## Notes:
- This runs using the users pre-installed python 2
- Old bash profile will be copied and saved to $HOME/.bash_profile<date> and then will
be replaced by bash_profile_template.txt

## To Run:
1. Clone this repo into your home directory
2. Run the setup script
```bash
cd /path_to/DevelopmentSetup
python comp_dev_setup_Py2.py      (for mac)
```
3. Enjoy :)

## Setting Up Your Python Virtual Environment(s):

### Creating Environment:
```bash
    pyenv virtualenv <python_version> <environment_name>
```
##### Installing Python versions for pyenv: 
If you don't have python versions installed spesifically for pyenv you can run 
```bash
pyenv install -l
```
to view the versions available and then 
```bash
pyenv install <version> 
``` 
to install the version of your choosing


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

## Trouble/Problems?
### Don't trip Dogg, we got you!
#### Problem & Possible Solutions:
1. When you open Python within your command window it should look like
![problem_img](https://github.com/TylerFilko/TF_DevSetup/blob/master/example_imgs/DevSetup_ex.png?raw=true)
 - If not, run this command and will all be ok (hopefully)
 ```bash
 sed '1 s/$/_HiStOrY_V2_/' $HOME/.pyhistory
 ```
- For more info on this fix: https://stackoverflow.com/questions/17824898/why-does-readline-read-history-file-give-me-ioerror-errno-2-no-such-file-or
2. Is it just not running?
- Did you clone the repo into your $HOME directory? If not sure, check (command below displays home directory)
```bash
echo $HOME
```
- What branch did you grab? Was it 'master' ?
```bash
git branch
```
If the branch denoted by the asterisk is not master
```bash
git checkout master
```

Environment Pages/Repos within script:

- Homebrew: https://brew.sh/
- Pyenv: https://github.com/pyenv/pyenv
- Pyenv-virtualenv: https://github.com/pyenv/pyenv-virtualenv
- direnv: https://github.com/direnv/direnv

testing
