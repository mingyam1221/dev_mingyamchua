class Dog:
    # Class attribute
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        #self.breed = breed

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} barks: {sound}"

    # Replace .description() with __str__()
    def __str__(self):
        return f"{self.name} is {self.age} years old"

class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

class GoldenRetriever(Dog):
    def speak(self, sound ="Bark"):
        return super().speak(sound)
