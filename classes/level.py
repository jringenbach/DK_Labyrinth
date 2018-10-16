# -*- coding: utf-8 -*-

#------------------------------------------------------------------------
#                               IMPORT
#------------------------------------------------------------------------


import csv
import pygame
import boolean
from classes.element import Element
from classes.cell import Cell
from classes.scrolls import Scrolls
import displayDK

#------------------------------------------------------------------------
#                               CLASS
#------------------------------------------------------------------------


class Level:
    """Class containing all the attributes for a level

    Attributes:
    :numLevel: Number of the level (int)
    :_grilleCSV: a list that contains multiple lists containing cell of the game that were loaded from a csv in a string format
    :_elements: list of elements that we can find in the level
    :_grille: a list that contains multiple lists containing cell with element objects
    :_start: coordinates of the start element (where the player starts the level)
    :_end: coordinates of the end element
    :_spikes: list that contains all coordinates of the spikes in the level
    :_scrolls: list that contains all coordinates of the scrolls in the level
    :_keys: list that contains all coordinates of the keys in the level
    :_box: list that contains all coordinates of the boxes in the level
    :csvPath : path that link to the csv file containing the level (string)
    """

    def __init__(self, numLevel):
        self.numLevel = numLevel
        self._grilleCSV = list()
        self._elements = list()
        self._grille = list()
        self._start = (0,0)
        self._end = (14,14)
        self._spikes = list()
        self._scrolls = list()
        self._keys = list()
        self._boxes = list()
        self.csvPath = None

        #We search the corresponding csv file depending on the level
        with open("resources/levelFiles.txt", "r") as fileRead:
            i = 1
            for line in fileRead:
                if i == self.numLevel:
                    line = line.replace("\n","")
                    self.csvPath = line
                else:
                    pass
                
                i=i+1

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

    def _get_start(self):
        """Getters for start element which is a tuple of the coordinates """
        return self._start

    def _set_start(self, coordinates):
        """Setters for start element which is a tuple of the coordinates """
        self._start = coordinates

    def _get_end(self):
        """ Getters for the position of the end of the level"""
        return self._end

    def _set_end(self, coordinates):
        """Setters for the position of the end of the level """
        self._end = coordinates

    def _get_spikes(self):
        """ Getters for the list of spikes in the level"""
        return self._spikes

    def _set_spikes(self, listOfSpikes):
        """ Setters for the list of spikes in the level"""
        self._spikes = listOfSpikes

    def _get_scrolls(self):
        """ Getters for the list of scrolls in the level"""
        return self._scrolls

    def _set_scrolls(self, listOfScrolls):
        """ Setters for the list of scrolls in the level"""
        self._scrolls = listOfScrolls

    def _get_keys(self, listOfKeys):
        """Getters for the list of keys in the level"""
        return self._keys

    def _set_keys(self, listOfKeys):
        """Setters for the list of keys in the level """
        self._keys = listOfKeys

    def _get_boxes(self):
        """Getters for the list of boxes in the level"""
        return self._boxes

    def _set_boxes(self, listOfBoxes):
        """Setters for the list of Boxes in the level"""
        self._boxes = listOfBoxes

    elements = property(_get_elements, _set_elements)
    end = property(_get_end, _set_end)
    grille = property(_get_grille, _set_grille)
    grilleCSV = property(_get_grille_csv, _set_grille_csv)
    start = property(_get_start, _set_start)
    spikes = property(_get_spikes, _set_spikes)
    scrolls = property(_get_scrolls, _set_scrolls)
    keys = property(_get_keys, _set_keys)
    boxes = property(_get_boxes, _set_boxes)

