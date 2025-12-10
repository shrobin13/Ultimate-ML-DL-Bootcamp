n = int(input("Enter the value of n: "))

for i in range(n):
    for j in range(n, i, -1):
        print(j - i, end=" ")
    print()
