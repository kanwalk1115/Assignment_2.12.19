number= int(input("Enter a number"))
x = 1
for i in range(number):
    x = x * (i + 1)

print (f"The factorial of {number} is {x}")
