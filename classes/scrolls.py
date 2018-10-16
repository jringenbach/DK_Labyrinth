# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
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

                #We set x and y with rowTurnedToList[.] minus 1 because in the csv
                #file, cell starts at 1 and not 0 like in a list
                scroll_level_read = int(rowTurnedToList[0])
                scroll_x_read = int(rowTurnedToList[1]) - 1
                scroll_y_read = int(rowTurnedToList[2]) - 1

                if scroll_x_read == x and scroll_y_read == y and scroll_level_read == level.numLevel:
                    self.message = rowTurnedToList[3]

    def displayMessageOnWindow(self, window):
        """Display the message that the scroll contains on the window where
        the game is being played

        Attributes:
        :self: Scroll object that inherits from Element
        :window: window where the game is displayed
        """

        messageFont = pygame.font.SysFont("comicsansms", 18)
        messageRender = messageFont.render(self.message, True, (255,255,255))
        window.blit(messageRender, (0,450))
        pygame.display.flip()
        

                
        
