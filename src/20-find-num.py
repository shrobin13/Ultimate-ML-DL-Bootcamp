def is_all_digits_even(num):
    for i in range(0, len(num)):
        if int(num[i]) & 1 == 1:
            return False

    return True


list_of_num = []
for i in range(1000, 3001):
    if is_all_digits_even(str(i)):
        list_of_num.append(i)

for i in range(0, len(list_of_num)):
    print(list_of_num[i], end=" ")
