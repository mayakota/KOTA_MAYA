length = float(input("The length of the rectangle is: "))
width = float(input("The width of the rectangle is: "))

def calcPerim(length, width):
    p = (2 * length) + (2 * width)
    return(p)
print("Your rectangle is ", calcPerim(length, width), " ft around.")


