#public protected private 

class Account:
    def __init__(self,holder):
        self._account_holder = holder

class StudentAccount(Account):
    def __init__(self,holder,balance,school):
        self.__balance = balance

    def withdraw(self, amount):
        if amount > self.__balance:
            print('Not enough to withdraw')
            return
        self.__balance -= amount
        return amount
    
    def deposit(self, amount):
        if amount<0:
            return 'Negative can not be deposited'
        self.__balance += amount

    def get_balance(self):
        return self.__balance

sawon = StudentAccount('Sawon', 50000, 'Oxford')
# sawon.withdraw(200000)
sawon.deposit(40000)
# print(sawon.get_balance())

# print(dir(sawon))
# print(sawon.__balance)

print(sawon._StudentAccount__balance)