numbers = [2,3,4,12,34,56,54]
# total = sum(numbers)
# print(numbers)

nums = {12, 23, 24, 32, 45,34}
nums_tuple = 12, 23, 24, 32, 45,34
marks = {'physic': 67, 'chemistry': 76, 'mathematics': 89}
total= 0

for num in numbers:
    total+=num

# print(total)

for num in nums:
    total+=num

# print(total)

for num in nums_tuple:
    total+=num

# print(total)

# for mark in marks:
#     val=marks['physic']
#     val=marks[mark]
    # print(mark,val)

for subject, mark in marks.items():
    print(subject, mark)

# for i,num in enumerate(numbers):    #will show index number vvvvv
    # print(i,"->",num)




# https://docs.python.org/3/library/functions.html