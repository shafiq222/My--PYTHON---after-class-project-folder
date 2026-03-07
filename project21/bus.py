# Parent class
class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity

    # Method to calculate total fare
    def fare(self):
        return self.capacity * 100   # 100 is fare per passenger


# Child class
class Bus(Vehicle):

    # Override fare() to add 10% maintenance charge
    def fare(self):
        total = super().fare()
        maintenance_charge = total * 0.10
        return total + maintenance_charge


# Creating a Bus object
school_bus = Bus(50)

# Printing the total fare
print("Total Bus Fare:", school_bus.fare())