first_str = input("Enter first str: ")
second_str = input("Enter second str: ")

result = ""

for i in range(len(first_str)):
    result += first_str[i]

    if (i == (len(first_str)//2) - 1):
        result += second_str


print(result)
