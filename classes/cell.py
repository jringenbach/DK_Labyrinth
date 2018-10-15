# -*- coding: utf-8 -*-

class Cell:
    """Contains all attributes for a cell

    Attributes:
    :pos_x: position of the cell on the x axis (int)
    :pos_y: position of the cell on the y axis (int)
    :element: element that is in the cell (class Element)
    """

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
