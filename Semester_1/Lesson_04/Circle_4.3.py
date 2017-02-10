r = float(input("Enter the radius of the circle: "))

def area(r):
    global area
    area = 3.14159 * (r * r)

area(r)
print("The area of the circle is", area)
