numbers = [12, 34, 25, 12, 30, 25, 45]
numbers_tuple = 12, 34, 25, 12, 30, 25, 45
nums_tuple = (12, 14, 17)
# print(numbers_tuple)

# numbers_tuple[3] = 67
# del numbers_tuple[1]      immuteables, tuple method does not allow to add or delete

# print(numbers_tuple[2])

tuple2D = ([23,34,12], [12,23,])
tuple2D[0][1] = 78      #works
# print(tuple2D)

short_tuple = 3,
# short_tuple[1] = 2  wont work

tuple_from_list = tuple(numbers)
print(tuple_from_list, short_tuple)