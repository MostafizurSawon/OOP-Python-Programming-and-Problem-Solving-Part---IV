""" 
Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.
https://pynative.com/python-basic-exercise-for-beginners/
 """

a = int(input())
b = int(input())

if a*b <= 1000:
    print(a*b)
else:
    print (a-b)

