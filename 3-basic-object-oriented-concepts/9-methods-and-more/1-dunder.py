# f_name = 'Gopi'
# l_name = 'Tupi'
# print(f_name + ' ' + l_name)

# num_1 = [1,3,5,7]
# num_2 = [2,4,6,8]
# print(num_1 + num_2)

# is_good = False
# is_bad = True
# print(is_good + is_bad)


# dunder
# special method
# magic method

# https://docs.python.org/3/reference/datamodel.html

class Person:
    def __init__(self, name, age, money) -> None:
        self.name = name
        self.age = age
        self.money = money

    def __add__(self, other):
        return self.age + other.age
        # return self.money + other.money

gopi = Person('Gopi', 28, 800)
dalim = Person('dalim', 27, 767)

print(dalim+gopi)
# print(type(gopi))

