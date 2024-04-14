class Dog:

    def __init__(self, name, size, age):
        self.name = name
        self.size = size
        self.age = age

    def bark(self):
        if self.size >= 50:
            return "Wooof! Woof!"
        elif self.size >= 20:
            return "Ruff! Ruff!"
        else:return "Yip! Yip!"

    def calcHumanAge(self):
        return 12 + (self.age - 1) * 7


goldenRetriever = Dog("Golden Retriever", 60, 10)
print(goldenRetriever.bark())
print(goldenRetriever.calcHumanAge())

siberianHusky = Dog("Siberian Husky", 55, 6)
print(siberianHusky.bark())
print(siberianHusky.calcHumanAge())

poodle = Dog("Poodle", 10, 1)
print(poodle.bark())
print(poodle.calcHumanAge())

shibaInu = Dog("Shiba Inu", 35, 4)
print(shibaInu.bark())
print(shibaInu.calcHumanAge())
