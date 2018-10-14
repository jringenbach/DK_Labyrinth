# -*- coding: utf-8 -*-

class Element:
    """An element is a character, a pnj or a block """

    def __init__(self, name, symbol, skin, isDangerous, blockThePlayer):
        self.name = name
        self.symbol = symbol
        self.skin = skin
        self.isDangerous = isDangerous
        self.blockThePlayer = blockThePlayer
