n = int(input("Enter a number to find factorial: "))

factorial = 1
for i in range(1, n+1):
    factorial *= i

print("The factorial of the given number",n,"is",factorial)