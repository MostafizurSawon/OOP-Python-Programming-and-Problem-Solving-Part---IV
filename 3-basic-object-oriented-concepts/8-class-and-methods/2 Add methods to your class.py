
class Phone:
    brand = 'Sony'
    model = 'Xperia 5'
    color = 'Red'
    price = 60000
    features = ['Android', 'Camera', 'Wifi', 'Bluetooth', 'Snapdragon 855', 'Oled display', '3130 mah battery']

    def call(self):
        print("calling ... tut tut tut tut tut tut tut tut")

    def send_sms(self, msg, num):
        sms = f'sending {msg} to {num}'
        return sms

my_phone = Phone()
print(my_phone.features[2])
my_phone.call()         #TypeError: Phone.call() takes 0 positional arguments but 1 was given

sms = my_phone.send_sms('Hello', 8801920693718)
print(sms)

#self is a must

    