class Person:
    def __init__(self,name,phone,age) -> None:
        assert age >= 18, f"Only greater than 18 is accepted on line 3"
        assert len(phone)==11, f"Invalid phone no on line 4"
        self.name=name
        self.phone=phone
        self.age=age

    def __repr__(self) -> str:  # print
        return f"Name -> {self.name}\nPhone -> {self.phone}\nAge -> {self.age}"
    
user = Person("Sawon","01928473726",19)
print(user)