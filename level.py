# -*- coding: utf-8 -*-

import csv

class Level:
    """Class containing all the attributes for a level """

    def __init__(self, numLevel):
        self.numLevel = numLevel
        self._grilleCSV = list()

        #We search the corresponding csv file depending on the level
        with open("resources/levelFiles.txt", "r") as fileRead:
            i = 1
            for line in fileRead:
                if i == self.numLevel:
                    self.csvPath = line
                else:
                    i = i + 1

#------------------------------------------------------------------------
#                           GETTERS AND SETTERS
#------------------------------------------------------------------------

    def _get_grille_csv(self):
        """Getters for _grilleCSV """
        return self._grilleCSV

    def _set_grille_csv(self):
        """Setters for _grilleCSV
        We read the csv file and copy it into _grilleCSV"""
        with open(self.csvPath, "r") as csvFile:
            fileRead = csv.reader(csvFile, delimiter=",")
            for row in fileRead:
                self._grilleCSV.append(row)
        

    grilleCSV = property(_get_grille_csv, _set_grille_csv)

#------------------------------------------------------------------------
#                               METHODS
#------------------------------------------------------------------------

        def whichElementIsInTheLevel(self):
            """We search in _grilleCSV which element is present in the level.
            And we return a list of those elements."""
            for row in self._get_grille_csv():
                print(row)
                
