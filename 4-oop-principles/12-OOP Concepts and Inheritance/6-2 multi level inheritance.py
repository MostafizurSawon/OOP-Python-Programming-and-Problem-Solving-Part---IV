class Vehicle:
    def __init__(self, name, license, price):
        self.name = name
        self.licence = license
        self.price = price
        print('Vehicle class init called.')

    def start(self):
        print(f'{self.name} started')

class Bus(Vehicle):
    def __init__(self, name, license, price,seat,ticket_price):
        self.seat = seat
        self.available_seats = seat
        self.ticket_price = ticket_price
        print('Bus init called.')
        super().__init__(name, license, price)

    def sell_ticket(self, quantity, amount):
        self.available_seats -= quantity
        remainer = amount - self.ticket_price* quantity
        if remainer >= 0:
            return Ticket(customer_name)
        return 'No ticket for you'

class AcBus(Bus):
    def __init__(self):
        print('Ac bus created.')

class MiniBus(Bus):
    def __init__(self):
        print('Mini Bus created.')
        super().__init__('Mimi Mini', 'Raj231', 1200000, 45, 654)

class Ticket:
    def __init__(self, owner):
        self.owner = owner

mini = MiniBus()
print(mini.name)

print(mini.seat)
        


    