
l = float(input("What is the length of the rectangle?: "))
w = float(input("What is the width of the rectangle?: "))

def calcPerim(l, w):
    global calcPerim
    calcPerim = (2 * l) + (2 * w)

calcPerim(l, w)
print("The perimeter of the rectangle is", calcPerim, "ft around.")

    
