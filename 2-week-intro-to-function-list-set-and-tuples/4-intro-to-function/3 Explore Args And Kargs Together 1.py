def add(num1,num2, *num):
    # print(num1)
    # print(num2)
    # print(num)
    return num

add(3,4,5,6,7)

def full_name(f_name, l_name):
    name = f'{f_name} {l_name}'
    return name

name = full_name(l_name = 'Rahman', f_name = 'Mostafizur')

# print(name)

def long_name(**kargs):         #key args
    print(kargs)

#long_name(first = "Dr.",last = 'Chowdhury', middle = 'Sawon')

def name_mixed(first,last, **name_parts):
    print(first, last, name_parts)

# name = name_mixed(last = 'Rahman', first = 'Mostafizur', middle='First')

def all_types(first, *args, **kargs):
    print(first)
    for nam in args:
        print("args=> ",nam)
    print("kargs=> ",kargs)
    for key, value in kargs.items():
        print(key, value)

all_types('abc','def','ghi','jkl','mno',name = 'abul', father = 'babul')