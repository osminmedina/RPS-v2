print('Welcome to Rock Paper Scissors! ')
print('Rock...')
print('Paper...')
print('Scissors...')

player1 = input('Player One, what do you choose? ')
print('*** NO CHEATING!!\n\n' * 20)
player2 = input('Player Two, what do you choose? ')

if player1 == player2:
  print('It is a tie! ')
elif player1 == 'rock':
  if player2 == 'scissors':
    print('player1 wins! ')
  elif player2 =='paper':
    print('player2 wins! ')
elif player1 == 'paper':
  if player2 == 'rock':
    print('player1 wins! ')
  elif player2 == 'scissors':
    print('player2 wins! ')
elif player1 == 'scissors':
  if player2 == 'rock':
    print('player2 wins! ')
  elif player2 == 'paper':
     print('player1 wins! ')
else:
  print('something terrible went wrong ): ')