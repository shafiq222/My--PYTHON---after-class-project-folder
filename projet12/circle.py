import math

def get_circumference(radius):
    return 2 * math.pi * radius

# Get input from the user
user_radius = float(input("Enter the radius of the circle: "))

# Call the function and store the result
final_val = get_circumference(user_radius)

print(f"A circle with radius {user_radius} has a circumference of {final_val}")