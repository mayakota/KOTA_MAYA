def receipt(item1, price1, item2, price2, item3, price3):
    print("{:<6}\t{:15f}".format(item1, price1))
    print("{:<6}\t{:15f}".format(item2, price2))
    print("{:<6}\t{:15f}".format(item3, price3))

item1 = input("Please enter item 1:")
price1 = int(input("Please enter the price:"))
item2 = input("Please enter item 2:")
price2 = int(input("Please enter the price:"))
item3 = input("Please enter item 3:")
price3 = int(input("Please enter the price:"))

print("<<<<<<<<<<<__Receipt__>>>>>>>>>>")

receipt(item1, price1, item2, price2, item3, price3)

print("___________________________________")
print("Thank you for your support")



