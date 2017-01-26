import random
class Item:
    def __init__(self, iManufacturer, iName, iCategory = "", iPrice = ""):
        self.itemManufacturer = iManufacturer
        self.itemName = iName
        self.itemCategory = iCategory
        self.itemPrice = iPrice
        self.userUPC = random.randint(0, 1000000)

    def setTHING(self, newItemManufacturer, newitemName, newitemCategory, newitemPrice):
        self.itemManufacturer = newItemManufacturer
        self.itemName = newItemName
        self.itemCategory = newItemCategory
        self.itemPrice = newItemPrice
        self.userUPC = random.randint(0, 1000000)

    
    def getItemManufacturer(self):
        return self.itemManufacturer

    def getItemName(self):
        return self.itemName

    def getItemCategory(self):
        return self.itemCategory

    def getItemPrice(self):
        return self.itemPrice
    
    def __str__(self):
           print("Customer Info...\nItem Manufacturer: ", self.itemManufacturer, "\nItem Name: ", self.lastName, "\nAvatar: ", self.avatar, "\nUser ID#: ", str(self.userID))
    
