# method overloading
# print('Max number:',max(34,2,78,67,57,86,86))
# print('Max number:',max([13,45,67]))
# print('Max:',max('A','B','C','D','E','F'))

def add(num1, num2, num3=0):
    return num1 + num2 + num3

# res = add(12,90)
# print(res)

# print(add(10,30))
# print(add(10,30,60))

def add2(*args, **kwargs):
    pass

# operator overloading
print(12+32)

class Account:
    def __init__(self, holder, balance):
        self.holder = holder
        self.__balance = balance

    def __add__(self,other):
        return self.__balance + other.__balance

    def __eq__(self, __o: object) -> bool:
        return self.__balance == __o.__balance

my_account = Account('Sawon', 89)
my_account2 = Account('Sawon2', 86)

res = my_account + my_account2
print(res)