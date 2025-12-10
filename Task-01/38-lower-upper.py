inp = input("Enter the value: ")

result = ""

for i in range(len(inp)):
    if (inp[i].islower()):
        result += inp[i]

for i in range(len(inp)):
    if (inp[i].isupper()):
        result += inp[i]

print(result)
