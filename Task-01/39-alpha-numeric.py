inp = input("Enter alpha numeric: ")

sum = 0
count = 0

for i in range(len(inp)):
    if (inp[i].isnumeric()):
        sum += int(inp[i])
        count += 1


print(f"Total: {sum}\nAverage: {sum/count}")
