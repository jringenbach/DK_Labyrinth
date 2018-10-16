# -*- coding : utf-8 -*-

import displayDK
import pygame
import loading
from classes.level import Level

keep_playing = True
numLevel = 1
playerAction = ""
whatNext = ""

#Display main menu where you can select levels
pygame.init()
playerAction = displayDK.displayTitleScreen("resources/img/titleScreen_640_480.png")

#We look for what we have to load depending on the choice of the player
if playerAction == "Nouvelle Partie":

    #We load the first level
    while keep_playing:
        whatNext = displayDK.displayLevel(numLevel)

        if whatNext == "Next_level":
            print("The player goes to next level")
            numLevel = numLevel + 1
            
        elif whatNext == "Quit_the_game":
            print("The player quits the game")
            keep_playing = False
        

#We load the screen where the player can select a level
elif playerAction == "Selection des niveaux":
    displayDK.displayLevelSelection()

#We quit the program
else:
    pass


