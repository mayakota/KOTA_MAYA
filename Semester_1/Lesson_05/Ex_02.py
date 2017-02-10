def format(item, price):
    print("{:<12}\t{:>15f}".format(item, price))

item1 = input("Enter the first item: ")
price1 = float(input("Enter the first price: "))

item2 = input("Enter the second item: ")
price2 = float(input("Enter the second price: "))

item3 = input("Enter the third item: ")
price3 = float(input("Enter the third price: "))

item4 = input("Enter the fourth item: ")
price4 = float(input("Enter the fourth price: "))

subtotal = price1 + price2 + price3 + price4

print("The subtotal is", subtotal)

if subtotal >= 2000:
    discount = .15 * subtotal

if subtotal < 2000:
    discount = 0 * subtotal

tax = .07 * subtotal

total = subtotal - discount + tax

print("<<<<<<<<<<<<<<< Receipt >>>>>>>>>>>>>")
   
format(item1, price1)
format(item2, price2)
format(item3, price3)
format("Subtotal: ", subtotal)
format("Discount: ", discount)
format("Total: ", total)

print("_____________________________")
print("Thank you for your support")
