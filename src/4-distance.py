import math as m

x1 = float(input("x ordinate first point: "))
y1 = float(input("y ordinate first point: "))

x2 = float(input("x ordinate second point: "))
y2 = float(input("y ordinate second point: "))


def calc_distance(x1, x2, y1, y2):
    return m.sqrt((x1 - x2)**2 + (y1 - y2)**2)


distance = calc_distance(x1, x2, y1, y2)

print(f"Distance Between two coordinate is: {distance:.3f}")
