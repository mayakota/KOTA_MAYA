def compound(p, r, n, t):
    a = p * (1 + r / n)**(n * t)
    return(a / (12 * t))

p = float(input("Enter the principal: "))
r = float(input("Enter your interest rate: "))
n = float(input("Enter the number of times the loan is compounded per year: "))
t = float(input("Enter the life of the loan: "))

print("Your compound interest is ", compound(p, r, n, t), " dollars.")









           
