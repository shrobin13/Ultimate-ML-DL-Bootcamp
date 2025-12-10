inp = input("Enter the value: ")


def is_present(ch, inp):
    for i in range(len(inp)):
        if inp[i] == ch:
            return True

    return False


res = ""

for i in range(len(inp)):
    if not is_present(inp[i], res):
        res += inp[i]


print(res)
