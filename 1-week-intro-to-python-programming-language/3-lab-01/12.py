""" 
Exercise 8: Print the following pattern
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5

solution 1:
for num in range(10):
    for i in range(num):
        print (num, end=" ") #print number
    # new line after each row to display pattern correctly
    print("\n")
    
"""
print("Enter your number: ", end="")
n = int(input())

for i in range(n):
    # print(i)
    for j in range(i):
        print(i, end = " ")
    print("\n")