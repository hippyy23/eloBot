import os
import pip

__author__ = "Munteanu Adrian"
__copyright__ = "Copyright 2019, EloBot"
__credits__ = ["Munteanu Adrian"]

__version__ = "0.1"
__email__ = "adrinarol@gmail.com"

boold = True


def check_lib(module):
    '''
    This method checks if the libraries used by exportdata.py are installed
    correctly. If they are not installed, install them automatically.
    '''
    # returns an object with every library installed in the client's pc
    com_d = os.popen('python -m pip list --disable-pip-version-check')
    listd = com_d.read()
    if module in listd:
        if boold:
            print("Library " + module + " already exists")
    else:
        if boold:
            print("Downloading library " + module)
        os.system('python -m pip install ' + str(module) +
                  ' -q --disable-pip-version-check')
        if boold:
            print("Library " + module + " installed")


def check():
    '''
    Passes every package name in the array and sends them as arguments to check_lib().
    '''
    packages = ['bs4', 'requests']
    for i in packages:
        check_lib(i)

check()
