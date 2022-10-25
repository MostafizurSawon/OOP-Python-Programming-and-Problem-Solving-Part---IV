# read only property

class Student:
    def __init__(self, name, id, marks):
        self._name = name
        self.__id = id
        self.marks = marks

    @property
    def student_id(self):
        return self.__id

    @property
    def name(self):
        return self._name

    @name.deleter
    def name(self):
        del self._name


sawon = Student('Sawon ss', 17, 89)
print(sawon.student_id)

# sawon.student_id = 34   # will not work (read only)
print(sawon.student_id)
print(sawon.name)

del sawon.name

# print(sawon.name)
print(dir(sawon))


