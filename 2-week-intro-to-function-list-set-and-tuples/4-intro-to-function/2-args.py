def minus(num1, num2):
    total = num1 - num2
    # print(f'num1 = {num1}, num2 = {num2}')
    # print(total)
    return total

result = minus(num2 = 23, num1 = 12)
# print(result)

# output = minus(3) will show error message

def add(num1, num2 = 3):    #parameter must be at last position (num1, num4,num3,num2= 3)
    return num1 + num2

# print(add(5))

def mul2(*num): #args = *num
    # print(num)
    res = 1
    for n in num:
        # print(n)
        res = res * n
    # print(res)
    return res

output2 = mul2(3,4,5,6)
print(output2)
