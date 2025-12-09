def is_neil_armstrong(num):
    sum = 0
    for i in range(len(num)):
        digit = int(num[i])
        sum += (digit * digit * digit)
        if (sum > int(num)):
            return False

    return sum == int(num)


start_range = int(input("Enter the starting range:"))
end_range = int(input("Enter the ending range:"))

for i in range(start_range, end_range):
    if is_neil_armstrong(str(i)):
        print(f"{i} is neil Armstrong!")
