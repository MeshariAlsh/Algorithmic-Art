import math


class Util:

    @staticmethod

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
        #print(f'{positionOfSpiral}: Value of Hypotenuse: {Hypotenuse} | Loop No. {counter}\n')
        return Hypotenuse
