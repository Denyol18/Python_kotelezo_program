"""Objektum kezelő szkriptje"""

import sprite as sp
import npc as n


class ObjectHandler:
    """Objektum kezelőt reprezentáló osztály"""

    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = 'resources/sprites/npc'
        self.static_sprites = 'resources/sprites/static_sprites'
        add_sprite = self.add_sprite
        add_npc = self.add_npc

        # Spriteok
        add_sprite(sp.Sprite(game))
        add_sprite(sp.Sprite(game, pos=(1.8, 1.8)))
        add_sprite(sp.Sprite(game, pos=(9.8, 5.5)))

        # NPCk
        add_npc(n.NPC(game))

    def update(self):
        """Objektum kezelőt frissítő függvény"""

        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]

    def add_npc(self, npc):
        """Függvény, ami a paraméterként kapott
        npct hozzáadja az npc_listhez"""

        self.npc_list.append(npc)

    def add_sprite(self, sprite):
        """Függvény, ami a paraméterként kapott
        spriteot hozzáadja a sprite_listhez"""

        self.sprite_list.append(sprite)
