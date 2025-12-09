first = int(input("Enter first term: "))
second = int(input("Enter second term: "))
nth_pos = int(input("Enter the nth position: "))

nth_term = first + (nth_pos - 1) * (second - first)

print(f"Nth term of series: {nth_term}")
