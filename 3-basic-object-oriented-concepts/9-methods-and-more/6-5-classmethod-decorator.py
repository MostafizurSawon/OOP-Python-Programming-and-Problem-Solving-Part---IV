class Shopping:
    mall = 'Jamuna Future Park'
    hours = []

    def __init__(self, customer):
        self.customer = customer
        self.items = []
        self.total = 0

    @classmethod
    def opening_hour(cls,day):
        return cls.mall

    @staticmethod
    def multiply(a, b):
        return a * b

    def add_to_total(self, amount):
        self.total += amount
        # print(self.total)
    
    def add_to_cart(self, item, price, quantity):
        item_total = price * quantity
        # self.total += item_total
        self.add_to_total(item_total)
        self.items.append(item)
        

    def checkout(self):
        pass


# https://www.tutorialspoint.com/class-method-vs-static-method-in-python