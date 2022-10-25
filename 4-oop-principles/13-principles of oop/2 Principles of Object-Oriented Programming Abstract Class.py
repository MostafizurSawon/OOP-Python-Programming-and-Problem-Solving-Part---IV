from abc import ABC, abstractmethod

# Abstract Base Class

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

    @property
    @abstractmethod
    def name(self):
        # print('Godzilla')
        pass

    @abstractmethod
    def move(self):
        print('moving around the zoo.')

class Monkey(Animal):
    def __init__(self):
            self.__name = 'Monkey'

    def sing(self):
        print("Monkey is singing")

    def eat(self):
        print("Eating banana")

    def move(self):
        print('hanging and moving around the zoo.')
        super().move()

    @property
    def name(self):
        # return 'Godzilla name called!'
        return self.__name
    
    @name.setter
    def name(self,value):
        self.__name = value


laika = Monkey()
# print(laika)

# laika.eat()
# laika.move()
# laika.name()
# print(laika.name())

laika.name = 'King of monsters'

print(laika.name)

# https://www.tutorialspoint.com/Difference-between-abstract-class-and-interface#:~:text=An%20abstract%20class%20can%20contain,extended%2C%20while%20Interfaces%20are%20implemented.

#  abstract class vs interface