class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        return f"{self.name} says hello!"

# Example usage
dog = Animal("Buddy", "Dog")
cat = Animal("Whiskers", "Cat")

print(dog.speak())
print(cat.speak())
print(cat.speak())
