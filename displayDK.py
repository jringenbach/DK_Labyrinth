# -*- coding : utf-8 -*-

#------------------------------------------------------------------------
#                               METHODS
#------------------------------------------------------------------------

import eventHandler
import pygame
import loading
from pygame.locals import *
from classes.level import Level

def displayTitleScreen(titleScreenImgPath):
    """Method where I configure how the title screen is displayed """

    #Setting the image for the title screen
    window = pygame.display.set_mode((640,480))
    titleScreen = pygame.image.load(titleScreenImgPath).convert()
    window.blit(titleScreen, (0,0))

    #Setting the new game button for the title screen
    newGame = pygame.image.load("resources/img/new_game_resized.png").convert()
    window.blit(newGame, (320, 240))
    pygame.display.flip()

    continuer = 1
    while continuer:
        for event in pygame.event.get():
            print("Continuer : "+str(continuer))
            if event.type == KEYDOWN: 
                print("Une touche a été pressée")
                playerAction = eventHandler.eventTitleScreen(event)
                continuer = loading.exitTitleScreen(playerAction)
                
            elif event.type == QUIT:
                continuer = 0

            elif event.type == MOUSEBUTTONDOWN:
                continuer = 0

    loading.whatToLoadFromTitleScreen(playerAction)
        

            

    
def displayLevel(numLevel):
    """Display the level the player has selected """
    print("Chargement du niveau 1")
    
    #We create the object Level and load its elements
    level = Level(numLevel)
    level.loadingLevelForDisplay()

def displayLevelSelection():
    """Screen where all the levels unlocked are listed """
    print("Level selection method")
    pass

    
