import math
class Distance:
    def __int__(self, x1, y1, x2, y2):
        self.xOne = x1
        self.yOne = y1
        self.xTwo = x2
        self.yTwo = y2
        self.distance = 0

    def setValues(self, newX1, newY1, newX2, newY2):
        self.xOne = newX1
        self.yOne = newY1
        self.xTwo = newX2
        self.yTwo = newY2
        self.distance = 0
    
    def getMPH(self):
        self.distance = math.sqrt((self.xTwo - self.xOne) * (self.xTwo - self.xOne) + (yTwo - yOne) * (yTwo - yOne))
        return self.distance

def main():
    x1 = int(input("Please enter a number for X one: "))
    y1 = int(input("Please enter a number for Y one: "))
    x2 = int(input("Please enter a number for X two: "))
    y2 = int(input("Please enter a number for Y two: "))
    
        
        
