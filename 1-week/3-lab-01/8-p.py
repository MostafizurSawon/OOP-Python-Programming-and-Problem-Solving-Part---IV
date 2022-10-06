""" 
Excercise: 4
Remove first n characters from a string
Write a program to remove characters from a string starting from zero up to n and return a new string.

For example:

remove_chars("pynative", 4) so output must be tive. Here we need to remove first four characters from a string.
remove_chars("pynative", 2) so output must be native. Here we need to remove first two characters from a string.

def remove_chars(word, n):
    print('Original string:', word)
    x = word[n:]
    return x

print("Removing characters from a string")
print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))
 """


# remove_char("pynative", 4)
data = "pynative"
len = len(data)
print("type how many characters to remove: ",end=" ")
n = int(input())

new_data = ""
for i in range(n,len):
    new_data += data[i]

print(new_data)

