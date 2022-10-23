

# https://docs.python.org/3/reference/datamodel.html

class Person:
    def __init__(self, name, age, money, height) -> None:
        self.name = name
        self.age = age
        self.money = money
        self.height = height

    def __call__(self):
        print(f'This is {self.name}')

    def __eq__(self, other):
        return self.age == other.age

    def __len__(self):
        return self.height

    def __add__(self, other):
        return self.age + other.age
        # return self.money + other.money

gopi = Person('Gopi', 28, 800, 88)
dalim = Person('dalim', 27, 767,75)

print(dalim+gopi)
# print(type(gopi))
# gopi()
# print(gopi == dalim)
print(len(gopi))

