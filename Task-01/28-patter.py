n = int(input("Enter the value of n: "))

for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(i + 1):
        print("*  ", end=" ")
    print()


# pythonic way ( ofcourse chatgpt )
# n = int(input("Enter the value of n: "))
#
# for i in range(n):
#     print("  " * (n - i - 1) + "*   " * (i + 1))
