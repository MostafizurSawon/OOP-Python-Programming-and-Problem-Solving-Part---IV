class Shopping:
    def __init__(self, customer):
        self.customer = customer
        self.items = []
        self.total = 0

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

result = Shopping.multiply(47,2)
print(result)

my_shopping = Shopping('Sawon')
my_shopping.add_to_total(599)
print(my_shopping.total)

result_3 = my_shopping.multiply(15,5)
print(result_3)
# result = Shopping.add_to_total(self, amount)