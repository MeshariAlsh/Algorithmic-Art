import pygame
import math
import time
import Spiral

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
NUM_OF_LINES = 5 
NUM_OF_RENDERED_LINES = 2
myLines = []
drawing = []

def main():

    global Head
    global Tail

    spiral1 = Spiral.Spiral(Head, Tail)
    myLines.append([Head, Tail])

    for row_of_patterns in range(5):
        for p in range(1,3):
            if len(myLines) < 5:
                for j in range(2,4):
                    if len(myLines) < 5:

                        sign = (-1) ** j 
                        Head = (centerWindowPos[0] + ( p * 200 * sign), centerWindowPos[1] - 50 - (50 * (p - 1)))
                        Tail = (centerWindowPos[0] + ( p * 200 * sign), centerWindowPos[1] + 50 - (50 * (p - 1)))
                        myLines.append([Head, Tail])
                        
            # Top row 
            elif len(myLines) >= 5 and len(myLines) <= 9 :
                #initial the center of the row
                if len(myLines) == 5  and len(myLines) < 6:
                        Head = (centerWindowPos[0], centerWindowPos[1] - 300)
                        Tail = (centerWindowPos[0], centerWindowPos[1] - 200)
                        myLines.append([Head, Tail])
                        
                for j in range(2,4):

                    sign = (-1) ** j 
                    Head = (centerWindowPos[0] + ( p * 200 * sign), centerWindowPos[1] - 230 - (70 * (p - 1)))
                    Tail = (centerWindowPos[0] + ( p * 200 * sign), centerWindowPos[1] - 130 - (70 * (p - 1)))
                    myLines.append([Head, Tail])
                   
            # Bottom Row
            elif len(myLines) >= 10 and len(myLines) <= 15 :
                    #initial the center of the row
                if len(myLines) == 10  and len(myLines) < 11:
                        Head = (centerWindowPos[0], centerWindowPos[1] + 100)
                        Tail = (centerWindowPos[0], centerWindowPos[1] + 200)
                        myLines.append([Head, Tail])
                        
                for j in range(2,4):
                    sign = (-1) ** j 
                    Head = (centerWindowPos[0] + ( p * 200 * sign), centerWindowPos[1] + 150 - (50 * (p - 1)))
                    Tail = (centerWindowPos[0] + ( p * 200 * sign), centerWindowPos[1] + 250 - (50 * (p - 1)))
                    myLines.append([Head, Tail])
                   
    for j in range (15):
        for i in range(4):
            spiral1 = Spiral.Spiral(myLines[j][0], myLines[j][1])
            spiral1.GenerateSpiralPattern(i)
            drawing.append(spiral1.lines)

            spiral1.head= myLines[j][0]
            spiral1.tail = myLines[j][1]

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
        
        window.fill((245, 245, 220))
        
        # Render Lines
        for patterns in drawing:
                    for lines in patterns:
                        pygame.draw.line(window, lineColour, lines[0], lines[1] , LINE_WIDTH)

        pygame.display.flip()

    pygame.quit()

main()