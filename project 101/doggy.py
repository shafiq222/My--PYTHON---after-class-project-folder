class Dog:
    # Class variable (shared by all dogs)
    species = "Canis familiaris"

    def __init__(self, name, breed):
        # Instance variables (unique to each dog)
        self.name = name
        self.breed = breed

    def display(self):
        print("Name:", self.name)
        print("Breed:", self.breed)
        print("Species:", Dog.species)
        print("---------------------")


# Creating two different dog objects with different breeds
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "German Shepherd")

# Displaying details
dog1.display()
dog2.display()