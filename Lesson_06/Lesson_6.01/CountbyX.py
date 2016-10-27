number = int(input("Enter a number: "))
number2 = int(input("How much should each number go up by? "))

output = ""

printNumber ():
    for i in range (0, number, number2):
        output = output + str(i) + "\t"

printNumber()
print(output)
