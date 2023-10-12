# light_control_gui
Light Control GUI for JCHS 2023 Props

# Steps to setup
1.  Download the appropriate version of the Synapse SNAPtoolbelt executable for your system's architecture. https://developer.synapse-wireless.com/snaptoolbelt/install.html
2.  Install a recent version of Python on your system.  I am using Python 3.9.5.
3.  Create a new virtual environment to be used with this program.  A python virtual environment is stored as a directory.  
* `python3 -m venv .venv --prompt "light_control_gui"`
4.  Activate your new virtual environment by running the following command: 
*  Windows: `.venv/bin/activate.bat`
*  Linux/MacOS: `source .venv/bin/activate`
5.  Now you can install this repository and all of it's dependencies using `pip install .`
6.  Now you can run the script using `python3 light_control_gui/guiv2.py`