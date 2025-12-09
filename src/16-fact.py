given_num = int(input("Factorial of: "))

factorial = 1
for i in range(1, given_num + 1):
    factorial *= i

print(f"Factorial of {given_num} is: {factorial}")
