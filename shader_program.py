# IMPORTS
# -----------------------------------------------
from settings import *


class ShaderProgram:

    def __init__(self, app):
        # Set a pointer to OpenGL context
        self.app = app
        self.ctx = app.ctx

        self.player = app.player

        # ------------------ shaders ------------------ #
        self.quad = self.get_program(shader_name='quad')
        # -------------------------------------------- #

        self.set_uniforms_on_init()

    # Set uniforms
    def set_uniforms_on_init(self):
        self.quad['m_proj'].write(self.player.m_proj)
        self.quad['m_model'].write(glm.mat4())

    # Update uniforms
    def update(self):
        self.quad['m_view'].write(self.player.m_view)

    # Method to load shaders using context manager
    def get_program(self, shader_name):
        with open(f'shaders/{shader_name}.vert') as file:
            vertex_shader = file.read()
        with open(f'shaders/{shader_name}.frag') as file:
            fragment_shader = file.read()

        # Return an instance of the shader program
        program = self.ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        return program
