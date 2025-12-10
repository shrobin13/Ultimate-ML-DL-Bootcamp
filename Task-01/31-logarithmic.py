n = int(input("Enter the value of n: "))
x = int(input("Enter the value of x: "))


if x == 0:
    print("Invalid input. ")

else:
    base = (1 - 1/x)
    sum = 0

    for i in range(1, n + 1):
        if i < 2:
            sum += base
        else:
            sum += 0.5*(base**i)

    print(f"Total: {sum:.2f}")
