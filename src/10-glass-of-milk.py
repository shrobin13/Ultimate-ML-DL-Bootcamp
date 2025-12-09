h_mt = int(input("Height of milk tank: "))
w_mt = int(input("width of milk tank: "))
b_mt = int(input("breadth of milk tank: "))

h_g = int(input("Height of a glass: "))
r_g = int(input("Radius of a glass: "))

vol_t = h_mt * w_mt * b_mt
vol_g = 3.1416 * r_g * r_g * h_g

print(f"Number of glass: {int(vol_t//vol_g)}")
