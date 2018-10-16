# -*- coding : utf-8 -*-

#------------------------------------------------------------------------
#                               LIB IMPORT
#------------------------------------------------------------------------

import eventHandler
import os
import pygame
import loading
from pygame.locals import *
from classes.cell import Cell
from classes.scrolls import Scrolls
from classes.level import Level
from classes.player import Player

#------------------------------------------------------------------------
#                               GLOBAL VARIABLE
#------------------------------------------------------------------------

#Center the window of the game at the center of the computer screen
os.environ['SDL_VIDEO_CENTERED'] = '1'

#Window where the game is displayed
firstPixel = None
windowWidth = 640
windowHeight = 480
window = pygame.display.set_mode((windowWidth,windowHeight))
playerAction = None

#------------------------------------------------------------------------
#                               METHODS
#------------------------------------------------------------------------

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

    #Display the title screen as long as the player presses wrong key
    while continuer:
        for event in pygame.event.get():

            if event.type == KEYDOWN: 
                playerAction = eventHandler.eventTitleScreen(event)
                continuer = loading.exitTitleScreen(playerAction)
                
            elif event.type == QUIT:
                continuer = 0

            elif event.type == MOUSEBUTTONDOWN:
                continuer = 0


    return playerAction
    
def displayGrille(level, firstPixel):
    """We place all elements on the table"""

    print("firstPixel : "+str(firstPixel))
    for row in level._get_grille():
        for cell in row:
            if cell.element is not None:
                pos_x = firstPixel + (cell.pos_x * 30)
                pos_y = cell.pos_y * 30
                elementPNG = pygame.image.load(cell.element.skin).convert_alpha()
                window.blit(elementPNG, (pos_x, pos_y))

            else:
                pass

    
def displayLevel(numLevel):
    """Display the level the player has selected """
    print("Chargement du niveau "+str(numLevel))

    #String that will go back to main and let the program knows what to do next
    #Go to next level? Quit the game?
    action = ""
   
    #We create the object Level and load its elements
    level = Level(numLevel)
    level.loadingLevelForDisplay()

    #We calculate where should be the center of the game on the screen in order
    #to display correctly all elements
    gameWidth = len(level._get_grille()[0]) * 30
    firstPixel = centerTheGameOnTheScreen(window.get_width(), gameWidth)

    #We set a new background image
    window.fill(pygame.Color("black"))
    background = pygame.image.load("resources/img/fond.jpg").convert()
    window.blit(background, (firstPixel,0))
    pygame.display.flip()

    #We place each element with their pixels position on the screen
    displayGrille(level, firstPixel)

    #We place the player on the table
    player = Player()
    playerPNG = pygame.image.load(player.character.skin).convert_alpha()
    player.positionRect = playerPNG.get_rect(x = level.start[0], y = level.start[1])
    print("Position joueur : ["+str(player.positionRect.x)+","+str(player.positionRect.y)+"]")
    window.blit(playerPNG, (firstPixel+player.positionRect.x*30, player.positionRect.y*30))
    pygame.display.flip()
                
    continuer = 1

    #We display the level while the player hasn't finished it
    while continuer:
        for event in pygame.event.get():
            if event.type == QUIT:
                action = "Quit_the_game"
                continuer = 0

            #If the player press a key, we check if he can move
            elif event.type == KEYDOWN:
                #We reset the screen by filling it with black color
                window.fill(pygame.Color("black"))
                player.move(level, event)

                #We display background and elements of the level again
                window.blit(background, (firstPixel,0))
                displayGrille(level, firstPixel)
                playerPNG = pygame.image.load(player.character.skin).convert_alpha()
                window.blit(playerPNG, (firstPixel + player.positionRect.x * 30, player.positionRect.y*30))
                pygame.display.flip()

                #We do multiple checks at the end of the player turn to see if
                #he/she is on scroll, dies or wins.
                level.checkPlayerOnScroll(player, window)
                level.checkPlayerDies(player)
                if level.checkEndLevel(player):
                    continuer = 0
                    action = "Next_level"

    return action
           


def displayLevelSelection():
    """Screen where all the levels unlocked are listed """
    print("Level selection method")
    pass

def centerTheGameOnTheScreen(windowWidth, gameWidth):
    """Method that calculates where the first pixel of the width of the game
    has to be in order to have the game centered on the screen

    Attributes:
    :windowWidth: width of the window : int
    :gameWidth: width of the game : int    
    """
    print("window width : "+str(windowWidth))
    print("game width : "+str(gameWidth))
    blankSpace = windowWidth - gameWidth
    print("Blank Space : "+str(blankSpace))
    firstPixel = blankSpace / 2
    print("firstPixel : "+str(firstPixel))

    return firstPixel

    
