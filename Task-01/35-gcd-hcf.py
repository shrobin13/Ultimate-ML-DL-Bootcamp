def hcf(a, b):
    return a if b == 0 else hcf(b, a % b)


def lcm(a, b):
    return (a * b)//hcf(a, b)


a = int(input("Enter a: "))
b = int(input("Enter b: "))

print(f"GCD:{lcm(a, b)}\nHCF: {lcm(a, b)}")
