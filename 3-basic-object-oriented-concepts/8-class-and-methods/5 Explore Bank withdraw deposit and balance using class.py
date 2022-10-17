class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 500
        self.max_withdraw = 20000

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount < self.min_withdraw:
            return "Sorry You have to withdraw at least 500 taka!"

        elif amount > self.balance:
            return f"Sorry you have only {self.balance} taka!"
        
        elif amount > self.max_withdraw:
            return f"Sorry You have crossed your limit of {self.max_withdraw} taka!"

        elif amount > self.balance-500:
            return f"Sorry you have to keep at least 500 taka in your account!"

        elif amount%500 != 0:
            return f"Sorry we have only 500 and 1000 taka note!"

        else:
            self.balance -= amount
            return f'Here is your money: {amount}\nYour current balance is: {self.balance}'

    def deposit(self, amount):
        self.balance += amount

my_bank = Bank(19000)
# reply = my_bank.withdraw(120)
# reply = my_bank.withdraw(22000)
# reply = my_bank.withdraw(20000)
reply = my_bank.withdraw(18500)
print(reply)
my_bank.deposit(6123)
# print(reply)
my_bank.withdraw(2500)
print('Your current bank balance: ', my_bank.get_balance())