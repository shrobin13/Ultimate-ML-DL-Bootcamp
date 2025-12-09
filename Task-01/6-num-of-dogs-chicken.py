num_of_head = int(input("Enter the number of head: "))
num_of_legs = int(input("Enter the number of legs: "))

no_dogs = (num_of_legs - (2 * num_of_head))/2

print(f"Number of Chicken: {num_of_head - no_dogs}")
print(f"Number of Dogs: {no_dogs}")
