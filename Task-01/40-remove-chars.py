inp = input("Enter val: ")

res = ""
for i in range(len(inp)):
    if inp[i].isnumeric():
        res += inp[i]

print(res)
