class Phone:
    manufacturer = "China"  #class/static varibale
    def __init__(self,brand,color,price):   #instance variable
        self.brand = brand
        self.color = color
        self.price = price

    def send_sms(self, msg, num):
        sms = f'sending {msg} to {num}'
        return sms

my_phone = Phone('Sony', 'Red', 60000)
print(f"Brand: {my_phone.brand}\nColour: {my_phone.color}\nPrice: {my_phone.price}\nManufactured by: {my_phone.manufacturer}")
print("\n")
dad_phone = Phone('Xiaomi','Blue', 19000)
print(f"Fathers Phone Brand: {dad_phone.brand}\nColour: {dad_phone.color}\nPrice: {dad_phone.price}\nManufactured by: {dad_phone.manufacturer}")