import math
class Animal:
    def __init__(self,name, weightKg, heightM, isPredator, speedKph):
        self.name = name
        self.weightKg = weightKg
        self.heightM = heightM
        self.isPredator = isPredator
        self.speedKph = speedKph
        self.activityMultipller = 1.2
        
    def getBmi(self):
        return round(self.weightKg / (self.heightM ** 2),2)
    
    def getDailyCalories(self):
        return (math.floor((70 * self.weightKg ** 0.75) * self.activityMultipller * 100) / 100)
    

       

    def isDangerous(self):
        if self.isPredator or self.heightM >= 1.7 or self.speedKph >= 35:
            return True
        else:return False



rabbit = Animal("rabbit", 10, 0.3, False, 20)
print(rabbit.getBmi())
print(rabbit.isDangerous())
snake =  Animal("snake", 30, 1, True, 30)
print(snake.isDangerous())
print(snake.getDailyCalories())
elephant =  Animal("elephant", 300, 3, False, 5)
print(elephant.getBmi())
print(elephant.getDailyCalories())
gazelle =  Animal("gazelle", 50, 1.5, False, 100)
print(gazelle.getDailyCalories())
print(gazelle.isDangerous())
