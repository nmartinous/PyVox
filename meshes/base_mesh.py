# IMPORTS
# -----------------------------------------------
import numpy as np


# Mesh class that all other meshes will inherit from
class BaseMesh:
    def __init__(self):
        # OpenGL context
        self.ctx = None
        # Shader program
        self.program = None
        # Vertex buffer data type format: "3f 3f"
        self.vbo_format = None
        # Attribute names according to format: ("in_position", "in_color")
        self.attrs: tuple[str, ...] = None
        # Vertex array object
        self.vao = None

    def get_vertex_data(self) -> np.array: ...

    def get_vao(self):
        vertex_data = self.get_vertex_data()
        vbo = self.ctx.buffer(vertex_data)
        vao = self.ctx.vertex_array(self.program, [(vbo, self.vbo_format, *self.attrs)], skip_errors=True)
        return vao

    def render(self):
        self.vao.render()
