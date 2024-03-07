# IMPORTS
# -----------------------------------------------
from settings import *
from shader_program import ShaderProgram
from scene import Scene

import moderngl as mgl
import pygame as pg
import sys


# Application class that:
#   - Runs main application loop
#   - Updates objects42
#   - Renders objects
#   - Handles events
class VoxelEngine:

    def __init__(self):
        # Initialize pygame submodules
        pg.init()

        # Set OpenGL attributes
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)  # OpenGL 3.x
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)  # OpemGL x.3
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)  # Prohibit deprecated funcs
        pg.display.gl_set_attribute(pg.GL_DEPTH_SIZE, 24)  # Set depth buffer to 24 bits

        # Set resolution
        pg.display.set_mode(WIN_RES, flags=pg.OPENGL | pg.DOUBLEBUF)

        # Create OpenGL Context
        self.ctx = mgl.create_context()

        # Enable fragment depth testing, culling of invisible faces, color blending
        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE | mgl.BLEND)

        # Enable automatic garbage collection of unused OpenGL objects
        self.ctx.gc_mode = 'auto'

        # Clock objects and variables
        self.clock = pg.time.Clock()
        self.delta_time = 0
        self.time = 0

        # Flag to check if application is running
        self.is_running = True

        # Run on init method
        self.on_init()

    # Runs on initialization of application
    def on_init(self):
        # Create instance of shader program
        self.shader_program = ShaderProgram(self)
        self.scene = Scene(self)

    # Update object states
    def update(self):
        # Update shader program
        self.shader_program.update()
        self.scene.update()

        # Update the clock variables each tick
        self.delta_time = self.clock.tick()
        self.time = pg.time.get_ticks() * 0.001

        # FPS performance monitor in window title
        pg.display.set_caption(f'{self.clock.get_fps() :.0f}')

    # Render objects
    def render(self):
        # Clear frame a depth buffers
        self.ctx.clear(color=BG_COLOR)
        self.scene.render()
        # Display new frame
        pg.display.flip()

    # Handle events
    def handle_events(self):
        # Iterate over events
        for event in pg.event.get():
            # If the window is closed or the escape key is pressed:
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                # Set running flag to false
                self.is_running = False

    # Run main application loop
    def run(self):
        # While the application is running:
        while self.is_running:
            # Call running methods
            self.handle_events()
            self.update()
            self.render()
        # If the application is not running: close it
        pg.quit()
        sys.exit()


# Run on start
if __name__ == '__main__':
    # Create and run the engine
    app = VoxelEngine()
    app.run()
