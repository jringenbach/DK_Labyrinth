# -*- coding : utf-8 -*-

#------------------------------------------------------------------------
#                               LIB IMPORT
#------------------------------------------------------------------------

import eventHandler
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

"""

:firstPixel: the first pixel of the width where the game (and not the screen) has to be displayed
:playerAction: action that the player chooses in the titleScreen : string

"""

#Window where the game is displayed
firstPixel = None
playerAction = None

#------------------------------------------------------------------------
#                               METHODS
#------------------------------------------------------------------------

def displayTitleScreen(titleScreenImgPath, window):
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
    
def displayGrille(level, firstPixel, window):
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

    
def displayLevel(numLevel, window):
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
    displayGrille(level, firstPixel, window)

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

        #We display background and elements of the level again
        window.fill(pygame.Color("Black"))

        #We load the background image
        window.blit(background, (firstPixel,0))

        #We load the table of elements with their graphics
        displayGrille(level, firstPixel, window)

        #We load the player character (donkey kong)
        playerPNG = pygame.image.load(player.character.skin).convert_alpha()
        window.blit(playerPNG, (firstPixel + player.positionRect.x * 30, player.positionRect.y*30))

        #If the player walked on a scroll, we display its message
        level.checkPlayerOnScroll(player, window)

        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                action = "Quit_the_game"
                continuer = 0

            #If the player press a key, we check if he can move
            elif event.type == KEYDOWN:

                #We reset the screen by filling it with black color

                player.move(level, event)
                print("x : "+str(player.positionRect.x))
                print("y : "+str(player.positionRect.y))

                #If the player dies, he goes back to the starting point of the current level
                level.checkPlayerDies(player)
                   
                #If player walks on the finish line, he goes to next level
                if level.checkEndLevel(player):
                    continuer = 0
                    action = "Next_level"

    return action
           


def displayLevelSelection():
    """Screen where all the levels unlocked are listed """
    numberOfLevels = loading.howManyLevels()

    for x in range(0, numberOfLevels):
        messageFont = pygame.font.SysFont("comicsansms", 18)
        messageRender = messageFont.render(self.message, True, (255,255,255))
        window.blit(messageRender, (0,450))
        pygame.display.flip()
    

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

    
