# -*- coding: utf-8 -*-

class Element:
    """An element is a character, a pnj or a block """

    def __init__(self, skin, isDangerous):
        self.skin = skin
        self.isDangerous = isDangerous
