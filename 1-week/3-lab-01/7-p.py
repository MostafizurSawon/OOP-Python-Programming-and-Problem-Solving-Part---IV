"""  Print characters from a string that are present at an even index number

Write a program to accept a string from the user and display characters that are present at an even index number.

For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’. 
"""

str = "pynative"
n = len(str)
print(n)

for i in range(n):
    if i%2==0:
        print(str[i],end=" ")
