import pygame
import math
import time
import Spiral

pygame.init()
window = pygame.display.set_mode((1000,1000))
sizeWindow = pygame.display.get_window_size()
centerWindowPos = (sizeWindow[0] / 2 , sizeWindow[1] /2) 

# Line information 
diffcolor = (255, 255, 0)
lineColour = (0, 0, 0)
Head = (centerWindowPos[0], centerWindowPos[1] - 100)
Tail = (centerWindowPos[0], centerWindowPos[1])
LINE_WIDTH = 7
NUM_OF_SPIRAL_VARIANTS = 4
myLines = []
drawing = []

# Row pattern information
x_step =  200 
y_offset = 50
 
def generate_patterns(offset_multiplier, x_step , y_offset, row_type):
     
     if row_type == "top":
        y_head_multiplier = - 5
        y_tail_multiplier = - 3
        Head = (centerWindowPos[0], centerWindowPos[1] - 300)
        Tail = (centerWindowPos[0], centerWindowPos[1] - 200)
        myLines.append([Head, Tail])

     elif row_type == "middle":
        y_head_multiplier = - 1
        y_tail_multiplier = 1
           
     elif row_type == "bottom":
        y_head_multiplier = 3
        y_tail_multiplier = 5
        Head = (centerWindowPos[0], centerWindowPos[1] + 100)
        Tail = (centerWindowPos[0], centerWindowPos[1] + 200)
        myLines.append([Head, Tail])
           
     for j in range(2,4):
        sign = (-1) ** j 
        Head = (centerWindowPos[0] + ( offset_multiplier * x_step * sign), 
                centerWindowPos[1] + (y_offset * y_head_multiplier) - (y_offset * (offset_multiplier - 1)))
        
        Tail = (centerWindowPos[0] + ( offset_multiplier * x_step * sign), 
                centerWindowPos[1] + (y_offset * y_tail_multiplier) - (y_offset * (offset_multiplier - 1)))
        print(f"Value of Head: {Head} and Tail: {Tail}  ___{row_type}__")
        myLines.append([Head, Tail])
      
def generate_row (row_type):
    
    for offset_multiplier in range(1,3):
         generate_patterns(offset_multiplier, x_step, y_offset, row_type)
            
def main():

    global Head
    global Tail
    global myLines

    #Initialise the centered spiral pattern
    spiral1 = Spiral.Spiral(Head, Tail)
    myLines.append([Head, Tail])
    
    # Generates the coords for each spiral pattern
    generate_row("middle")
    generate_row("top")
    generate_row("bottom")

    print(f"Size of myline: {len(myLines)} \n")
    
    # Generates the spiral patterns
    for line in range (len(myLines)):
        for variant in range(NUM_OF_SPIRAL_VARIANTS):
            spiral1 = Spiral.Spiral(myLines[line][0], myLines[line][1])
            spiral1.GenerateSpiralPattern(variant)
            drawing.append(spiral1.lines) # Appends it to render later
            spiral1.head= myLines[line][0]
            spiral1.tail = myLines[line][1]

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
        
        window.fill((245, 245, 220))

        # Render complete artwork
        for patterns in drawing:
                    for lines in patterns:
                        pygame.draw.line(window, lineColour, lines[0], lines[1] , LINE_WIDTH)

        pygame.display.flip()

    pygame.quit()

main()