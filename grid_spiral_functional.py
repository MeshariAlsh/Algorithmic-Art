import pygame
import math
import time

pygame.init()

window = pygame.display.set_mode((1000,1000))
sizeWindow = pygame.display.get_window_size()
centerWindowPos = (sizeWindow[0] / 2 , sizeWindow[1] /2) # To get the coords for Head and Tail of the origin line

# Line information 
diffcolor = (255, 255, 0)
lineColour = (0, 0, 0)
Head = (centerWindowPos[0], centerWindowPos[1] - 100)
Tail = (centerWindowPos[0], centerWindowPos[1])
LINE_WIDTH = 5
NUM_OF_STEPS = 5 
NUM_OF_RENDERED_LINES = 20
myLines = []
storePointsfrom = []
SPIRAL_STEP_SIZE = 1.5

# Function uses derived formula from  L_1 metric unit sphere to find points in the 4th quadrant
def ComputeNewLineFourthQuadrant(distance, prevHead):

    midPoint = (distance/ 2)
    k = int(midPoint)
    endPoint = ( (prevHead[0] + k), (k + prevHead[1] - distance) )
    return endPoint

# Function uses derived formula from  L_1 metric unit sphere to find points in the 1st quadrant
def ComputeNewLineFirstQuadrant(distance, prevHead):
    print(f"Value of prevhead in FirstQuad: ______________{prevHead}")

    midPoint = (distance/ 2)
    k = int(midPoint)
    endPoint = ( (prevHead[0] + k), (prevHead[1] + distance - k ) )
    return endPoint

def ComputeNewLineThirdQuadrant(distance, prevHead):

    midPoint = (distance/ 2)
    k = int(midPoint)
    endPoint = ( (prevHead[0] - k), (k + prevHead[1] - distance) )
    return endPoint

# Function uses derived formula from  L_1 metric unit sphere to find points in the 1st quadrant
def ComputeNewLineSecondQuadrant(distance, prevHead):

    midPoint = (distance/ 2)
    k = int(midPoint)
    endPoint = ( (prevHead[0] - k), (prevHead[1] + distance - k ) )
    return endPoint

# Get the length of the phantom line.
def ModifySpiralStep(length, counter, positionOfSpiral):

    step_size = (length * SPIRAL_STEP_SIZE)
   
    return step_size

def GenerateNewLinesLeftDown( prevLineHead, prevLineTail, counter):

    # Identification string
    positionOfSpiral = "Left-Down Hand Side"

    print(f'{positionOfSpiral}: Begining points prevLineHead: {prevLineHead}. and prevLineTail {prevLineTail}-- \n')

                
    # To get the radius of the L_1 unit sphere respective to previous head 
    lenOfPhantomLine = (prevLineTail[1] - prevLineHead[1]) 
    Hypotenuse = ModifySpiralStep(lenOfPhantomLine, counter, positionOfSpiral) 
    radius = int(Hypotenuse)

    print(f'Left-Down Hand Side: Length of the radius in Manhattan Metric unit sphere {radius} Loop No {counter}. \n')

    # Counter is used as a switch to change the direction of the each line generated  
    if ( counter % 2 == 0):
        newLineHead = ComputeNewLineThirdQuadrant(radius, prevLineHead)
         
    else:
         newLineHead = ComputeNewLineFourthQuadrant(-radius, prevLineHead)
   
    print(f'Right-Down Hand Side: New point after function compute newline: {newLineHead} ____ The old points to be a tail now: {prevLineHead}. \n')

    return newLineHead


def GenerateNewLinesRightDown( prevLineHead, prevLineTail, counter):

    # Identification string
    positionOfSpiral = "Right-Down Hand Side"

    print(f'{positionOfSpiral}: Begining points prevLineHead: {prevLineHead}. and prevLineTail {prevLineTail}-- \n')

                
    # To get the radius of the L_1 unit sphere respective to previous head 
    lenOfPhantomLine = (prevLineTail[1] - prevLineHead[1]) 
    Hypotenuse = ModifySpiralStep(lenOfPhantomLine, counter, positionOfSpiral) 
    radius = int(Hypotenuse)

    print(f'Right-Down Hand Side: Length of the radius in Manhattan Metric unit sphere {radius} Loop No {counter}. \n')

    # Counter is used as a switch to change the direction of the each line generated  
    if ( counter % 2 == 0):
        newLineHead = ComputeNewLineThirdQuadrant(-radius, prevLineHead)
         
    else:
         newLineHead = ComputeNewLineFourthQuadrant(radius, prevLineHead)
   
    print(f'Right-Down Hand Side: New point after function compute newline: {newLineHead} ____ The old points to be a tail now: {prevLineHead}. \n')

    return newLineHead


