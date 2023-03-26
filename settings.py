"""Általános játék beállítások scriptje"""

import math


# Felbontás, FPS limiter

RES = WIDTH, HEIGHT = 1280, 720
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 60

# Játékos kezdő pozíció és szög, méret, gyorsaság, forgássi sebesség

PLAYER_POS = 8, 4.5
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.005
PLAYER_ROT_SPEED = 0.005
PLAYER_SIZE_SCALE = 60

# Egér beállítások, határok

MOUSE_SENSITIVITY = 0.0003
MOUSE_MAX_REL = 40
MOUSE_BORDER_LEFT, MOUSE_BORDER_TOP = 100, 100
MOUSE_BORDER_RIGHT = WIDTH - MOUSE_BORDER_LEFT
MOUSE_BORDER_BOTTOM = HEIGHT - MOUSE_BORDER_TOP

# FOV, sugarak, mélység

FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20

# Nézet és annak mérete

SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)
SCALE = WIDTH // NUM_RAYS

# Textúra méret

TEXTURE_SIZE = 256
HALF_TEXTURE_SIZE = TEXTURE_SIZE // 2
