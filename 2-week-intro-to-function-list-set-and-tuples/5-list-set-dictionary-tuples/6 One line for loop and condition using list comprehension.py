numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
names = ['Sawon', 'sumon', 'gopi', 'Zim']
ages = [23, 42, 54,27]
odd_numbers = [num for num in numbers if num%2 == 1 and num%3!=0]

# print(odd_numbers)

pair = [(nam, age) for nam in names for age in ages if age<30]

print(pair)

