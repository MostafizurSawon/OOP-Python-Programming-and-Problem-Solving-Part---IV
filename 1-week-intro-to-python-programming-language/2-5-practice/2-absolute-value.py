
for i in range(3):
    print('Input', i+1, ": ", end='')
    num = int(input())
    if num < 0:
        num = num * - 1
        print('Output', i+1, ": ", end='')
        print('Absolute value :', num)
    else:
        print('Output', i+1, ": ", end='')
        print('Absolute value :', num)
