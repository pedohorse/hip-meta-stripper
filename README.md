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

works only on commercial hip files as non-commercial files have a proprietary cpio block headers.

### Installation
just copy the contents of `scripts` folder into your user houdini preferences folder
* *(on windows)* `C:\Users\<username>\Documents\houdiniXX.Y\scripts` 
* *(on linux)* `~/houdiniXX.Y/scripts`
* *(on mac)* `~/Library/Preferences/houdini/XX.Y/scripts`

Feel free to open up the `hip,etastrip.py` and readjust it to your needs: some useful constants are set in the top of the file.

For example, if you dont want POSE variable to be spoofed -
just delete the line 
* ```[re.compile(b'set -g POSE = (.*?)$'),           b'set -g POSE = /dev/null'],```

### Usage
#### Automatically on save
**By default** the script is set to run automatically on save.  
It will back up your hip file to `backup/<hipfilename>.orig` in case something goes wrong.  
And your standard backups will also contain the unmodified file.  
This should minimize the risk of losing your hip file to script's bugs.

#### standalone
Also you can run the script completely separately and outside of houdini.  
just run `hipmetastrip.py <path_to_input.hip> <path_to_output.hip>`

For example:  
```hipmetastrip.py scene_042d_final.hip scene_042d_final_nometa.hip```  
if hip files are in your current directory

or use full paths
```hipmetastrip.py D:\prjects\important\scene_042d_final.hip D:\prjects\important\scene_042d_final_nometa.hip```

you can specify just one filename if you want to strip metadata in place  
```hipmetastrip.py D:\prjects\important\scene_042d_final.hip```  
or  
```hipmetastrip.py scene_042d_final.hip```

### Error reporting
Oh yes, please DO report those errors! I'll try to fix them as soon as possible


### Support
you can: [patreon](https://www.patreon.com/xapkohheh)
