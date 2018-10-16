# -*- coding : utf-8 -*-

#------------------------------------------------------------------------
#                               IMPORT
#------------------------------------------------------------------------

import displayDK
import os
import pygame
import loading
from classes.level import Level

#------------------------------------------------------------------------
#                               VARIABLES
#------------------------------------------------------------------------

"""

:keep_playing: is True while the player is playing. If he clicks on the red cross, it will be False.
:numLevel: number of the current level : int
:playerAction: Choice of the player in the title screen : string
:whatNext: What will happen after the end of a level (end of displayDK.displayLevel) : string

"""

keep_playing = True
numLevel = 1
playerAction = ""
whatNext = ""
windowWidth = 640
windowHeight = 480
window = window = pygame.display.set_mode((windowWidth,windowHeight))


#------------------------------------------------------------------------
#                           CORE OF THE GAME
#------------------------------------------------------------------------

#Initialization of pygame
pygame.init()

#Center the window of the game at the center of the computer screen
os.environ['SDL_VIDEO_CENTERED'] = '1'

#Display main menu where you can select levels
playerAction = displayDK.displayTitleScreen("resources/img/titleScreen_640_480.png", window)

#We look for what we have to load depending on the choice of the player
if playerAction == "Nouvelle Partie":

    #We load the first level
    while keep_playing:
        whatNext = displayDK.displayLevel(numLevel, window)

        if whatNext == "Next_level":
            print("The player goes to next level")
            numLevel = numLevel + 1
            keep_playing = True
            
        elif whatNext == "Quit_the_game":
            print("The player quits the game")
            keep_playing = False
        

#We load the screen where the player can select a level
elif playerAction == "Selection des niveaux":
    displayDK.displayLevelSelection()

#We quit the program
else:
    pass


