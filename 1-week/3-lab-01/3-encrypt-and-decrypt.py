# data = "firebaby"

data = "firebaby"
shift = 3
output = ''

for char in data:
    output += chr((ord(char)+shift-97)%26+97)

print(output)