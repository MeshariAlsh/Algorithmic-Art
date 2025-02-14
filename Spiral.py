
from Util import Util  
import pygame

NUM_OF_LINES = 5 
LINE_WIDTH = 5
NUM_OF_LINES = 5 
NUM_OF_RENDERED_LINES = 5
lineColour = (0, 0, 0)

class Spiral:

    def __init__(self, head, tail):
        self._head = head
        self._tail = tail
        self.lines = []

    @property
    def head(self):
         return self._head
    
    @property
    def tail(self):
         return self._tail
    
    @head.setter
    def head(self, newHead):
         self._head = newHead

    @tail.setter
    def tail(self, newTail):
        self._tail = newTail

    def GenerateNewLinesLeftDown( self, prevLineHead, prevLineTail, counter):

        # Identification string
        positionOfSpiral = "Left-Down Hand Side"
                
        # To get the radius of the L_1 unit sphere respective to previous head 
        lenOfPhantomLine = (prevLineTail[1] - prevLineHead[1]) 
        Hypotenuse = Util.CalculateHypotenuse(lenOfPhantomLine, counter, positionOfSpiral) 
        radius = int(Hypotenuse)

        print(f'Left-Down Hand Side: Length of the radius in Manhattan Metric unit sphere {radius} Loop No {counter}. \n')

        # Counter is used as a switch to change the direction of the each line generated  
        if ( counter % 2 == 0):
            newLineHead = Util.ComputeNewLineThirdQuadrant(radius, prevLineHead)
         
        else:
            newLineHead = Util.ComputeNewLineFourthQuadrant(-radius, prevLineHead)
   
        print(f'Left-Down Side: New point after function compute newline: {newLineHead} Loop No {counter}. \n')

        return newLineHead


    def GenerateNewLinesRightDown( self, prevLineHead, prevLineTail, counter):

        # Identification string
        positionOfSpiral = "Right-Down Hand Side"
                
        # To get the radius of the L_1 unit sphere respective to previous head 
        lenOfPhantomLine = (prevLineTail[1] - prevLineHead[1]) 
        Hypotenuse = Util.CalculateHypotenuse(lenOfPhantomLine, counter, positionOfSpiral) 
        radius = int(Hypotenuse)

        print(f'Right-Down Hand Side: Length of the radius in Manhattan Metric unit sphere {radius} Loop No {counter}. \n')

        # Counter is used as a switch to change the direction of the each line generated  
        if ( counter % 2 == 0):
            newLineHead = Util.ComputeNewLineThirdQuadrant(-radius, prevLineHead)
         
        else:
            newLineHead = Util.ComputeNewLineFourthQuadrant(radius, prevLineHead)
   
        print(f'Right-Down Hand Side: New point after function compute newline: {newLineHead} Loop No {counter}. \n')

        return newLineHead


    # Left side spiral
    def GenerateNewLinesLEFT( self, prevLineHead, prevLineTail, counter):

        # Identification string
        positionOfSpiral = "Left Hand Side"
                
        # To get the radius of the L_1 unit sphere respective to previous head 
        lenOfPhantomLine = (prevLineTail[1] - prevLineHead[1]) 
        Hypotenuse = Util.CalculateHypotenuse(lenOfPhantomLine, counter, positionOfSpiral) 
        radius = int(Hypotenuse)

        print(f'Left Hand Side: Length of the radius in Manhattan Metric unit sphere {radius} Loop No {counter}. \n')

        # Counter is used as a switch to change the direction of the each line generated  
        if ( counter % 2 == 0):
            newLineHead = Util.ComputeNewLineSecondQuadrant(radius, prevLineHead)
        else:
            newLineHead = Util.ComputeNewLineThirdQuadrant(radius, prevLineHead)
        
        print(f'Left Hand Side: New point after function compute newline: {newLineHead} Loop No {counter}. \n')

        return newLineHead 

         
    def GenerateNewLinesRIGHT(self, prevHead, prevTail, counter):

        print(f"prevTail: {prevTail}, type: {type(prevTail)}")
        print(f"prevHead: {prevHead}, type: {type(prevHead)}")


        # Identification string
        positionOfSpiral = "Right Hand Side"
                
        # To get the radius of the L_1 unit sphere respective to previous head 
        lenOfPhantomLine = (prevTail[1] - prevHead[1]) 
        Hypotenuse = Util.CalculateHypotenuse(lenOfPhantomLine, counter, positionOfSpiral) 
        radius = int(Hypotenuse)

        #print(f'Right Hand Side: Value of y  {prevTail[1]} Loop No {counter}. \n')

        # Counter is used as a switch to change the direction of the each line generated  
        if ( counter % 2 == 0):
            newLineHead = Util.ComputeNewLineFourthQuadrant(radius, prevHead)
        else:
            newLineHead = Util.ComputeNewLineFirstQuadrant(radius, prevHead)
   
        #print(f'Right Hand Side: New point after function compute newline: {newLineHead} Loop No {counter}. \n')

        return newLineHead

    def GenerateSpiralPattern(self, spiralPattern):

        if spiralPattern == 0:

            for i in range(NUM_OF_LINES):
                newLineHead = self.GenerateNewLinesRIGHT(self._head , self._tail, i)
                self.lines.append([newLineHead, self._head])
                self._tail = self._head
                self._head = newLineHead 
                
        elif spiralPattern == 1:
             
             for i in range(NUM_OF_LINES):
                newLineHead = self.GenerateNewLinesLEFT(self._head , self._tail, i)
                self.lines.append([newLineHead, self._head])
                self._tail = self._head
                self._head = newLineHead 

        elif spiralPattern == 2:
             
             for i in range(NUM_OF_LINES):
                newLineHead = self.GenerateNewLinesRightDown(self._head , self._tail, i)
                self.lines.append([newLineHead, self._head])
                self._tail = self._head
                self._head = newLineHead 
                
        elif spiralPattern == 3:
              
              for i in range(NUM_OF_LINES):
                newLineHead = self.GenerateNewLinesLeftDown(self._head , self._tail, i)
                self.lines.append([newLineHead, self._head])
                self._tail = self._head
                self._head = newLineHead 

    #For debugging        
    def drawLines(self, window):
      
      for line in range(NUM_OF_RENDERED_LINES):
                 pygame.draw.line(window, lineColour,self.lines[line][0], self.lines[line][1] , LINE_WIDTH)

    
        
