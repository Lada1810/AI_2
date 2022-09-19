from concurrent.futures import process
import cv2
import trimesh
from trimesh.visual import texture, TextureVisuals
from trimesh import Trimesh
from PIL import Image
import numpy as np

img = Image.open("Dog.jpg")

tex = TextureVisuals(image = img)


with open("Dog.obj", 'r') as f:
    mesh_uv = trimesh.exchange.obj.load_obj(f)




uv = mesh_uv['visual'].uv
# print(uv)

mesh = trimesh.load("./Dog.obj", process = False)

material = trimesh.visual.texture.SimpleMaterial(image=img)

color_visuals = trimesh.visual.TextureVisuals(uv=uv, image=img, material=material)
mesh=trimesh.Trimesh(vertices=mesh.vertices, faces=mesh.faces, visual=color_visuals, validate=True, process=False)
mesh.show()
