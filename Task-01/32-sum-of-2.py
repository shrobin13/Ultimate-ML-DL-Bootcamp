n = int(input("Enter the value of n: "))

sum = 0
val = 0
for i in range(1, n + 1):
    val *= 10
    val += 2
    sum += val

print(f"Total: {sum}")
