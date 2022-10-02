print('> player 1: ', end='')
player_1 = input()

print('> player 2: ', end='')
player_2 = input()


""" 
if player_1 == 'rock':
    if player_2 == 'paper':
        print('Player 2 is the winner')
    else:
        print('Player 1 is the winner')

 """
if player_1 == player_2:
    print("> Draw!")

elif (player_2 == 'paper' and player_1 == 'rock') or (player_2 == 'rock' and player_1 == 'scissor') or (player_2 == 'scissor' and player_1 == 'paper'):
    print('> Player 2 is the winner')
    
else:
    print('> Player 1 is the winner')