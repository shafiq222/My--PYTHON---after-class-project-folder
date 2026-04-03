class Benz:
    
    def speed(self):
        print("Benz runs smoothly at 200 km/h")

    def fuel_type(self):
        print("Benz uses petrol or diesel")


class Ferrari:
    
    def speed(self):
        print("Ferrari runs very fast at 340 km/h")

    def fuel_type(self):
        print("Ferrari uses high-performance petrol")


# Polymorphism
cars = [Benz(), Ferrari()]

for car in cars:
    car.speed()
    car.fuel_type()
    print()