str = 'madam'
l = len(str) - 1
count = True
r = int(l/2)

for i in range(r):
    if str[i] != str[l]:
        count = False
    l -= 1

if count:
    print("palindrome")
else:
    print("Not palindrome!")

# if (str[: : -1]) == str:
#     print('Palindrome')

# else:
#     print("Not palindrome!")