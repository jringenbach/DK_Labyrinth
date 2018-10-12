# -*- coding : utf-8 -*-

#------------------------------------------------------------------------
#                               METHODS
#------------------------------------------------------------------------

import pygame
from pygame.locals import *

def displayTitleScreen(titleScreenImgPath):
    """Method where I configure how the title screen is displayed """
    window = pygame.display.set_mode((640,480))
    titleScreen = pygame.image.load(titleScreenImgPath).convert()
    print(titleScreenImgPath)
    window.blit(titleScreen, (0,0))
    pygame.display.flip()

    continuer = 1
    while continuer:
        for event in pygame.event.get():
            #If the player clicks or click on the red cross, it goes next
            if event.type == MOUSEBUTTONDOWN or event.type == QUIT:
                continuer = 0

    
    
