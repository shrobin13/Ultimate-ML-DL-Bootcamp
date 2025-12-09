num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

temp = num1
num1 = num2
num2 = temp

print(f"First Number: {num1}\nSecond Number: {num2}")

# num1, num2 = num2, num1 //pythonic way to swap values
