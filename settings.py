# IMPORTS
# -----------------------------------------------
from numba import njit

import numpy as np
import glm
import math


# WINDOW RESOLUTION
WIN_RES = glm.vec2(1600, 900)  # Set resolution to 1600x900

# COLORS
# -----------------------------------------------
# Background color
BG_COLOR = glm.vec3(0.1, 0.16, 0.25)