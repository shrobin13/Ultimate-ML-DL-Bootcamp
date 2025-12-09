a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a + b > c and b+c > a and c+a > b:
    print("Triangle is possible!")
else:
    print("Triangle is not possible!")
