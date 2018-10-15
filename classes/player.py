# -*- coding : utf-8 -*-

from classes.element import Element
import pygame
from pygame.locals import *

class Player:
    """Contain all the information about the player """

    def __init__(self):
        self.character = Element("DK", "P", "resources/img/sprites/dk_down.png", False, False)
        self.positionRect = ""

#------------------------------------------------------------------------
#                               METHODS
#------------------------------------------------------------------------


    def move(self, level, event):
        """We check if the player can move regarding of the key that has been
        pressed. If he will pass through a wall, we stop the player from doing
        that."""

        player_pos_x = self.positionRect.x
        player_pos_y = self.positionRect.y
        nextCell = list()
        
        #If the player press "right"
        if event.key == K_RIGHT and player_pos_x < 14:
            nextCell = level._get_grille()[player_pos_y][player_pos_x+1]
            self.character.skin = "resources/img/sprites/dk_right.png"

            if nextCell is not None and nextCell.element.blockThePlayer == True:
                print("Le joueur est bloqué")
                
            else:
                print("Player goes right")
                self.positionRect = self.positionRect.move(1, 0)

        #If the player press "left"
        elif event.key == K_LEFT and player_pos_x > 0:
            nextCell = level._get_grille()[player_pos_y][player_pos_x-1]
            self.character.skin = "resources/img/sprites/dk_left.png"

            if nextCell is not None and nextCell.element.blockThePlayer == True:
                print("Le joueur est bloqué")
                
            else:
                print("Player goes left")
                self.positionRect = self.positionRect.move(-1, 0)

        #If the player press "up"
        elif event.key == K_UP and player_pos_y > 0:
            nextCell = level._get_grille()[player_pos_y-1][player_pos_x]
            self.character.skin = "resources/img/sprites/dk_up.png"

            if nextCell is not None and nextCell.element.blockThePlayer == True:
                print("Le joueur est bloqué")


            else:
                print("Player goes up")
                self.positionRect = self.positionRect.move(0, -1)

        #If the player press "down"
        elif event.key == K_DOWN and player_pos_y < 14:
            nextCell = level._get_grille()[player_pos_y+1][player_pos_x]
            self.character.skin = "resources/img/sprites/dk_down.png"

            if nextCell is not None and nextCell.element.blockThePlayer == True:
                print("Le joueur est bloqué")

            else:
                print("Player goes down")
                self.positionRect = self.positionRect.move(0, 1)

        #If he presses anything else. Nothing happens.
        else:
            pass


            
