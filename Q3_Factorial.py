num = int(input("Enter an integer: "))
fact = 1
c = num

if num < 0:
    print("Factorial invalid for negative numbers.")
else:
    while c > 0:
        fact *= c
        c -= 1
    print("The factorial is", fact)
