# -*- coding : utf-8 -*-

from classes.element import Element
import pygame
from pygame.locals import *

class Player:
    """Contain all the information about the player """

    def __init__(self):
        self.character = Element("DK", "P", "resources/img/dk_bas.png", False, False)
        self.positionRect = ""

#------------------------------------------------------------------------
#                               METHODS
#------------------------------------------------------------------------


    def move(self, level, event):
        """We check if the player can move regarding of the key that has been
        pressed"""

        player_pos_x = self.positionRect.x
        player_pos_y = self.positionRect.y
        print(str(player_pos_x)+","+str(player_pos_y))
        nextCell = list()
     

        #If the player press "right"
        if event.key == K_RIGHT:
            nextCell = level._get_grille()[player_pos_y][player_pos_x+1]
            
            if nextCell is not None and nextCell.element.blockThePlayer == True:
                print("Le joueur est bloqué")
                

            else:
                print("Player goes right")
                self.positionRect = self.positionRect.move(1, 0)

        #If the player press "left"
        elif event.key == K_LEFT:
            nextCell = level._get_grille()[player_pos_y][player_pos_x-1]
            print("NextCell")
            print(nextCell)
            if nextCell is not None:
                print(nextCell.element.name)
                print(str(nextCell.element.blockThePlayer))
            if nextCell is not None and nextCell.element.blockThePlayer == True:
                print("Le joueur est bloqué")
                
            else:
                print("Player goes left")
                self.positionRect = self.positionRect.move(-1, 0)

        #If the player press "up"
        elif event.key == K_UP:
            nextCell = level._get_grille()[player_pos_y-1][player_pos_x]
            if nextCell is not None:
                print(nextCell)
            else:
                print("vide")

            if nextCell is not None and nextCell.element.blockThePlayer == True:
                print("Le joueur est bloqué")


            else:
                print("Player goes up")
                self.positionRect = self.positionRect.move(0, -1)

        #If the player press "down"
        elif event.key == K_DOWN:
            nextCell = level._get_grille()[player_pos_y+1][player_pos_x]
            if nextCell is not None:
                print(nextCell)
            else:
                print("vide")

            if nextCell is not None and nextCell.element.blockThePlayer == True:
                print("Le joueur est bloqué")

            else:
                print("Player goes down")
                self.positionRect = self.positionRect.move(0, 1)


            
