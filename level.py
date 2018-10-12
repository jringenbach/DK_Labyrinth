# -*- coding: utf-8 -*-

class Level:
    """Class containing all the attributes for a level """

    def __init__(self, numLevel):
        self.numLevel = numLevel
        self._grilleCSV = ""

#------------------------------------------------------------------------
#                           GETTERS AND SETTERS
#------------------------------------------------------------------------

    def _get_grille_csv(self):
        """Getters for _grilleCSV """
        return self._grilleCSV

    def _set_grille_csv(self, grille):
        """Setters for _grilleCSV """
        #load grillecsv with the corresponding csv file
        pass

    grilleCSV = property(_get_grille_csv, _set_grille_csv)
        
