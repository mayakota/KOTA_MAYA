class Car:
    def __int__(self, p, i, e, t):
        self.paint = p
        self.interior = i
        self.engine = e
        self.tires = t

    def setCustom(self, newPaint, newInterior, newEngine, newTires):
        self.paint = newPaint
        self.interior = newInterior
        self.engine = newEngine
        self.tires = newTires
        
    def getPaint(self):
        return self.paint

    def getInterior(self):
        return self.interior

    def getEngine(self):
        return self.engine

    def getTires(self):
        return self.tires
    
