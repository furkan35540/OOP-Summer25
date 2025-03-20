class Animal:
    def __init__(self, name, group, number_of_legs, skills):
        self.name = name
        self.group = group
        self.number_of_legs = number_of_legs
        self.skills = skills

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Group: {self.group}")
        print(f"Number of Legs: {self.number_of_legs}")
        print(f"Skills: {', '.join(self.skills)}")
        print("-" * 30)


# List of animals as objects
animals = [ Animal("Cat", "Mammals", 4, ["jumping", "climbing", "hunting"]),
    Animal("Dog", "Mammals", 4, ["running", "hunting", "smelling"]),
    Animal("Frog", "Amphibians", 4, ["jumping", "swimming", "croaking"]),
    Animal("Shark", "Fish", 0, ["swimming", "hunting", "detecting vibrations"]),
    Animal("Snake", "Reptiles", 0, ["slithering", "camouflaging", "hunting"])]

# Displaying information for each animal
for animal in animals:
    animal.display_info()