# Left side spiral
def GenerateNewLinesLEFT( prevLineHead, prevLineTail, counter):

    # Identification string
    positionOfSpiral = "Left Hand Side"

    print(f'{positionOfSpiral}: Begining points prevLineHead: {prevLineHead}. and prevLineTail {prevLineTail}-- \n')

                
    # To get the radius of the L_1 unit sphere respective to previous head 
    lenOfPhantomLine = (prevLineTail[1] - prevLineHead[1]) 
    Hypotenuse = ModifySpiralStep(lenOfPhantomLine, counter, positionOfSpiral) 
    radius = int(Hypotenuse)

    print(f'Left Hand Side: Length of the radius in Manhattan Metric unit sphere {radius} Loop No {counter}. \n')

    # Counter is used as a switch to change the direction of the each line generated  
    if ( counter % 2 == 0):
        newLineHead = ComputeNewLineSecondQuadrant(radius, prevLineHead)
    else:
        newLineHead = ComputeNewLineThirdQuadrant(radius, prevLineHead)
        
    print(f'Right-Down Hand Side: New point after function compute newline: {newLineHead} ____ The old points to be a tail now: {prevLineHead}. \n')

    return newLineHead 

def GenerateNewLinesRIGHT( prevLineHead, prevLineTail, counter):

    # Identification string
    positionOfSpiral = "Right Hand Side"

    print(f'{positionOfSpiral}: Begining points prevLineHead: {prevLineHead}. and prevLineTail {prevLineTail}-- \n')

                
    # To get the radius of the L_1 unit sphere respective to previous head 
    lenOfPhantomLine = (prevLineTail[1] - prevLineHead[1]) 
    print(f'Right Hand Side: Length of the Phantomlin ------------------({lenOfPhantomLine}) . \n')

    #CalculateHypotenuse
    Hypotenuse = ModifySpiralStep(lenOfPhantomLine, counter, positionOfSpiral) 
    radius = int(Hypotenuse)

    print(f'Right Hand Side: Length of the radius in Manhattan Metric unit sphere {radius} Loop No {counter}. \n')

    # Counter is used as a switch to change the direction of the each line generated  
    if ( counter % 2 == 0):
        newLineHead = ComputeNewLineFourthQuadrant(radius, prevLineHead)
    else:
        newLineHead = ComputeNewLineFirstQuadrant(radius, prevLineHead)
   
    print(f'Right-Down Hand Side: New point after function compute newline: {newLineHead} ____ The old points to be a tail now: {prevLineHead}. \n')

    return newLineHead

def main():

    global Tail
    global Head

    # Generate Lines
    for lines in range(NUM_OF_STEPS):
        newLineHead = GenerateNewLinesRIGHT(Head , Tail, lines)
        myLines.append([newLineHead,Head])
        Tail = Head
        Head = newLineHead

    Head = (centerWindowPos[0], centerWindowPos[1] - 100)
    Tail = (centerWindowPos[0], centerWindowPos[1])
    
    for lines in range(NUM_OF_STEPS):
        newLineHead = GenerateNewLinesLEFT(Head , Tail, lines+1)
        myLines.append([newLineHead, Head])
        Tail = Head
        Head = newLineHead

    Head = (centerWindowPos[0], centerWindowPos[1] - 100)
    Tail = (centerWindowPos[0], centerWindowPos[1])
        
    for lines in range(NUM_OF_STEPS):
        newLineHead = GenerateNewLinesRightDown(Head , Tail, lines)
        myLines.append([newLineHead, Head])
        Tail = Head
        Head = newLineHead

    Head = (centerWindowPos[0], centerWindowPos[1] - 100)
    Tail = (centerWindowPos[0], centerWindowPos[1])
        
    for lines in range(NUM_OF_STEPS):
        newLineHead = GenerateNewLinesLeftDown(Head , Tail, lines+1)
        myLines.append([newLineHead, Head])
        Tail = Head
        Head = newLineHead

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
        
        window.fill((245, 245, 220))

        # Render Lines
        for lines in range(NUM_OF_RENDERED_LINES):
                 pygame.draw.line(window, lineColour,myLines[lines][0], myLines[lines][1] , LINE_WIDTH)
        
        pygame.display.flip()

    pygame.quit()


main()