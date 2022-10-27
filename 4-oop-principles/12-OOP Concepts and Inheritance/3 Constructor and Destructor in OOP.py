import time

class School:
    def __init__(self, name, address, principle=''):
        self.name = name
        self.address = address
        self.principle = principle
        self.grades = []

    def add_grade(self, name, teacher):
        new_grade = Grade(name, teacher)
        self.grades.append(new_grade)

    def remove_grade(self, name):
        idx = 0
        for i, grade in enumerate(self.grades):
            if grade.name == name:
                idx = i
        del self.grades[idx]

class Grade:
    def __init__(self,name, teacher):
        self.students = []
        self.name = name
        self.teacher = teacher

    def __repr__(self) -> str:
        return f'{self.name} with teacher {self.teacher}'

    def __del__(self):
        print(f'Deleting {self.name} with teacher {self.teacher}')

oxford = School('Oxford', 'Natore', 'Mokhles')
oxford.add_grade('class 5', 'obaidur Sir')
oxford.add_grade('Class 8', 'Jalal Sir')
oxford.add_grade('Class 7', 'Kamrul Sir')

print(oxford.grades)
oxford.remove_grade('class 8')
print(oxford.grades)

print('code running done!')
time.sleep(10)