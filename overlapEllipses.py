# Name = Monish Manjunath
# Date = 02/23/2020
# Honor statement = I have not given or received any unauthorized assistance on this assignment.
# Video link Url = "https://youtu.be/Nn4zS2qmbuo "



import math
from warandpeaceRNG import WarAndPeacePseudoRandomNumberGenerator as WPRNG

class Point():
    """ A class which accepts a point object """
    
    def __init__(self, xcoord, ycoord):
        """ Constuctore function for Point class   """
        self.x = xcoord                                             # Set X co ordinate
        self.y = ycoord                                             # Set Y co ordinate
    
    def setx(self, xcoord):
        """ Sets X coordinate """                                   # Set X co ordinate
        self.x = xcoord
    
    def sety(self, ycoord):
        """ Sets Y coordinate """
        self.y = ycoord                                             # Set Y co ordinate
    
    def move(self, dx, dy):
        """ This function moves the x and y coorodinate by a specified value """
        self.x = self.x + dx                                        # Move the X co ordinate by the given value
        self.y = self.y + dy                                        # Move the Y co ordinate by the given value

    def getx(self):
        """ Returns x value """
        return self.x                                               # Return X co ordinate
    
    def gety(self):
        """ Returns y value """
        return self.y                                               # Return Y co ordinate
    
    def __repr__(self):
        """ This function returns the cannonical string representation """
        return "Point({}, {})".format(self.x, self.y)

class Ellipse():
    """ Create an ellipse class  """

    def __init__(self, p1, p2, width):                                  # the ellipse class accepting two points and the width 
        """ A constructore class of ellipse class initializing values """  
        self.p1 = p1
        self.p2 = p2
        self.width = width
        self.centervalx = (p1.x + p2.x) / 2
        self.centervaly = (p1.y + p2.y) / 2
        self.center = Point(self.centervalx, self.centervaly)
        self.area = self.width / 2                                  

        if self.centervaly == self.p1.y:                                    # If the centaer y is equal to the y value of point 1
            self.b = math.sqrt(math.pow(self.area, 2) - math.pow(self.p1.x -self.centervalx, 2))    # Calculating for values to send to rectangle class
            self.rect  = Rectangle(self.centervalx - self.area, self.centervaly + self.b, self.centervaly - self.b, self.centervalx + self.area)      # Calling the rectangle class  with thedimension of the rectangle
        else:
            self.b = math.sqrt(math.pow(self.area,2) - math.pow(self.p1.y)- self.centervaly, 2)
            self.rect = Rectangle(self.centervalx - self.b, self.centervaly + self.area, self.centervaly - self.area, self.centervalx + self.b)
        self.area = math.pi * self.area * self.b                                       # Calcualting the area of the ellipse

    def valueinellipse(self, point):
        """ Fucntion to check if the point is in the ellipse """
        point1distance = distance(self.p1, point)                   # Calling the distance  class and sending the  point 1 value
        point2disatnce = distance(self.p2, point)                   # Calling the distance  class and sending the  point 2 value

        if point1distance + point2disatnce <= self.width:           # Checking if the sum of the distance of the point is less than width
            return (True)                                           # return true if the sum is  less the width
        else:
            return (False)                                          # return false if the sum is more the width


class Rectangle():
    """ This class create a rectangle with dimension of top, bottom, left and right  """
    def __init__(self, left, top, bottom, right):
        """ The constructor class for the rectangle class which initializes  all the values """
        self.left = left                                            # Value of the left boudnary in the rectangle
        self.top = top                                              # Value of the top  boudnary in the rectangle
        self.bottom = bottom                                        # Value of the bottom boudnary in the rectangle
        self.right = right                                          # Value of the right boudnary in the rectangle

    def ifpointinside(self, p):
        """ Checks if the point is inside the rectangle """
        if p.ycoord >= self.top and p.ycoord <= self.bottom and p.xcoord >= self.left and p.xcoord <= self.right:
            return True                                             # return true if the point is present inside
        else:
            return False                                            # return false if the point is present inside
    
    def __repr__(self):
        """ This function returns the cannonical string reprsentation  """
        return "Top: {}, Bottom: {}, Right: {}, Left: {}". format(self.top, self.bottom, self.right, self.left)



class ComputeRectangleValues():
    """  This class is created to obtain the boundary values of the rectangle """

    def __init__(self, ellipse1, ellipse2):
        """ The constructor class for the outline class which initializes  all the values """
        self.ellipse1 = ellipse1                                    # Initalize the ellipse 1 value  
        self.ellipse2 = ellipse2                                    # Initalize the ellipse 2 value  
        leftboundary = min(ellipse1.rect.left, ellipse2.rect.left)                          # Calculating the left boundary of the rectangle
        rightboundary = max(ellipse1.rect.right, ellipse2.rect.right)                       # Calculating the right boundary of the rectangle
        bottomboundary = min(ellipse1.rect.bottom, ellipse2.rect.bottom)                    # Calculating the bottom boundary of the rectangle
        topboundary = max(ellipse1.rect.top, ellipse2.rect.top)                             # Calculating the top boundary of the rectangle

        self.length = topboundary - bottomboundary                                          # Calculating the length of the rectangle
        self.width = rightboundary - leftboundary                                           # Calculating the width of the rectangle
        self.rect = Rectangle(leftboundary, topboundary, bottomboundary,rightboundary)      # Calling the rectangle fucntion and sending the appropriate values
        

class ComputeOverlapOfEllipses():
    """ This class computes the overlap area of ellipses """
    def __init__(self, x1, samples = 100):
        self.x1 = x1
        self.rng = WPRNG()                              # Calling the war and peacer random number genrator function
        self.count = 0                                  # Initalising count value
        self.lstofpoints = []                           # Intialising the number  of  sample points
        self.samples = samples
        self.hits = self.hitpoints()                    # Calling the hit points function

    
    def hitpoints(self):
        """ This fucntion checks if the points are in the ellipse and increments the count """
        for i in range(self.samples):

            a = (self.x1.rect.right - self.rng.random() * self.x1.width)
            b = (self.x1.rect.top - self.rng.random() * self.x1.length)

            p = Point(a,b)                                  
            self.lstofpoints.append(p)                                  # Appening the points to the list of points

            if self.x1.ellipse1.valueinellipse(p)  and self.x1.ellipse2.valueinellipse(p):   # Checking if the point is both in ellipse 1 and ellipse 2
                self.count += 1                                         # incrementing count if the point is in both ellipses 
        return ((self.count/self.samples)* (self.x1.width * self.x1.length))


def distance(point1, point2):
    """ This function returns a total distance by accepting the x and y values """
    x = point1.x - point2.x
    y = point1.y - point2.y
    totaldistance = (math.sqrt(math.pow(x, 2) + math.pow(y,2)))                 # Calculating the distacne to check if the point is inside  
    return totaldistance        


def main():
    """ This is the main function which calls the appropriate function calls and display the value of the overlapping area """
    p1 = Point(0,0)                                                 
    p2 = Point(0,0)
    p3 = Point(0,0)
    e1 = Ellipse(p1, p2, 2)
    e2 = Ellipse(p2, p3, 3)
    overlap = ComputeRectangleValues(e1, e2)

    success = ComputeOverlapOfEllipses(overlap, 10000)
    print("The overlapping area of an ellipse is: " + str(success.hits))

main()



