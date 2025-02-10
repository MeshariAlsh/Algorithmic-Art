import pygame
import math
import time

pygame.init()

window = pygame.display.set_mode((1000,1000))
sizeWindow = pygame.display.get_window_size()
centerWindowPos = (sizeWindow[0] / 2 , sizeWindow[1] /2) # To get the coords for Head and Tail of the origin line

# Line information 
diffcolor = (255, 255, 0)
lineColour = (255, 0, 0)
Head = (centerWindowPos[0], centerWindowPos[1] - 100)
Tail = (centerWindowPos[0], centerWindowPos[1])
LINE_WIDTH = 5
NUM_OF_LINES = 5 
NUM_OF_L = 20
myLines = []
storePointsfrom = []

# Second Line information 
HeadTwo = (centerWindowPos[0], centerWindowPos[1] - 100)
TailTwo = (centerWindowPos[0], centerWindowPos[1])

# Third Line information 
HeadThree = (centerWindowPos[0], centerWindowPos[1] - 100)
TailThree = (centerWindowPos[0], centerWindowPos[1])

# Four Line information 
HeadFour = (centerWindowPos[0], centerWindowPos[1] - 100)
TailFour = (centerWindowPos[0], centerWindowPos[1])

# Function uses derived formula from  L_1 metric unit sphere to find points in the 4th quadrant
def ComputeNewLineFourthQuadrant(distance, prevHead):

    midPoint = (distance/ 2)
    k = int(midPoint)
    endPoint = ( (prevHead[0] + k), (k + prevHead[1] - distance) )
    return endPoint

# Function uses derived formula from  L_1 metric unit sphere to find points in the 1st quadrant
def ComputeNewLineFirstQuadrant(distance, prevHead):

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
def CalculateHypotenuse(Oppistite, counter, positionOfSpiral):
   
    Hypotenuse = (Oppistite / math.sin(math.radians(45)))
    print(f'{positionOfSpiral}: Value of Hypotenuse: {Hypotenuse} | Loop No. {counter}\n')
    return Hypotenuse

def GenerateNewLinesLeftDown( prevLineHead, prevLineTail, counter):

    # Identification string
    positionOfSpiral = "Left-Down Hand Side"
                
    # To get the radius of the L_1 unit sphere respective to previous head 
    lenOfPhantomLine = (prevLineTail[1] - prevLineHead[1]) 
    Hypotenuse = CalculateHypotenuse(lenOfPhantomLine, counter, positionOfSpiral) 
    radius = int(Hypotenuse)

    print(f'Left-Down Hand Side: Length of the radius in Manhattan Metric unit sphere {radius} Loop No {counter}. \n')

    # Counter is used as a switch to change the direction of the each line generated  
    if ( counter % 2 == 0):
        newLineHead = ComputeNewLineThirdQuadrant(radius, prevLineHead)
         
    else:
         newLineHead = ComputeNewLineFourthQuadrant(-radius, prevLineHead)
   
    print(f'Left-Down Side: New point after function compute newline: {newLineHead} Loop No {counter}. \n')

    return newLineHead


def GenerateNewLinesRightDown( prevLineHead, prevLineTail, counter):

    # Identification string
    positionOfSpiral = "Right-Down Hand Side"
                
    # To get the radius of the L_1 unit sphere respective to previous head 
    lenOfPhantomLine = (prevLineTail[1] - prevLineHead[1]) 
    Hypotenuse = CalculateHypotenuse(lenOfPhantomLine, counter, positionOfSpiral) 
    radius = int(Hypotenuse)

    print(f'Right-Down Hand Side: Length of the radius in Manhattan Metric unit sphere {radius} Loop No {counter}. \n')

    # Counter is used as a switch to change the direction of the each line generated  
    if ( counter % 2 == 0):
        newLineHead = ComputeNewLineThirdQuadrant(-radius, prevLineHead)
         
    else:
         newLineHead = ComputeNewLineFourthQuadrant(radius, prevLineHead)
   
    print(f'Right-Down Hand Side: New point after function compute newline: {newLineHead} Loop No {counter}. \n')

    return newLineHead


