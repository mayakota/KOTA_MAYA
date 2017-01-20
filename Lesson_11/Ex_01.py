class MilesPerHour:
    def __int__(self, d, h, m):
        self.distance = d
        self.hours = h
        self.minutes = m
        self.mph = 0

    def setValues(self, newDistance, newHours, newMinutes):
        self.distance = newDistance
        self.hours = newHours
        self.minutes = newMinutes
        self.mph = 0

    def getDist(self):
        return self.distance

    def getHours(self):
        return self.hours

    def getMins(self):
        return self.minutes

    def getMPH(self):
        self.mph = self.distance / ((self.hours + self.minutes) / 60.0)
        return self.mph

def main():
    distance = int(input("Please enter the distance: "))
    hours = int(input("Please enter the hours: "))
    minutes = int(input("Please enter the minutes: "))

    newUser = MilesPerHour(distance, hours, minutes)
    print(newUser.getDist(), "miles in", newUser.getHours(), "hours and", newUiser.getMins(), "=", user.MPH())
    newUser.setValues(10, 2, 0)
    print(newUser.getDist(), "miles in", newUser.getHours(), "hours and", newUiser.getMins(), "=", user.MPH())

main()
