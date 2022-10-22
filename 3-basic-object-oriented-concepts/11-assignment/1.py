def exp(a, n):
    if a == 0:
        print("First number can not be zero")
        return

    res = pow(a, n)
    return res

print(">> Enter numbers: ", end='')
a, n = input().split()
a ,n = [int(a), int(n)]

print(">> Result is: ", end='')
print(exp(a, n))
