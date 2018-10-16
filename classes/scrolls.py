# -*- coding: utf-8 -*-

from classes.element import Element

class Scrolls(Element):
    """Scrolls inherit from Element.
    This is an element that will have an additionnal attribute : message"""

    def __init__(self, message):
        Element.__init__(self, "scroll", "P", "resources/img/sprites/scroll_30_30.png", False, False)
        self.message = message

    def loadScrollFromFile(self, x, y, level):
        """Find the scroll to load in the csv file that contains all the scrolls

        Attributes:
        :x: coordinates x of the scroll we are looking for
        :y: coordinates y of the scroll we are looking for
        :level: level of the scroll we are looking for
        """

        #csv where all the scrolls are
        scrollTXTPath = "resources/scrolls.txt"

        with open("resources/scrolls.txt", "r") as fileRead:
            for row in fileRead:
                rowTurnedToList = row.split(":")
                print("rowTurnedToList")
                print(rowTurnedToList)
                scroll_level_read = int(rowTurnedToList[0])
                scroll_x_read = int(rowTurnedToList[1]) - 1
                scroll_y_read = int(rowTurnedToList[2]) - 1
                print("test en x : "+str(scroll_x_read == x))
                print("x player : "+str(x))
                print("test en y : "+str(scroll_y_read == y))
                print("y player : "+str(y))
                print("test level : "+str(scroll_level_read == level.numLevel))

                if scroll_x_read == x and scroll_y_read == y and scroll_level_read == level.numLevel:
                    self.message = rowTurnedToList[3]

                
        
