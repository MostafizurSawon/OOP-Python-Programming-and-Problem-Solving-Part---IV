""" Exercise 7: Return the count of a given substring from a string
Write a program to find how many times substring “Emma” appears in the given string.

Given:

str_x = "Emma is good developer. Emma is a writer"
Expected Output:

Emma appeared 2 times """




def return_count(str):
    count = 0
    string = ""
    for i in range(len(str)):
        if str[i] != " " and str[i] != ".":
            string += str[i]
        
    string = string.lower()
    print(string)
    for j in range(len(string)):
        if string[j] == "e":
            if string[j+1] == "m":
                if string[j+2] == "m":
                    if string[j+3] == "a":
                        count += 1
    return count

str = "Emma is good developer. Emma is a writer"
# print(str)

print(return_count(str))


