n = int(input("Enter the value of n: "))

for i in range(2*n):
    if i <= n:
        for j in range(i):
            print("*", end=" ")
        print()
    else:
        for j in range(2*n-i):
            print("*", end=" ")
        print()
