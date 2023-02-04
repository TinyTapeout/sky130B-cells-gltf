import sys
import gdspy
import os

TARGET_DIR = "cells"

# Load the GDS file
lib = gdspy.GdsLibrary()
with open(sys.argv[1], "rb") as f:
    lib.read_gds(f)

# Loop over all cells
for cell in lib.cells.values():
    cell_gds = os.path.join(TARGET_DIR, cell.name + ".gds")
    cell_lib = gdspy.GdsLibrary(precision=1e-9)
    cell_lib.add(cell)
    cell_lib.write_gds(cell_gds)
    os.system("python GDS2glTF/gds2gltf.py {}".format(cell_gds))
