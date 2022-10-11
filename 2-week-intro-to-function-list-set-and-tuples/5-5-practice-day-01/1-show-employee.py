def show_employee(name="anonymous", salary=9000):
    employee = f'Name ---> {name} \nSalary -> $ {salary} '
    return employee

# emp = show_employee("Mostafizur Rahman", 50000)
# emp = show_employee("Mostafizur")
emp = show_employee()

print(emp)