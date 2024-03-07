# IMPORTS
# -----------------------------------------------
from settings import *
from meshes.quad_mesh import QuadMesh


class Scene:

    def __init__(self, app):
        self.app = app
        # Create instance of quad mesh
        self.quad = QuadMesh(self.app)

    def update(self):
        pass

    def render(self):
        self.quad.render()
