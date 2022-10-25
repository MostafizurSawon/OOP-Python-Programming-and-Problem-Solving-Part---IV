# Abstract Class

class Book:
    def __init__(self, name):
      self.name = name

    def read(self):
        raise NotImplementedError   #must be implemented

    def exercise(self):
        pass

class Physics(Book):
    def __init__(self,name):
        super().__init__(name)

topon = Physics('Shahjahan Topon Sir')
# topon.read()
topon.exercise()
