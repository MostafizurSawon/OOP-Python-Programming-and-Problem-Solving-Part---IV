class Calculator:
    def add(self,num1, num2):
        return num1 + num2
    
    def subtract(self,num1, num2):
        return num1 - num2
    
    def multiply(self,num1, num2):
        return num1 * num2
    
    def divide(self,num1, num2):
        return num1 / num2

calc = Calculator()

add = calc.add(4,5)
print(add)

sub = calc.subtract(34,5)
print(sub)

mul = calc.multiply(5, 2)
print(mul)

div = calc.divide(78, 4)
print(div)

