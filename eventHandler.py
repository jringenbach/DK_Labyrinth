# -*- coding : utf-8 -*-

import pygame
from pygame.locals import *

#------------------------------------------------------------------------
#                               METHODS
#------------------------------------------------------------------------

def eventTitleScreen(event):
    """Handle the key pressed by the player in the title screen.
    Also handle what happens with the mouse."""

    #If the player clicks or click on the red cross, it goes next
    if event.type == QUIT:
        playerChoice = "Quitter"

    #if the player press a key
    elif event.type == KEYDOWN:
        #The player choses to play a new game
        if event.key == K_1:
            playerChoice = "Nouvelle Partie"

        #The player wants to go to level selection
        elif event.key == K_2:
            playerChoice = "Selection des niveaux"

        #The player wants to quit the game
        elif event.key == K_3:
            playerChoice = "Quit_the_game"

        #The player presses anything
        else:
            playerChoice = "Touche au hasard"

    else:
        playerChoice = None

    return playerChoice
