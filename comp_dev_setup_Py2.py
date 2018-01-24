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
    # Install Homebrew to usr directory
    try:
        print("Updating Homebrew")
        subprocess.check_call(['brew', 'update'], check=True)
    except:
        print("installing Homebrew")
        subprocess.check_call('/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"', shell=True)


    print("Installing pyenv")

    try:
        subprocess.check_call(['brew', 'install', 'pyenv'])
    except subprocess.CalledProcessError:
        print("You already have pyenv")

    print("Install Pyenv-virtualenv")
    try:
        subprocess.check_call(['brew', 'install', 'pyenv-virtualenv'])
    except subprocess.CalledProcessError:
        print("You already have Pyenv-virtualenv")

    print("Install direnv")
    try:
        subprocess.check_call(['brew', 'install', 'direnv'])
    except subprocess.CalledProcessError:
        print("You already have direnv")


    # Copy and save pythonrc.py on usr home
    # If user doesn't have -wr access, this is accomplished using sudo
    print('Creating ~/pythonrc.py and /etc/.inputrc simlink')
    try:
        subprocess.check_call(['ln -s $HOME//pythonrc.py $HOME/pythonrc.py'],shell=True)
    except subprocess.CalledProcessError:
        subprocess.check_call(['sudo ln -s $HOME/DevelopmentSetup/pythonrc.py $HOME/pythonrc.py'],shell=True)
    except:
        print("You already have pythonrc.py setup")

    # Copy and save .inputrc file on usr home
    # If user doesn't have -wr access, this accomplished using sudo
    print('Creating /etc/.inputrc simlink')
    try:
        subprocess.check_call(['ln -s $HOME/DevelopmentSetup/inputrc /etc/.inputrc'],shell=True)
    except subprocess.CalledProcessError:
        subprocess.check_call(['sudo ln -s $HOME/DevelopmentSetup/inputrc /etc/.inputrc'],shell=True)
    except:
        print("You already have this stuff installed")


    # Updating Bash profile
    # Except catches if user doesn't have access to .bash_profile file, updates so user has read/write ability

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
    subprocess.check_call(['cat $HOME/TF_DevSetup/bash_profile_template.txt > $HOME/.bash_profile'],shell=True)

    print("you are all set to go")

if __name__ == '__main__':
    mac_dev_setup()