# Left side spiral
def GenerateNewLinesLEFT( prevLineHead, prevLineTail, counter):

    # Identification string
    positionOfSpiral = "Left Hand Side"
                
    # To get the radius of the L_1 unit sphere respective to previous head 
    lenOfPhantomLine = (prevLineTail[1] - prevLineHead[1]) 
    Hypotenuse = CalculateHypotenuse(lenOfPhantomLine, counter, positionOfSpiral) 
    radius = int(Hypotenuse)

    print(f'Left Hand Side: Length of the radius in Manhattan Metric unit sphere {radius} Loop No {counter}. \n')

    # Counter is used as a switch to change the direction of the each line generated  
    if ( counter % 2 == 0):
        newLineHead = ComputeNewLineSecondQuadrant(radius, prevLineHead)
    else:
        newLineHead = ComputeNewLineThirdQuadrant(radius, prevLineHead)
        
    print(f'Left Hand Side: New point after function compute newline: {newLineHead} Loop No {counter}. \n')

    return newLineHead 

def GenerateNewLinesRIGHT( prevLineHead, prevLineTail, counter):

    # Identification string
    positionOfSpiral = "Right Hand Side"
                
    # To get the radius of the L_1 unit sphere respective to previous head 
    lenOfPhantomLine = (prevLineTail[1] - prevLineHead[1]) 
    Hypotenuse = CalculateHypotenuse(lenOfPhantomLine, counter, positionOfSpiral) 
    radius = int(Hypotenuse)

    print(f'Right Hand Side: Length of the radius in Manhattan Metric unit sphere {radius} Loop No {counter}. \n')

    # Counter is used as a switch to change the direction of the each line generated  
    if ( counter % 2 == 0):
        newLineHead = ComputeNewLineFourthQuadrant(radius, prevLineHead)
    else:
        newLineHead = ComputeNewLineFirstQuadrant(radius, prevLineHead)
   
    print(f'Right Hand Side: New point after function compute newline: {newLineHead} Loop No {counter}. \n')

    return newLineHead


def main():

    global Tail
    global Head

    global TailTwo # Second Spiral
    global HeadTwo

    global TailThree # Third Spiral
    global HeadThree

    global TailFour # Four Spiral
    global HeadFour


    # Generate Lines
    for lines in range(NUM_OF_LINES):
        newLineHead = GenerateNewLinesRIGHT(Head , Tail, lines)
        myLines.append([newLineHead,Head])
        Tail = Head
        Head = newLineHead

    for lines in range(NUM_OF_LINES):
        newLineHeadTwo = GenerateNewLinesLEFT(HeadTwo , TailTwo, lines+1)
        myLines.append([newLineHeadTwo, HeadTwo])
        TailTwo = HeadTwo
        HeadTwo = newLineHeadTwo

    for lines in range(NUM_OF_LINES):
        newLineHeadThree = GenerateNewLinesRightDown(HeadThree , TailThree, lines)
        myLines.append([newLineHeadThree, HeadThree])
        TailThree = HeadThree
        HeadThree = newLineHeadThree

    for lines in range(NUM_OF_LINES):
        newLineHeadFour = GenerateNewLinesLeftDown(HeadFour , TailFour, lines+1)
        myLines.append([newLineHeadFour, HeadFour])
        TailFour = HeadFour
        HeadFour = newLineHeadFour


    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
        
        window.fill((0, 0, 0))

        # Render Lines
        for lines in range(NUM_OF_L):
                 pygame.draw.line(window, lineColour,myLines[lines][0], myLines[lines][1] , LINE_WIDTH)
        
        for lines in range(4):
            pygame.draw.line(window, lineColour,myLines[lines+11][0], myLines[lines+11][1] , LINE_WIDTH)



        
        pygame.display.flip()

    pygame.quit()


main()