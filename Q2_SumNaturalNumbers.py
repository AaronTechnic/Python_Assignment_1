n = int(input("Enter a positive integer N: "))
sum = 0

for i in range(1,n+1):
    sum+=i

print(f"Sum of the first {n} natural numbers is {sum}")
