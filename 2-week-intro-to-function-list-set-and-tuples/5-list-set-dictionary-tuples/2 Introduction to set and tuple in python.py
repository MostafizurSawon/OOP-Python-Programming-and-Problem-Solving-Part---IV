#No duplicate allowed in sets
numbers = [12, 34, 25, 12, 30, 25, 45]
nums = {12, 34, 25, 12, 30, 25, 45}
# print(numbers, nums)

numbers_set = set(numbers)      #uniqe numbers
numbers_set.add(25)
numbers_set.add(15)

print(numbers_set)

