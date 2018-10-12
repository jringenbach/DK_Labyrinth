# -*- coding: utf-8 -*-

import csv
from element import Element

class Level:
    """Class containing all the attributes for a level """

    def __init__(self, numLevel):
        self.numLevel = numLevel
        self._grilleCSV = list()
        self._elements = list()

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

            #We read each row of the csv file
            for row in fileRead:
                rowSplitted = row[0].split(";")
                self._grilleCSV.append(rowSplitted)

    def _get_elements(self):
        return self._elements

    def _set_elements(self, elements):
        self._elements = elements

        
    elements = property(_get_elements, _set_elements)
    grilleCSV = property(_get_grille_csv, _set_grille_csv)

#------------------------------------------------------------------------
#                               METHODS
#------------------------------------------------------------------------

    def loadingLevelElements(self, listElements):
        """We create a list of element objects depending on which
        element is in the level"""

        listElementObjects = list()

        #We gonna check for each element their matching properties in elementsFiles
        for element in listElements:
            with open("resources/elementsFiles.txt", "r") as elementFile:
                for row in elementFile:
                    rowSplitted = row.split(":")

                    if rowSplitted[0] == element: #rowSplitted[0] is the symbol of the element
                        elementSkin = rowSplitted[1] #rowSplitted[1] is the path to get its skin
                        elementName = rowSplitted[2] #rowSplitted[2] is the name of the element
                        elementToCreate = Element(elementSkin, elementName)
                        listElementObjects.append(elementToCreate)

        self._set_elements(listElementObjects)
                        
                        
    def whichElementIsInTheLevel(self):
        """We search in _grilleCSV which element is present in the level.
        And we return a list of those elements."""

        listElements = list()

        #We read each line
        for row in self._get_grille_csv():
            #We read each cell of each line
            for cell in row:
                if cell in listElements or cell == "":
                    pass
                
                else:
                    listElements.append(cell)

        self.loadingLevelElements(listElements)

                
