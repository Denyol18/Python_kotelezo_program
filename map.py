"""
Jatekter beallitasok
"""

import pygame as pg

_ = False

mini_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 1, 1, 1, _, _, _, _, _, 1, 1, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, 1, _, _, 1],
    [1, _, _, 1, _, 1, _, _, _, _, 1, _, _, _, _, 1],
    [1, _, _, 1, _, 1, _, _, _, _, 1, 1, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, 1, 1, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()

    def get_map(self):
        for i, row in enumerate(self.mini_map):
            for j, value in enumerate(row):
                if value:
                    self.world_map[(j, i)] = value

    def draw(self):
        [pg.draw.rect(self.game.screen, 'green', (pos[0] * 50, pos[1] * 50, 50, 50), 2)
         for pos in self.world_map]
