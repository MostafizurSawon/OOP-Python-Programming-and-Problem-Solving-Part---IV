def double_it(num):
    result = num * 2
    # print(result)
    return result

# double_it(7)


def add(num1, num2):
    num1 = double_it(num1)
    total = num1 + num2
    # print(total)
    return total


sum = add(24, 43)


def multiply(num1, num2):
    result = num1 * num2
    # print(result)
    return result     #if not retunred that wll return "None"

# print(multiply(3, 2))


output = multiply(3, 4)
# print(output)

final_number = output + sum

print(final_number)