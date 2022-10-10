numbers = [23, 12, 24, 16,12, 39, 26, 71]

# print(numbers[2])
# print(numbers[-6 ])

# print(numbers[1:5])
# print(numbers[1:-3])
# print(numbers[1:])

# list[ start: end: step]
# print(numbers[2: 7: 2])
# print(numbers[-2: -7: -2])
# print(numbers[:])
# print(numbers[: : -1])  # reverse print

numbers.append(89)
numbers[len(numbers):] = [99]

numbers.insert(2,100)
numbers.remove(71)
numbers.pop(4)
# numbers.clear()
# print(numbers)
# numbers.index(12,1,5)

numbers.sort()


# print(numbers.count(12))
numbers.reverse()

num2 = numbers.copy()

print(numbers[:])
print(num2)






# python list       https://docs.python.org/3/tutorial/datastructures.html
