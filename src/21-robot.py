import math

down = int(input("Enter down step: "))
up = int(input("Enter up step: "))
left = int(input("Enter left step: "))
right = int(input("Enter right step: "))

x_axis = right - left
y_axis = up - down

distance = math.sqrt(x_axis**2 + y_axis**2)

print(f"Total distance: {round(distance)}")
