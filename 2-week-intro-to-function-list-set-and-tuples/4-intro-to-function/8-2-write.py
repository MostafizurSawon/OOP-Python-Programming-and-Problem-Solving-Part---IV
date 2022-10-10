with open('message.txt', 'a') as fileWrite:
    fileWrite.write("\nWe will go furtherrr!")

with open('message.txt', 'r') as fileRead:
    text = fileRead.read()
    print(text)