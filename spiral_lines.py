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
NUM_OF_L = 10 

myLines = []
storePointsfrom = []

# Second Line information 
diffcolor = (255, 255, 0)
lineColour = (255, 0, 0)
HeadTwo = (centerWindowPos[0], centerWindowPos[1] - 100)
TailTwo = (centerWindowPos[0], centerWindowPos[1])
LINE_WIDTH = 5
NUM_OF_LINES = 5 
myLines = []
storePointsfrom = []

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

def main():

    global Tail
    global Head

    global TailTwo # Second line
    global HeadTwo

    # Generate Lines
    for lines in range(NUM_OF_LINES):
        newLineHead = GenerateNewLinesRIGHT(Head , Tail, lines)
        myLines.append([newLineHead,Head])
        Tail = Head
        Head = newLineHead
        #storePointsfrom.append([newLineHead,Head]) # For the spirl to appear on the top of the old spirl coords

    for lines in range(NUM_OF_LINES):
        newLineHeadTwo = GenerateNewLinesLEFT(HeadTwo , TailTwo, lines+1)
        myLines.append([newLineHeadTwo,HeadTwo])
        TailTwo = HeadTwo
        HeadTwo = newLineHeadTwo

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
                 


        
        pygame.display.flip()

    pygame.quit()


main()