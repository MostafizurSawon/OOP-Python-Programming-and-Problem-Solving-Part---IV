balance = 5000


def total_cost(price, quantity):
    global balance  # not recommended
    cost = price * quantity
    remaining = balance - cost
    balance = remaining
    # print(remaining)
    return cost


print("outside balance before: ", balance)
# print(cost)       will not work
pay = total_cost(30, 5)
print(f' Please pay: {pay} taka')

print("outside balance after: ", balance)
