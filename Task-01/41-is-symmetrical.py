def is_symmetrical(val):
    str1 = val[:len(val)//2]
    str2 = val[len(val)//2:]

    return str1 == str2


inp = input("Enter the str: ")

if is_symmetrical(inp):
    print("Symmetrical!")
else:
    print("Not Symmetrical!")
