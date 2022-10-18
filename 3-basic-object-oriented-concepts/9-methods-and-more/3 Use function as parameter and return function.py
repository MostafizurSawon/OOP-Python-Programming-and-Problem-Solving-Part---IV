# def do(work):
#     print('Start')
#     work()

# def prac():
#     print('Python')

# def learning():
#     print('Learning')

# do(prac)
# do(learning)

def do():
    print('Start')
    
    def ins():
        print('Inner')

    ins()

# do()

def learning():
    print('Learning')

    def ins2():
        print('Inner2nd')

    return ins2

# first = learning()
# print(first)
# first()
learning()()
