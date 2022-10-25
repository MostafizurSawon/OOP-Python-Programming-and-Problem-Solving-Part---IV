class Account:
    def __init__(self, holder, initial_balance):
        self.holder = holder    # public attribute
        self._account_number = 12
        self.__balance = initial_balance    # public attribute, can not be accessed outside

    def deposit(self,amount):
        print(f'Adding {amount} to your account')
        self.__balance += amount

    def withdraw(self,amount):
        print(f'Withdrawing {amount} from your account')
        self.__balance -= amount

class StudentAccount(Account):
    def __init__(self, holder, initial_balance,school):
        self.school = school
        super().__init__(holder, initial_balance)

    def get_balance(self):
        return self.__balance


gopi = StudentAccount('Gopi', 60000, "DIU")
# print(gopi.__balance)
print(gopi.holder)
gopi.deposit(15000)
gopi.withdraw(10000)

# print(gopi.get_balance())

# gopi.__balance = 0
gopi.deposit(12000)
# print(gopi.__balance)

gopi._account_number = 137
print(gopi._account_number)


