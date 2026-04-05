import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    # Method to compute area
    def area(self):
        return math.pi * self.radius ** 2

    # Method to compute perimeter (circumference)
    def perimeter(self):
        return 2 * math.pi * self.radius


# Create an object of the class
r = float(input("Enter the radius of the circle: "))
c = Circle(r)

print("Area of the circle:", c.area())
print("Perimeter of the circle:", c.perimeter())