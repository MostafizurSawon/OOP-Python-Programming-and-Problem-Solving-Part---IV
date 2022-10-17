class Shop:
    cart = []
    def __init__(self, buyer):
        self.buyer = buyer

    def add_to_cart(self, item):
        self.cart.append(item)
        
shopper_1 = Shop("Sawon")
shopper_1.add_to_cart('t-shirt')
print(shopper_1.cart)

shopper_2 = Shop("Gopi")
shopper_2.add_to_cart('Jeans Pant')
print(shopper_2.cart)

