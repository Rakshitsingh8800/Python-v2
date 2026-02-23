class dog:

    species = "Canis familiaris"

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    def display_details(self):
        print("Name: ", self.name)
        print("Breed: ", self.breed)
        print("Species: ", dog.species)
        print("---------------------------------")

dog1 = dog("Labrador", "Buddy")
dog2 = dog("German Shepherd", "Max")

dog1.display_details()
dog2.display_details()