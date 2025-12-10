inp = input("Enter the string: ")
word = input("Enter the word: ")


def is_there(word, inp):
    word_inp = ""
    count = 1
    for i in range(len(inp)):
        if inp[i] != " ":
            word_inp += inp[i]
        if inp[i] == " " or i == len(inp) - 1:
            if word == word_inp:
                return count
            count += 1
            word_inp = ""
    return -1


pos = is_there(word, inp)

print(f"Word position: {pos}")
