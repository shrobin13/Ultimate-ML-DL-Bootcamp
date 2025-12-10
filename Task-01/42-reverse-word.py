inp = input("Enter input: ")

res = ""
word = ""
for i in range(len(inp)):
    word += inp[i]
    if inp[i] == " ":
        res += word[::-1]
        word = ""
    if i == len(inp) - 1:
        res += " "
        res += word[::-1]

print(res[::-1])
