# def square(x):
#     return x*x

square = lambda x: x*x

res = square(6)
# print(res)

add = lambda x,y: x + y
# print(add(34,21))

nums = [12,23,21,34,13,25,32]
def double_num(x):
    return x*2

double_lambda = lambda x: x*2

# doubles_nums = map(double_num, nums)

doubles_nums = map(lambda x: x*2, nums)

# print(f'{nums} -> {list(doubles_nums)}')

even_nums = filter(lambda num: num % 2 == 0 ,nums)
# print(f'{nums} -> {list(even_nums)}')

actors = [
    {'name': 'Sakib', 'age': 39},
    {'name': 'Sawon', 'age': 27},
    {'name': 'sumon', 'age': 38},
    {'name': 'Zim', 'age': 27},
    {'name': 'Gopi', 'age': 38},
]

senior_artists = filter(lambda actor: actor['age'] > 35, actors)
print(list(senior_artists))

junior_artists = filter(lambda actor: actor['age'] < 35, actors)
# print(list(junior_artists))
