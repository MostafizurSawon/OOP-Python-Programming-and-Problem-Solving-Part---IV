""" 

Exercise 10: Create a new list from a two list using the following condition

Create a new list from a two list using the following condition

Given a two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.

Given:

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
Expected Output:

result list: [25, 35, 40, 60, 90]
 """

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

list3 = []

for i in range(len(list1)):
    if(list1[i] % 2 == 1):
        list3.append(list1[i])
    if(list2[i] % 2 == 0):
        list3.append(list2[i])

print(list3)