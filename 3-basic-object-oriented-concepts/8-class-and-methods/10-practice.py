
class Bank:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def withdraw(self, amount):
        if amount < self.amount:
            return f'Hey {self.name}, Here is your {amount} taka'
        
my_bank = Bank('SawOn', 5000)

money = my_bank.withdraw(3000)
print(money)