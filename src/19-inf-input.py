
state = True
sum = 0
n_inp = -1

while state:
    inp = int(input("Enter number (0 to exit): "))
    if inp == 0:
        state = False

    sum += inp
    n_inp += 1


print(f"Sum of input: {sum}\nAverage of input: {sum/n_inp}")
