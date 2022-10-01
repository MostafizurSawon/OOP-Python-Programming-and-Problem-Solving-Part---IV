num = 1

# print even numbers only
while num < 20:
    num += 1
    if num % 2 == 1:
        continue    # WON'T GO FURTHER to
    print(num)
    if num == 8:
        break
    
 