num = int(input("Enter integer value: "))

reversed = 0
while num > 0:
    reversed *= 10
    reversed += num % 10
    num //= 10


print(f"Reversed integer: {reversed}")
