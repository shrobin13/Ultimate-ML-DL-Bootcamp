list_of_num = []

for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        list_of_num.append(i)

for i in range(0, len(list_of_num)):
    print(list_of_num[i], end=",")
