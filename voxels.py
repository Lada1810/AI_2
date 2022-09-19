from concurrent.futures import process
import cv2
import trimesh
from trimesh.visual import texture, TextureVisuals
from trimesh import Trimesh
from PIL import Image
import numpy as np

# tex = TextureVisuals(image = img)

# print(uv)

mesh = trimesh.load("./Dog.obj", process = False)

voxelized_mesh = mesh.voxelized(0.01).hollow().as_boxes()

s = trimesh.Scene()
s.add_geometry(voxelized_mesh)
s.show()


