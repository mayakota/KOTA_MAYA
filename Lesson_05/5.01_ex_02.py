height = float(input("What is your height?"))
weight = float(input("What is your weight?"))

BMI = 0
condition = "undetermined"

def calcBMI(height,weight):
    global BMI,condition
    BMI = (weight/height) * 703
    if BMI < 18.5 :
        condition = "condition is Underweight"
    elif BMI < 24.9 :
        condition = "condition is Normal"
    elif BMI < 29.9 :
        condition = "Overweight"
    elif BMI < 34.9 :
        condition = "Obese"
    elif BMI < 39.9 :
        condition = "Very obese"
    elif BMI > 39.9 :
        condition = "Morbidly Obese"

calcBMI(height, weight)
print("Your BMI is", BMI)
print("Your condition is", condition)


