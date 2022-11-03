class Item:
    all = []
    def __init__(self,itemName,itemPrice) -> None:
        self.__itemName=itemName
        self.__itemPrice=itemPrice
        self.all.append(self)
    def __repr__(self) -> str:
        return f"Items are -> ({self.__itemName},{self.__itemPrice})"
        
item1 = Item("Gopi",69)
item2 = Item("Jim",34)
item1._Item__discount = 33
item1._Item__itemName = "Gopi Topi"
print(item1._Item__itemName)
# print(item1.__discount)
print(item1)
print(item1.__dict__)