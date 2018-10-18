# -*- coding : utf-8 -*-

from classes.element import Element
import pygame
from pygame.locals import *

#------------------------------------------------------------------------
#                               CLASS
#------------------------------------------------------------------------

class Box(Element):
    """Box inherits from Element
    Box have methods that calculate if they can move or not"""

    def __init__(self):
        Element.__init__(self, "box", "B", "resources/img/sprites/box_30_30.png", False, False)

#------------------------------------------------------------------------
#                               METHODS
#------------------------------------------------------------------------

    def canMove(self, player, level, event):
        """Calculate if the box can move on the next cell according to
        the move of the player

        Attributes:
        :player: class Player
        :level: class Level - The actual level that is being played
        :event: class pygame.event - contains which key the player press
        """
        player_x = player.positionRect.x
        player_y = player.positionRect.y
        x = 0
        y = 0
        box_x = 0
        box_y = 0

        #If the player goes left
        if event.key == K_LEFT:
            x = player_x - 2
            y = player_y
            box_x = player_x - 1
            box_y = player_y

        #If the player goes right
        elif event.key == K_RIGHT:
            x = player_x + 2
            y = player_y
            box_x = player_x + 1
            box_y = player_y

        #If the player goes up
        elif event.key == K_UP:
            x = player_x
            y = player_y - 2
            box_x = player_x
            box_y = player_y - 1

        #If the player goes down
        elif event.key == K_DOWN:
            x = player_x
            y = player_y + 2
            box_x = player_x
            box_y = player_y + 1
            
        else:
            pass

        #boxCanMove equals true if it can move, false otherwise
        boxCanMove = level.cellIsEmpty(x, y)

        #If the box can move. We move the box on the correct cell on the table
        if boxCanMove:
            level.grille[y][x].element = level._get_grille()[box_y][box_x].element
            #And we empty the cell where the box was
            level._get_grille()[box_y][box_x].element = None
            return True

        #If the box can't move, we canceled the player movement
        else:
            return False
            
            
