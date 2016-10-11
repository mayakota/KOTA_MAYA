height = float(input("What is your height?"))
weight = float(input("What is your weight?"))
condition = "undetermined"
BMI = (weight / height) * 703

def calcBMI():
    global BMI
    global condition 
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


