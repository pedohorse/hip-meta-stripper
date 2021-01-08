## Hip metadata stripper
Worry about government spying on you?
Duct tape your laptop's camera?
Carry your phone in tinfoil bag from chips?
Confuse local pigeons with David Lynch's movies?

Then you are just like me!

This script acts as a post-save callback that strips potentially unwanted data from your hip fils, such as:
* username
* hostname
* values of HIP and HIPNAME variables (since they are regenerated on startup anyway)
* timestamps

#### Installation
just copy the contents of `scripts` folder into your user houdini preferences folder
* *(on windows)* `C:\Users\<username>\Documents\houdiniXX.Y\scripts` 
* *(on linux)* `~/houdiniXX.Y/scripts`
* *(on mac)* `~/Library/Preferences/houdini/XX.Y/scripts`

Feel free to open up the `hip,etastrip.py` and readjust it to your needs: some useful constants are set in the top of the file.  
For example, if you dont want POSE variable to be spoofed -
just delete the line `[re.compile(b'set -g POSE = (.*?)$'),           b'set -g POSE = /dev/null'],`