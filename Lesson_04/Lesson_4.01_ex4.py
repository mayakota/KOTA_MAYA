def volume(l, w, h):
    v = l * w * h
    return(v / 1728)
l = float(input("Enter the length of the subwoofer in inches: "))
w = float(input("Enter the width of the subwoofer in inches: "))
h = float(input("Enter the height of the subwoofer in inches: "))

print("The volume of the subwoofer is ", volume(l, w, h), " cubic feet.")



