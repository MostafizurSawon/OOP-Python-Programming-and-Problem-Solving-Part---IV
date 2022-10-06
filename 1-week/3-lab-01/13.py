""" original number 121
Yes. given number is palindrome number

original number 125
No. given number is not palindrome number
 """

num = 121
str = str(num)
# print(str)
n = len(str)


if str[0] == str[n-1]:
    print("Yes. given number is palindrome number")

else:
    print("No. given number is not palindrome number")