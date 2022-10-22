s = "Programming Hero is the best"
s = s.split()
new = ""
len = len(s)

for i,word in enumerate(s):
    if i < len-1:
        new += word[::-1] + " "
    else:
        new += word[::-1]

print(new)