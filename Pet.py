import datetime


class Pet(object):

    def __init__(self, name, species, breed, color, gender, owner, address, birthdate, age):
        self.name = name
        self.species = species
        self.breed = breed
        self.color = color
        self.gender = gender
        self.owner = owner
        self.address = address
        self.birthdate = birthdate
        self.age = age

    def getDate(self):
        return datetime.datetime(self.birthdate)

    def getAge(self):
        return int(self.age)

    def description(self):
        return f"{self.name} is {self.getAge()} and is a {self.species} and is {self.color} "


class Dog(Pet):

    species = "Canis familiaris"

    def __init__(self, name, breed, color, gender):
        self.name = name
        self.breed = breed
        self.color = color
        self.gender = gender


class Puppy(Dog):

    def __init__(self, name, breed, color, gender, age):
        self.name = name
        self.breed = breed
        self.color = color
        self.gender = gender
        self.age = age

    def getAge(self):
        return f"{self.name} is {self.age * 12} months old"

    def play(self):
        return("(___()'`;\n      /,    /`\n      \\\\\"--\\\\")


def main():
    name = "Danny"
    species = Dog.species
    breed = "Golden Retriever"
    color = "golden"
    gender = "female"
    owner = "Ishant"
    address = "San Jose, CA"
    birthdate = datetime.datetime(2010, 4, 14)
    age = 12

    pet_specs = Pet(name, species, breed, color, gender, owner, address, birthdate, age)
    # pet_specs1 = Dog(species, breed, color, gender)
    pet_specs2 = Puppy(name, breed, color, gender, age)

    print(pet_specs.description())
    print(pet_specs.birthdate)
    print(pet_specs2.getAge())
    print(pet_specs2.description())
    print(pet_specs2.play())


main()

