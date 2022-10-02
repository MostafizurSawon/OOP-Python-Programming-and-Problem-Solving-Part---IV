loop = True
counter = 1
while loop:
    print('> input',counter,': ', end='')
    counter += 1
    inp = input()

    if inp == 'Quit' or inp == 'quit' or inp == 'Exit' or inp == 'exit':
        print("Tata bye bye!")
        loop = False
        break
    else:
        inp = int(inp)
    if inp == 0:
        print(inp,"is ZERO!")
    elif inp > 0 :
        print(inp,'is POSITIVE!')
    else:
        print(inp,'is NEGATIVE!')