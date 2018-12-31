# VComp    

## An video compressor with bitrate and size selection.  

[Github](https://github.com/poyynt/vcomp)  
[PyPI](https://pypi.org/project/vcomp)

### To execute:  
#### In Linux|Unix|macOS:  
##### GUI:  
Run `vcomp` in a shell.  
#### In Windows:
##### Method 1:
In a `cmd` window, execute `vcomp`.  
##### Method 2:
Copy the file `vcomp.exe` from `pythoninstallation\Scripts\` to your desired folder and double-click it.  
#### To use in your python code:  
A code that the **user** sets the compression level.
###### GUI
```python
import vcomp.main
vcomp.main.run()
```
#### To be quiet:  
A code that **you** set the compression level.
Set size to your desired height and bitrate to your desired bitrate, and f to the path of the file.
```python
import vcomp.compress
vcomp.compress.compress(size,bitrate,f)
```
