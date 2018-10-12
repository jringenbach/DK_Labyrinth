# -*- coding : utf-8 -*-

import numpy
import pygame
from level import Level


level1 = Level(1)
level1._set_grille_csv()
level1.whichElementIsInTheLevel()
level1.fillTableWithElements()
