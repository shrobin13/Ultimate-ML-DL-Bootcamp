num = int(input("Enter n: "))

sum = 0
i = 1
while i <= num:
    if i % 5 == 0:
        i += 1
        continue
    if sum > 300:
        break
    sum += i
    i += 1


print(f"Sum: {sum}")
