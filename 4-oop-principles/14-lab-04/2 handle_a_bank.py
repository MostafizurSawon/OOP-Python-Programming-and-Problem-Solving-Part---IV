""" 
Manages bank account
owner: SawOn
E-mail: mostafizur1102@gmail.com
"""

class Account:
    accID = 1

    def __init__(self, name, age, nid_num,balance):
        self.name = name
        self.age = age
        self.nid_num = nid_num
        self.balance = balance

    # update account id
        self.accout_id = Account.accID
        Account.accID += 1

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


acc1 = Account('Sawon', 28, 700533566, 500)
acc2 = Account('Gopi', 28, 700533589, 1500)
# print('You have:',acc1.balance)

# print(acc1.accout_id)
# print(acc2.accout_id)
print("Initial balance: ")
print(acc1.balance)

print('After Deposit:')
acc1.deposit(3000)
print(acc1.balance)

print('After withdraw:')
acc1.withdraw(2000)
print(acc1.balance)