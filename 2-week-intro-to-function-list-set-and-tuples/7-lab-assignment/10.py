import re

a = ['oh', 'Emelia', 'to']

s = "Oh, I got two tickets for Dhaka. I and Emelia love to visit different places very much. This time we are going to Bangladesh."

def create_new_string(a, s):
    new = ""
    s = s.replace('.', '')
    s = re.split(', | ', s)
    # print(s)
    for word in a:
        # print(word)
        # print(len(s))
        for i in range(len(s)):
            if word.lower() == s[i].lower() and s[i+1] != "visit":
                new += s[i+1]
                new += " "
                i+=1
    with open('out.txt', 'w') as output:
        output.write(new)
        print("Your result is at './out.txt'")

create_new_string(a, s)