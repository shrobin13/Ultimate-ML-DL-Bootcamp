# //murhy theme neovim

n = int(input("Enter decimal value: "))

bin_str = ""

while n:
    bin_str = bin_str + str(n % 2)
    n //= 2

print(bin_str[::-1])
