sent = input("Enter the str: ")

short_form = sent[0]

for i in range(len(sent)):
    if sent[i] == " " and i+1 < len(sent) - 1:
        short_form += sent[i+1]

print(short_form)
