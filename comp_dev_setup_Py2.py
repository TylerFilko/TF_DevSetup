#!/usr/bin/python

"""
Tyler Filko
10/30/18
Setup for Mac OS X DevEnviornment
Need to download Github repo before beginning (save in home)
"""

import subprocess
import datetime

def mac_dev_setup():
    Install Homebrew to usr directory
    try:
        print("Updating Homebrew")
        subprocess.check_call(['brew', 'update'])
    except subprocess.CalledProcessError:
        print("installing Homebrew")
        subprocess.check_call('/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"', shell=True,check=True)

    print("Installing pyenv")
    subprocess.check_call(['brew', 'install', 'pyenv'])

    print("Install Pyenv-virtualenv")
    subprocess.check_call(['brew', 'install', 'pyenv-virtualenv'])

    print("Install direnv")
    subprocess.check_call(['brew', 'install', 'direnv'])

    #Copy and save pythonrc.py file on usr home
    print('Creating pythonrc.py simlink')
    subprocess.check_call(['ln -s $HOME/DevelopmentSetup/pythonrc.py $HOME/pythonrc.py'],shell=True)
    subprocess.check_call(['ln -s $HOME/DevelopmentSetup/inputrc /etc/.inputrc'],shell=True)
    Updating Bash profile
    Except catches if user doesn't have access to .bash_profile file, updates so user has read/write ability

    print("Updating .bash_profile")
    print('backing up .bash_profile as .bash_profile_YYYY_MM_DD at $Home directory')
    time = datetime.datetime.today().isoformat()
    date = time[0:10].replace('-','_')

    # If user doesn't have -wr access, this access is changed
    try:
        subprocess.check_call(['cp $HOME/.bash_profile $HOME/.bash_profile{:s}'.format(date)],shell=True)
    except subprocess.CalledProcessError:
        subprocess.check_call(['sudo chmod 664 .bash_profile'],shell=True)
        subprocess.check_call(['cp','$HOME/.bash_profile',backuploc])

    print('Overwriting the old .bash_profile')
    subprocess.check_call(['cat $HOME/DevelopmentSetup/bash_profile_template.txt > $HOME/.bash_profile'],shell=True)

    print("you are all set to go")

if __name__ == '__main__':
    mac_dev_setup()
