"""
Tyler Filko
10/30/18
Setup for Mac OS X DevEnviornment
Need to download Github repo before beginning (save in home)
"""

import subprocess

def MacDevSetup():
    #Install Homebrew to usr directory
    subprocess.run('/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"')

    #Install Pyenv via Homebrew
    subprocess.run('brew update')
    subprocess.run('brew install pyenv')

    #Install Pyenv-virtualenv
    subprocess.run('brew install pyenv-virtualenv')

    #Install direnv
    subprocess.run('brew install direnv')

    #Copy and save pythonrc.py file on usr home
    subprocess.run('cp pythonrc.py ./Users/tafilko/DevelopmentSetup')        #can i do this? ,

    #Updating Bash profile
    #Except catches if user doesn't have access to .bash_profile file, updates so user has read/write ability
    try:
        subprocess.run('open .bash_profile')
    except:
        subprocess.run('sudo chmod 664 .bash_profile')
        subprocess.run('open .bash_profile')
    finally:
        subrocess.run('cat /Users/tafilko | pbcopy')
        subprocess.run('pdpaste > /User/tafilko/.bash_profile')

    print("you are all set to go")
