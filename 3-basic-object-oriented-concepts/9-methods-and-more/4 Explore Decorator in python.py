import math
import time

def timer(func):
    def inner(*args, **kwargs):
        print('Time Start')
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(end - start)
        print('Time End')
    return inner

@timer
def get_factorial(n):
    res = math.factorial(n)
    print(f'factorial of {n} = {res}')

# timer(get_factorial)()
get_factorial(n=60)