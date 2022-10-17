class Shopper:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        self.cart.append({'name': item, 'price': price, 'quantity': quantity})

    def checkout(self, amount):
        # print(self.cart)
        price = 0
        for item in self.cart:
            # print(item['price']*item['quantity'])
            price += item['price']*item['quantity']
        # print(price)
        if(amount < price):
            return f'Please give {price - amount} taka more!'
        elif(amount == price):
            return f'Thank you for your order, here are your products!'

        else:
            return f'Thank you for your order, here is your products and here is your {amount - price} taka!'
        

shopping = Shopper('Sawon')
shopping.add_to_cart('Shirt', 500, 2)
shopping.add_to_cart('Pant', 900,3)
shopping.add_to_cart('Sandles', 200,5)

reply = shopping.checkout(4700)
print(reply)