
# print 1 to 10 in reverse order
num = 10
count = 1

for i in range(num+1):
    if num == 0:
        continue
    print(count,'=>',num)
    num -= 1
    count += 1