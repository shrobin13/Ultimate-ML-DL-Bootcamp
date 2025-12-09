import math

f_num = int(input("Enter the numerator of first fraction: "))
f_denom = int(input("Enter the denominator of first fraction: "))

s_num = int(input("Enter the numerator of second fraction: "))
s_denom = int(input("Enter the denominator of second fraction: "))


num = (f_num * s_denom) + (s_num * f_denom)
denom = f_denom * s_denom
gcd = math.gcd(num, denom)

print(f"""
Result:
        {num//gcd}
        -----
        {denom//gcd}
      """)
