class Animal:
    def speak(self):
        print("Animal is speaking")  #This is the parent class
class Dog(Animal):
    def bark(self):
        print("Dog is barking")
class Cat(Animal):
    def meow(self):
        print("Cat is meowing")

d = Dog()
d.speak()

c = Cat()
c.meow()