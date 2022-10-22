import random

while(True):
    student_id = str(random.randint(100, 100000000))
    student_name = input('Student name: ')
    mark = input('Students mark: ')
    with open('out.txt', 'a') as output:
        output.write("Student Id: ")
        output.write(student_id)
        output.write("    ")
        output.write("Student Name: ")
        output.write(student_name)
        output.write("    ")
        output.write("Mark: ")
        output.write(mark)
        output.write("\n")