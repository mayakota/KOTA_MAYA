grade1 = input("What grade did you receive in your first class?")
grade2 = input("What grade did you receive in your second class?")
grade3 = input("What grade did you receive in your third class?")
grade4 = input("What grade did you receive in your fourth class?")
grade5 = input("What grade did you recieve in your fifth class?")
grade6 = input("What grade did you receive in your sixth class?")
grade7 = input("What grade did you receive in your seventh class?")

def calcPoints(grade):
    if grade == "A" :
        return 4.0
    if grade == "B" :
        return 3.0
    if grade == "C" :
        return 2.0
    if grade == "D" :
        return 1.0
    if grade == "F" :
        return 0.0
GPA = float((calcPoints(grade1) + calcPoints(grade2) + calcPoints(grade3) + calcPoints(grade4) + calcPoints(grade5) + calcPoints(grade6) + calcPoints(grade7))/7)
print("Your GPA is: ", GPA)
