class Laptop:
    def __init__(self, brand, ram):
        self.brand = brand
        self.ram = ram

    def increase_ram(self, ram = 4):
        self.last_ram = self.ram - 30
        self.ram = self.ram + ram

    def repair(self, ram_decrease = -7):
        self.increase_ram(ram_decrease)

my_laptop = Laptop('Lenovo', 8)
my_laptop.increase_ram()
my_laptop.increase_ram()
my_laptop.ram = 64
my_laptop.increase_ram()

# print(my_laptop.ram)
# print(my_laptop.last_ram)

print(my_laptop.ram)
my_laptop.repair(-9)
print(my_laptop.ram)

print(my_laptop.__dict__)