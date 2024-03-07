# IMPORTS
# -----------------------------------------------
from settings import *


class ShaderProgram:

    def __init__(self, app):
        # Set a pointer to OpenGL context
        self.app = app
        self.ctx = app.ctx

        # ------------------ shaders ------------------ #
        self.quad = self.get_program(shader_name='quad')
        # -------------------------------------------- #

        self.set_uniforms_on_init()

    # Set uniforms
    def set_uniforms_on_init(self):
        pass

    # Update uniforms
    def update(self):
        pass

    # Method to load shaders using context manager
    def get_program(self, shader_name):
        with open(f'shaders/{shader_name}.vert') as file:
            vertex_shader = file.read()
        with open(f'shaders/{shader_name}.frag') as file:
            fragment_shader = file.read()

        # Return an instance of the shader program
        program = self.ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        return program
