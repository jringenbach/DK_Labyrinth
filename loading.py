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

    elif playerAction == "Quitter":
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


