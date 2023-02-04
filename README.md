# Sky130B cells GLTF 3D models

This repository contains GLTF 3D models of the Sky130B cells.

## How to use

The GLTF files are located in the `cells` folder. You can use them in your favorite GLTF viewer. For instance:

https://gds-viewer.tinytapeout.com/?model=https://tinytapeout.github.io/sky130B-cells-gltf/cells/sky130_fd_sc_hd__and2_1.gds.gltf

After loading the cell, press "3" to center the model, and zoom in to see the details.

## How to generate

Setup:

```
git submodule update --init
cd GDS2glTF
pip install -r requirements.txt
```

Then run:

```
python generate.py $PDK_ROOT/sky130B/libs.ref/sky130_fd_sc_hd/gds/sky130_fd_sc_hd.gds
```
