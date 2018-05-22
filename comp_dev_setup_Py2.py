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
    # Install Homebrew to usr directory-------------------------------------------------------------
    try:
        print("Updating Homebrew")
        subprocess.check_call(['brew', 'update'], check=True)
    except:
        print("installing Homebrew")
        subprocess.check_call('/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"', shell=True)

    # Installing Atom-------------------------------------------------------------------------------
    try:
        print("Installing Atom")
        subprocess.check_call('brew', 'install', 'atom')
    except subprocess.CalledProcessError:
        print("Seems you already have Atom, or the script is breaking on Atom install")

    # Installing pyenv------------------------------------------------------------------------------
    print("Installing pyenv")
    try:
        subprocess.check_call(['brew', 'install', 'pyenv'])
    except subprocess.CalledProcessError:
        print("You already have pyenv")

    # Installing pyenv-virtualenv-------------------------------------------------------------------
    print("Install Pyenv-virtualenv")
    try:
        subprocess.check_call(['brew', 'install', 'pyenv-virtualenv'])
    except subprocess.CalledProcessError:
        print("You already have Pyenv-virtualenv")

    # Installing direnv-----------------------------------------------------------------------------
    print("Install direnv")
    try:
        subprocess.check_call(['brew', 'install', 'direnv'])
    except subprocess.CalledProcessError:
        print("You already have direnv")


    # Copy and save pythonrc.py on usr home---------------------------------------------------------
    # If user doesn't have -wr access, this is accomplished using sudo
    print('Creating ~/pythonrc.py and /etc/.inputrc simlink')
    try:
        subprocess.check_call(['sudo ln -s $HOME/TF_DevSetup/pythonrc.py $HOME/pythonrc.py'],shell=True)
    except subprocess.CalledProcessError:
        print("You already have pythonrc.py setup or something under that name in that directory")

    # Copy and save .inputrc file on usr home-------------------------------------------------------
    # If user doesn't have -wr access, this accomplished using sudo
    print('Creating /etc/.inputrc simlink')
    try:
        subprocess.check_call(['sudo ln -s $HOME/TF_DevSetup/inputrc /etc/.inputrc'],shell=True)
    except subprocess.CalledProcessError:
        print("You already have .inputrc setup or something under that name in that directory")

    # Updating Bash profile------------------------------------------------------------------------
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
        subprocess.check_call(['cp','$HOME/.bash_profile','$HOME/.bash_profile{:s}'.format(date)])

    print('Overwriting the old .bash_profile')
    subprocess.check_call(['cat $HOME/TF_DevSetup/bash_profile_template.txt > $HOME/.bash_profile'],shell=True)

    print("you are all set to go")

if __name__ == '__main__':
    mac_dev_setup()