#------------------------------------------------------------------------
#                               METHODS
#------------------------------------------------------------------------
    def checkEndLevel(self, player):
        """We check if the player has reached the end of the level """

        playerCoordinates = (player.positionRect.x, player.positionRect.y)

        #If the player coordinates match the end coordinates, he/she goes to
        #next level
        if playerCoordinates == self._get_end():
            #We return True because the player has finished the level
            return True

        else:
            #We return False
            return False
        

    def checkPlayerDies(self, player):
        """We check if the player has landed on a spike """

        listOfSpikesCoordinates = self._get_spikes()
        playerCoordinates = (player.positionRect.x, player.positionRect.y)

        if listOfSpikesCoordinates is not None:
            for spike in listOfSpikesCoordinates:
                if playerCoordinates == spike:
                    return True
                    

    def checkPlayerOnScroll(self, player, window):
        """We check if the player is on a scroll. If it is the case, we display
        the message

        attributes:
        :player: object of class Player that represents the player
        """

        player_x = player.positionRect.x
        player_y = player.positionRect.y
        cell = self._get_grille()[player_y][player_x]

        #If the player is indeed on a scroll, we display the message
        if cell.element is not None and cell.element.name == "scroll":
            cell.element.displayMessageOnWindow(window)
                    

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
                        elementBlocksThePlayer = boolean.strToBool(rowSplitted[4])
                        elementToCreate = Element(elementName, elementSymbol, elementSkin, elementIsDangerous, elementBlocksThePlayer)
                        listElementObjects.append(elementToCreate)

        #Now we can set our list of elements that are in the level
        self._set_elements(listElementObjects)

    def loadingLevelForDisplay(self):
        """Regroup all the methods that loads the elements of the level in self._grille """

        #We load all the elements and the table of the level selected       self._set_grille_csv()
        self._set_grille_csv()
        self.whichElementIsInTheLevel()
        self.fillTableWithElements()


    def fillTableWithElements(self):
        "We are going to fill the table with all the cell objects"

        listRow = list()
        i = 0
        j = 0

        #We read each line and cell of grille_csv and add the real class element
        #in a table (list of lists)
        for row in self._get_grille_csv():
            j = 0
            listCell = list()

            
            for cell in row:
                #We search which element is equal to the symbol in the current cell

                k = 0
                findSomething = False
                
                for element in self._get_elements():
                    if cell == element.symbol:
                        #If it is a scroll, we instanciate the scroll with its message
                        if cell == "P":
                            scroll = Scrolls("No message yet.")
                            scroll.loadScrollFromFile(j,i, self)
                            currentCell = Cell(j, i, scroll)
                            
                        else:
                            currentCell = Cell(j, i, element)

                        listCell.append(currentCell)
                        findSomething = True

                        #We set the coordinates of elements in level attributes : start, end, spikes, scrolls
                        self.setElementsCoordinates(cell, j, i)


                    #We need to get the number elements minus 1 to get a functional
                    #filling table method
                    nbElementsInTheLevel = len(self._get_elements())                        
                    if findSomething == False and k >= nbElementsInTheLevel - 1:
                        currentCell = Cell(j, i, None)
                        listCell.append(currentCell)
                    k = k + 1
                j = j + 1
            i = i + 1

            
            listRow.append(listCell)
            

        #Now that our elements are in each case. We set the attributes : grille, spikes, scrolls
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

    def printGrille(self):
        """Print the table with all the elements"""

        print("Length grille : "+str(len(self._get_grille())))
        for row in self._get_grille():
            print("(", end="")
            for cell in row:
                if cell is None:
                    print(" ,", end="")
                else:
                    print(cell.element.name+",", end="")
            print(")")

    def printGrilleCSV(self):
        """Print the csv table that we get from levelx.csv"""
        print("Length grillecsv : "+str(len(self._get_grille_csv())))
        for row in self._get_grille_csv():
            print("(", end="")
            for cell in row:
                if cell == "":
                    print(" ,", end="")
                else:
                    print(cell+",", end="")
            print(")")

    def setElementsCoordinates(self, symbol, x, y):
        """ Set the coordinates of the elements in start, end, spikes, scrolls"""
        #If it is the start element
        if symbol == "D":
            self._set_start((x,y))

        #If it is the end of the level element
        elif symbol == "F":
            self._set_end((x,y))

        #If it is a spike
        elif symbol == "S":
            self._get_spikes().append((x,y))
                            
        #If it is a scroll
        elif symbol == "P":
            self._get_scrolls().append((x,y))

        #If it is a key
        elif symbol == "K":
            self._get_keys().append((x,y))
        
              
