# -*- coding: utf-8 -*-

class Cell:
    """Contains all attributes for a cell """

    def __init__(self, pos_x, pos_y, element):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.element = element

#------------------------------------------------------------------------
#                               METHODS
#------------------------------------------------------------------------


    def getInfo(self):
        """Give information about the cell in the terminal """
        print("["+str(self.pos_x)+","+str(self.pos_y)+" : "+self.element.name+"]")
