num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
num3 = float(input("Enter your third number: "))

def average(num1, num2, num3):
    global average
    average = (num1 + num2 + num3) / 3

average(num1, num2, num3)
print("The average of the three numbers is", average)
