nums = [12, 34, 25, 46, 52, 29]
nums_iter = iter(nums)
try:
    print(next(nums_iter))
    print(next(nums_iter))
    print(next(nums_iter))
    print("Uff tired...")
    print(next(nums_iter))
    print(next(nums_iter))
    print("How many more??")
    print(next(nums_iter))
    print(next(nums_iter))

except StopIteration:
    print('Iteration is stopped!!')
