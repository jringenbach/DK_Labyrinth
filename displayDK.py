# -*- coding : utf-8 -*-

#------------------------------------------------------------------------
#                               METHODS
#------------------------------------------------------------------------

import eventHandler
import pygame
import loading
from pygame.locals import *
from classes.level import Level
from classes.player import Player

window = pygame.display.set_mode((450,450))
playerAction = None

def displayTitleScreen(titleScreenImgPath):
    """Method where I configure how the title screen is displayed """

    #Setting the image for the title screen
    #window = pygame.display.set_mode((640,480))
    titleScreen = pygame.image.load(titleScreenImgPath).convert()
    window.blit(titleScreen, (0,0))

    #Setting the new game button for the title screen
    """newGame = pygame.image.load("resources/img/new_game_resized.png").convert()
    window.blit(newGame, (320, 240))"""
    pygame.display.flip()

    continuer = 1
    while continuer:
        for event in pygame.event.get():

            if event.type == KEYDOWN: 
                playerAction = eventHandler.eventTitleScreen(event)
                continuer = loading.exitTitleScreen(playerAction)
                
            elif event.type == QUIT:
                continuer = 0

            elif event.type == MOUSEBUTTONDOWN:
                continuer = 0

    #We look for what we have to load depending on the choice of the player
    loading.whatToLoadFromTitleScreen(playerAction)
        

def displayGrille(level):
    """We place all elements on the table"""
    for row in level._get_grille():
        for cell in row:
            if cell is not None:
                pos_x = cell.pos_x * 30
                pos_y = cell.pos_y * 30
                elementPNG = pygame.image.load(cell.element.skin).convert_alpha()
                window.blit(elementPNG, (pos_x, pos_y))

            else:
                pass

    
def displayLevel(numLevel):
    """Display the level the player has selected """
    print("Chargement du niveau "+str(numLevel))
    
    #We create the object Level and load its elements
    level = Level(numLevel)
    level.loadingLevelForDisplay()

    #We set a new background image
    background = pygame.image.load("resources/img/fond.jpg").convert()
    window.blit(background, (0,0))
    pygame.display.flip()

    #We place each element with their pixels position on the screen
    displayGrille(level)

    #We place the player on the table
    player = Player()
    playerPNG = pygame.image.load(player.character.skin).convert_alpha()
    player.positionRect = playerPNG.get_rect(x = level.start[0]*30, y = level.start[1] * 30)
    window.blit(playerPNG, player.positionRect)
    pygame.display.flip()
                
    continuer = 1

    while continuer:
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = 0

            #If the player press a key, we check if he can move
            elif event.type == KEYDOWN:
                player.move(level, event)
                window.blit(background, (0,0))
                displayGrille(level)
                playerPNG = pygame.image.load(player.character.skin).convert_alpha()
                window.blit(playerPNG, (player.positionRect.x * 30, player.positionRect.y*30))
                pygame.display.flip()
                level.checkEndLevel(player)
           


def displayLevelSelection():
    """Screen where all the levels unlocked are listed """
    print("Level selection method")
    pass

    
