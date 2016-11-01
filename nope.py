area = 0
radius = 6

def calcRadius():
    global radius; area = 3.14 * (radius ** 2);

def radPrint():
    print("the rad is: ", area)

calcRadius()
radPrint()
