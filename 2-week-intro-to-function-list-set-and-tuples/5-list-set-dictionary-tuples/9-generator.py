nums = [12, 34, 25, 46, 52, 29]

def get_num(nums):
    for num in nums:
        yield num

res = get_num(nums)
print(next(res))
print(next(res))
print(next(res))
print('Exploring generator')
print(next(res))
print(next(res))
print(next(res))
# print(next(res))