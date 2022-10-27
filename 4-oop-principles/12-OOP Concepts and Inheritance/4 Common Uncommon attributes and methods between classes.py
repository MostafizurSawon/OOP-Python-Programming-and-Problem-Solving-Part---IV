#laptop, phone, watch, tablet

class laptop:
    def __init__(self, brand, price, color,disk_size):
        self.brand = brand
        self.price = price
        self.color = color
        self.disk_size = disk_size

    def run(self):
        print("Running the laptop.")

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





    

