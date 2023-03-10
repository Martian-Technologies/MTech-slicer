from util.selector import *
from util.voxelizer import *
from util.exporter import *

from slicers.tower_slicer import *
from slicers.cartesian_additive import *

path = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Scrap Mechanic\\Data\\Importer\\"
filename = "Importer.json"

# gets the 3d file
selector = Selector()
mesh = selector.select_3d_file(file='3D_models/duck.stl')

# Voxelizes the 3d file
voxelizer = Voxelizer()
voxels, voxelPostions = voxelizer.fixVoxels(voxelizer.voxelize(mesh, 1))

# uses a slicer to slice/cam the 3d file
slicer = Cartesian('line', block=0, support=1)
voxels, newvVoxelPositions = slicer.slice(voxels, voxelPostions)
allInstructionsArrays = slicer.cam(voxels)

# exports the intructions to path, filename
exporter = Exporter()
exporter.startExport(allInstructionsArrays, path, filename)
