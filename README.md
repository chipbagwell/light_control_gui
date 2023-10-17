# light_control_gui
Light Control GUI for JCHS 2023 Props

# Steps to setup
1.  Download the appropriate version of the Synapse SNAPtoolbelt executable for your system's architecture. https://developer.synapse-wireless.com/snaptoolbelt/install.html
2.  Once you have `toolbelt` installed, plug in the Synapse radio into a USB port.  Windows machines should find the correct serial drivers for it automatically.  Run the following commands
2.1.  `toolbelt config scan` - This will scan looking for Synapse radios and create a profile for them.  The name of the profile will be something like `tty.usbserial-A106NU2I` on a linux or mac system.  The name of the profile will be found in the output of that command as the value of the `name` key.
2.2.  `toolbelt config copy profile <discovered name> default`.  This copies the profile of the newly discovered radio to the default profile.
2.3.  `toolbelt node bridge info` - This will give you the state of the Synapse radio.  If this returns a JSON object of information such as channel and netID, then you are good to go.
2.  Install a recent version of Python on your system.  I am using Python 3.9.5.
3.  Create a new virtual environment to be used with this program.  A python virtual environment is stored as a directory.  
* `python3 -m venv .venv --prompt "light_control_gui"`
4.  Activate your new virtual environment by running the following command: 
*  Windows: `.venv/bin/activate.bat`
*  Linux/MacOS: `source .venv/bin/activate`
5.  Now you can install this repository and all of it's dependencies using `pip install .`
6.  Now you can run the script using `python3 light_control_gui/guiv2.py`