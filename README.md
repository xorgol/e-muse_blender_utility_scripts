# E-MUSE Blender utility scripts
A few small scripts for making our Blender workflows easier and faster.
Developed for [E-MUSE](https://e-muse.it).

## How to use
Go to the Scripting tab, press Open, load up the script you want to use, press Alt + P or the Run button to execute the script.

### Individual Objects To Files
Exports all objects to individual GLBs, keeping their world coordinates and compressing the materials. Set the export_path to your preferred destination, set compression parameters.

### Select No Material
Select all objects that don't have an assigned material.

### Selected Objects No Render
Disables the rendering of the selected objects. It's like pressing H, but it hides from the render instead of from the viewport.

### Selected Objects Pos
Export the coordinates and the material names of the selected objects. Useful for individually adding objects to a Three.js scene.

### Selected Objects Rename
Rename all the selected objects
