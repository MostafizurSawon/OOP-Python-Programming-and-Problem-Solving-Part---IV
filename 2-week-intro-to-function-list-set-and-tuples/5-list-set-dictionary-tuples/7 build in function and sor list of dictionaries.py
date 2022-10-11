largest = max(34, 23, 45, 65, 12, 15, 29)
# print(largest)
nums = [2, 5, 3, 1, 7, 4, 8, 6, 9]
rev_num = list(reversed(nums))
# print(rev_num)

sorted_nums = sorted(nums, reverse=True)
# print(sorted_nums)

actors = [
    {'name': 'Sakib', 'age': 39},
    {'name': 'Sawon', 'age': 27},
    {'name': 'sumon', 'age': 38},
    {'name': 'Zim', 'age': 27},
    {'name': 'Gopi', 'age': 38},
]

# sorted_actors = sorted(actors,key = lambda actor: actor['age'], reverse=True)
sorted_actors = sorted(actors, key=lambda actor: actor['name'], reverse=False)

print(sorted_actors)
frnd = ['Sawon', 'Sumon', 'Sumon', 'Zim', 'Suu']

print(sorted(frnd))
