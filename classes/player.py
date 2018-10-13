# -*- coding : utf-8 -*-

from classes.element import Element

class Player:
    """Contain all the information about the player """

    def __init__(self, x, y):
        self.character = Element("DK", "P", "resources/img/dk_bas.png", False)
        self.pos_x = x
        self.pos_y = y
