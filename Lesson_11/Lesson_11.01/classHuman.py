class human:
    def __init__(self, h, e, s):
        self.hair = h
        self.eyes = e
        self.skin = s

    def setHES(self, newHair, newEyes, newSkin):
        self.hair = newHair
        self.eyes = newEyes
        self.skin = newSkin

    def getHair(self):
        return self.hair

    def getEyes(self):
        return self.eyes

    def getSkin(self):
        return self.skin

def main():
    hair = input("Please enter your hair color: ")
    eyes = input("Please enter your eye color: ")
    skin = input("Please enter your skin color: ")

    features = human(hair, eyes, skin)

    print("My info... ")
    print("Hair: black")
    print("Eyes: brown")
    print("Skin: tan")

    print("Your info...")
    print("Hair", features.getHair())
    print("Eyes", features.getEyes())
    print("Skin", features.getSkin())

main()
    
    
    
