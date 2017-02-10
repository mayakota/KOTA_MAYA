side = float(input("Enter how large the side is: "))

def sa(side):
    global sa
    sa = 6 * (side * side)

sa(side)
print("The surface area of the cube is", sa)
