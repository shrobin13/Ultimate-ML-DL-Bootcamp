l1_x = int(input("First L1 x: "))
l1_y = int(input("First L1 y: "))
r1_x = int(input("First R1 x: "))
r1_y = int(input("First R1 y: "))
l2_x = int(input("Second L2 x: "))
l2_y = int(input("Second L2 y: "))
r2_x = int(input("Second R2 x: "))
r2_y = int(input("Second R2 y: "))

if r1_x < l2_x or r2_x < l1_x:
    print("Rectangles are not overlapping!")
elif r1_y > l2_y or r2_y > l1_y:
    print("Rectangles are not overlapping!")

else:
    print("Rectangles are overlapping!")
