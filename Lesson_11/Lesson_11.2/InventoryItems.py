import random
class Item:
    def __init__(self, tManufacturer, tName, tCategory = "", tPrice = ""):
        self.itemManufacturer = tManufacturer
        self.itemName = tName
        self.itemCategory = tCategory
        self.itemPrice = tPrice
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

    def getUserUPC(self):
        return self.userUPC
    
    def __str__(self):
           print("Customer Info...\nItem Manufacturer: ", self.itemManufacturer, "\nItem Name: ", self.itemName, "\nItem Category: ", self.itemCategory, "\nItem Price: ", self.itemPrice, "\nUser Price: ", self.userUPC)

def main():
    tName = input("Please enter the item's name: ")
    tManufacturer = input("Please enter the item's manufacturer: ")
    info = input("Will you be entering category and price information?")
    if info == "n":
        item1 = Item(iName, iManufacturer)
    else:
        tCategory = input("Please enter the item's category: ")
        tPrice = int(input("Please enter the item's price: "))
        item1 = Item(tManufacturer, tName, tCategory, tPrice)

    print(item1.__str__())

main()
            
        
        
                    
    
