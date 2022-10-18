from functools import partial

def get_num(a, b , c, d):
    return a*1000 + b*100 + c*10 + d

num = get_num(5,4,6,3)
# print(num)

fourth_only = partial(get_num, b = 0, c= 0, d=0)
num_2 = fourth_only(4)
print(num_2)


# https://docs.python.org/3/library/functools.html