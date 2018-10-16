# -*- coding : utf-8 -*-

from classes.level import Level
import displayDK

def exitTitleScreen(playerAction):
    """Close the title screen or not"""

    if playerAction == "Nouvelle Partie":
        print("Le joueur a choisi de faire une nouvelle partie.")
        return 0

    elif playerAction == "Selection des niveaux":
        print("Le joueur va à la sélection des niveaux.")
        return 0

    elif playerAction == "Quit_the_game":
        print("Le joueur quitte le programme")
        return 0

    elif playerAction == "Touche au hasard":
        print("Le joueur a tapé sur une autre touche")
        return 1

    elif playerAction is None:
        print("Le joueur ne fait rien.")
        return 1

    else:
        return 1

def howManyLevels():
    """Calculate the number of level present in the game by counting the number
    of csv files that exist for those levels"""

    totalLevels = 0

    #We read each line and count how many there are in the file that contains
    #all the paths for the levels
    with open("resources/levelFiles.txt", "r") as listOfLevelPaths:
        for line in listOfLevelPaths:
            totalLevels = totalLevels + 1

    return totalLevels


