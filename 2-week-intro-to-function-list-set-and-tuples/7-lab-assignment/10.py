import re

a = ['oh', 'Emelia', 'to']

s = "Oh, I got two tickets for Dhaka. I and Emelia love to visit different places very much. This time we are going to Bangladesh."

def create_new_string(a, s):
    new = ""
    split_str = re.split('; |, | ', s)
    split_sent = re.split('. ', s)
    for word in a:
        for j in range(len(split_str)):
            if word.lower() == split_str[j].lower():
                new += split_str[j+1]
                new += " "
                j+=1
    with open('out.txt', 'w') as f:
        f.write(new)


create_new_string(a, s)