""" Exercise 5: Check if the first and last number of a list is the same
Given:

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]
Expected Output:

Given list: [10, 20, 30, 40, 10]
result is True

numbers_y = [75, 65, 35, 75, 30]
result is False
 """

def check(a,n):
    if (a[0] == a[n-1]):
        return True
    else:
        return False

# numbers_x = [10,20,30,40,10]
numbers_x = [75, 65, 35, 75, 30]
len = len(numbers_x)

print(check(numbers_x, len))