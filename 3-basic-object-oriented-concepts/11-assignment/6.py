def func(arg1, arg2, arg3=4, arg4=5):
    print(arg1, arg2, arg3, arg4)

# func(6, 7)
# func(4, 5, arg3=6)
# func()
func(3, 4, arg2=1)


# a. 6 7 4 5
# b. 4 5 6 5
# c. TypeError: func() missing 2 required positional arguments: 'arg1' and 'arg2'
# d.  func() got multiple values for argument 'arg2'