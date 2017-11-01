#!/usr/bin/python

"""
Tyler Filko
10/30/18
Setup for Mac OS X DevEnviornment
Need to download Github repo before beginning (save in home)
"""

import subprocess

def mac_dev_setup():
    #Install Homebrew to usr directory
    try:
        print("Updating Homebrew")
        subprocess.check_call(['brew', 'update'])
    except subprocess.CalledProcessError:
        print("installing Homebrew")
        subprocess.check_call('/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"', shell=True)

    print("Installing pyenv")
    subprocess.call(['brew', 'install', 'pyenv'])

    print("Install Pyenv-virtualenv")
    subprocess.call(['brew', 'install', 'pyenv-virtualenv'])

    print("Install direnv")
    subprocess.call(['brew', 'install', 'direnv'])

    #Copy and save pythonrc.py file on usr home
    # print('Creating pythonrc.py simlink')
    # subprocess.check_call(['ln', '-s', '/Users/tafilko/DevelopmentSetup/pythonrc.py', '/Users/tafilko/pythonrc.py'])
    #
    #Updating Bash profile
    #Except catches if user doesn't have access to .bash_profile file, updates so user has read/write ability
    print("Updating .bash_profile")
    subprocess.call(['cat', '/Users/tafilko/', '|','pbcopy'])
    try:
        subprocess.call(['pdpaste', '>', '/User/tafilko/.bash_profile'])
    except subprocess.CalledProcessError:
        subprocess.call_check(['sudo chmod 664', '.bash_profile'])
        subprocess.call(['pdpaste', '>', '/User/tafilko/.bash_profile'])

    print("you are all set to go")

if __name__ == '__main__':
    mac_dev_setup()
