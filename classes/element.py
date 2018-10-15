# -*- coding: utf-8 -*-

class Element:
    """An element is a character, a pnj or a block

    Attributes:
    :name: name of the element (string)
    :symbol: symbol of the element in the csv file(string)
    :skin: path where the png need to be loaded to display the element (string)
    :isDangerous: boolean that indicates if this element is dangerous for the player
    :blockThePlayer: boolean that indicates if this element blocks the player when he/she tries to move
    """

    def __init__(self, name, symbol, skin, isDangerous, blockThePlayer):
        self.name = name
        self.symbol = symbol
        self.skin = skin
        self.isDangerous = isDangerous
        self.blockThePlayer = blockThePlayer
