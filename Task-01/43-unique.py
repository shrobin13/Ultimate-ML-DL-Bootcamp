inp1 = input("Enter first input: ")
inp2 = input("Enter second input: ")


def is_there(word, inp):
    word_inp = ""
    for i in range(len(inp)):
        if inp[i] != " ":
            word_inp += inp[i]
        if inp[i] == " " or i == len(inp) - 1:
            if word == word_inp:
                return True
            word_inp = ""
    return False


def find_for_each(inp1, inp2):
    word_in = ""
    lst = []
    for i in range(len(inp1)):
        if inp1[i] != " ":
            word_in += inp1[i]
        if inp1[i] == " " or i == len(inp1) - 1:
            if not is_there(word_in, inp2):
                lst.append(word_in)
            word_in = ""

    return lst


lst = find_for_each(inp1, inp2)
lst1 = find_for_each(inp2, inp1)
lst.extend(lst1)
print(lst)
