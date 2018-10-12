# -*- coding : utf-8 -*-

import numpy
import pygame
from level import Level
import displayDK

#Display main menu where you can select levels
displayDK.displayTitleScreen("resources/img/titleScreen_resized.png")

#Load the level depending on the choice of the player

level1 = Level(1)
level1._set_grille_csv()
level1.whichElementIsInTheLevel()
level1.fillTableWithElements()
