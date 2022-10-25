# poly => many
# morph => different

# print(4+3)
# print('Hello' + ' Sawon')
# print([23,43] + [45, 98])

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Animal making sound!")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print("Meow Meow!")

class Dog(Animal):
    def __init__(self, name):
        # super().__init__(name)
        Animal.__init__(self,name)

    def make_sound(self):
        print("Bark bark")

class Horse(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print("Hresh Hresha")


don = Cat('don')
# don.make_sound()

doggy = Dog('German Shepard')
# doggy.make_sound()

manik = Horse('Manik')
# manik.make_sound()

don2 = Dog('Asol Don')

animals = [don,doggy,manik,don2]
for animal in animals:
    animal.make_sound()

