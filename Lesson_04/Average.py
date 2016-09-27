num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

def average(num1, num2, num3):
    a = (num1 + num2 + num3) / 3
    return(a)
print("The average of" , num1 , num2 , "and" , num3, "is", average(num1, num2, num3)")
