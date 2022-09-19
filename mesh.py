from concurrent.futures import process
import cv2
import trimesh
from trimesh.visual import texture, TextureVisuals
from trimesh import Trimesh
from PIL import Image
import numpy as np

img = Image.open("Dog.jpg")

mesh = trimesh.load("./Dog.obj", process = False)

cloud_of_points = trimesh.points.PointCloud(mesh.vertices, colors= (0,0,0,255))
s = trimesh.Scene()
s.add_geometry(cloud_of_points)
s.show()