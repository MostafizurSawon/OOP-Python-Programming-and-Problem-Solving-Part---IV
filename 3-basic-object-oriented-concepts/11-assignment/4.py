# s = input("Input  : ")
s = "x3b4U5i2"
new = ""

for i,word in enumerate(s):
    if i % 2 == 1:
        len = int(word)
        for j in range(len):
            new += s[i-1]

new = sorted(new, key=str.casefold)
res = ""
for word in new:
    res += word
print("Output :",res)