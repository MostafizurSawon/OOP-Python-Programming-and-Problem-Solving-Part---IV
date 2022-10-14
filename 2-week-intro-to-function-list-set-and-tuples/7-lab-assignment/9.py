# import re

s = "I am the chief of Baghdad. Before that I used to be a superintendent of Bank Asia. Things have changed a lot since Jorina married me. A lot of girls tried to marry me."

# s=re.split(r'[," "!.]', s)

replace_with = ["chief", "thief", "superintendent", "sweeper", "married", "left", "tried", "died"]

def replace_word():
    new=s
    for i in range(0,len(replace_with),2):
        # print(replace_with[i])
        new = new.replace(replace_with[i], replace_with[i+1])

    print(new)

replace_word()