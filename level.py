# -*- coding: utf-8 -*-

import csv
from cell import Cell
from element import Element

class Level:
    """Class containing all the attributes for a level """

    def __init__(self, numLevel):
        self.numLevel = numLevel
        self._grilleCSV = list()
        self._elements = list()
        self._grille = list()

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
    def _get_grille(self):
        """Getters for grille : list of all the cell in the level"""
        return self._grille

    def _set_grille(self, listOfElementsInTheirCell):
        """Setter for grille : list of all the cell in the level"""
        self._grille = listOfElementsInTheirCell

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
        """Getters for the list of elements of the level"""
        return self._elements

    def _set_elements(self, elements):
        """Setters for the list of elements of the level"""
        self._elements = elements

    elements = property(_get_elements, _set_elements)
    grille = property(_get_grille, _set_grille)
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
                        elementSymbol = rowSplitted[0]
                        elementSkin = rowSplitted[1] #rowSplitted[1] is the path to get its skin
                        elementName = rowSplitted[2] #rowSplitted[2] is the name of the element
                        elementIsDangerous = rowSplitted[3]
                        elementToCreate = Element(elementName, elementSymbol, elementSkin, elementIsDangerous)
                        listElementObjects.append(elementToCreate)

        #Now we can set our list of elements that are in the level
        self._set_elements(listElementObjects)

    def fillTableWithElements(self):
        "We are going to fill the table with all the elements"

        listRow = list()
        listCell = list()
        i = 0
        j = 0

        #We read each line and cell of grille_csv and add the real class element
        #in a table (list of lists)
        for row in self._get_grille_csv():
            j = 0
            
            for cell in row:
                #We search which element is equal to the symbol in the current cell
                for element in self._get_elements():
                    if cell == element.symbol:
                        currentCell = Cell(i, j, element)
                        listCell.append(currentCell)
                    else:
                        listCell.append(None)
                j = j + 1
            i = i + 1

            listRow.append(listCell)

        #Now that our elements are in each case. We set the attributes : grille
        self._set_grille(listRow)
                        
                        
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
              
