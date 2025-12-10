n = int(input("Enter the value of n: "))
x = int(input("Enter the value of x: "))


sum = 1
for i in range(2, n + 1):
    sum += (x**i/i)

print(f"Total sum: {sum:.3f}")
