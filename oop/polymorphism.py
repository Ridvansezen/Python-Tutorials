class Animal:
    def squeal(self):
        pass
    

class Dog(Animal):
    def squeal(self):
        print("Bark Bark!")
        
        
class Cat(Animal):
    def squeal(self):
        print("Meow Meow!")
        
        
class Bird(Animal):
    def squeal(self):
        print("Chirp!")
        
        

squel_sounds = [Dog(), Cat(), Bird()]

for squeal in squel_sounds:
    squeal.squeal()