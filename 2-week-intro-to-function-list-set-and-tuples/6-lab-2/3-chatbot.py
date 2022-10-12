""" 
Chatbot

steps:
1. input/listen
2. process/decide
3. output/talkback
 """
greet_words = ['hi','hello','yoo', 'hey']
bye_words = ['bye','tata','hasta-la-vista']
bad_words = ['dog', 'pocha']

def listen():
    return input(">> ")

def decide(command):
    # print(">>",command)
    command = command.lower()
    broken_words = command.split(" ")
    # print(broken_words)

    for word in broken_words:
        if word in greet_words:
            talkback("Hey, Man!")
            break
        
        elif word in bye_words:
            talkback("Tata bye bye.")
            break

        elif word in bad_words:
            talkback("Behave yourself!!")
            break


def talkback(res):
    print(">> ",res)

while True:
    command = listen()
    # print(command)
    decide(command)

