#l inheritance

# base class will have only the common attributes and methods

class Device:
    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color

    # def __repr__(self):
    #     return f'Laptop {self.brand} : {self.price} : {self.color}'

class Laptop(Device):
    def __init__(self, brand, price, color,disk_size):
        super().__init__(brand, price, color)
        self.disk_size = disk_size

    def run(self):
        print("Running the laptop.")

    def __repr__(self):
        return f'Laptop {self.brand} : {self.price} : {self.color}'

    def purchase(self,money):
        if(money < self.price):
            return f'give {self.price-money} more money.'
        else:
            print('This device is ready for you.')
            return money-self.price

class Phone:
    def __init__(self, brand, price, color, camera,sim_number):
        self.brand = brand
        self.price = price
        self.color = color
        self.camera = camera
        self.sim_number = sim_number

    def is_dual_sim(self):
        return self.sim_num > 1

    def __repr__(self):
        return f'Phone {self.brand} : {self.price} : {self.color}'

class Watch:
    def __init__(self, brand, price, color, watch_type):
        self.brand = brand
        self.price = price
        self.color = color
        self.watch_type = watch_type

    def is_digital(self):
        return self.watch_type == 'digital'

class Manager:
    def __init__(self,name,salary,experience,designation):
        pass

    def withdraw_salary(self):
        pass

    def day_total_sales(self):
        pass

    def handle_customer_complain(self):
        pass

class SalePerson:
    def __init__(self,name,salary,experience,designation):
        pass

    def withdraw_salary(self):
        pass

    def handle_customer(self):
        pass

lenovo = Laptop('Lenovo',50000,'red','1tb')
hp = Laptop('hp',4000,'black','500gb')

print(lenovo)
print(hp)

oppo = Phone('Oppo', 12000, 'black', '12mp', 2)
print(oppo)

print(hp.brand)
