import re

def createplayer():
  IsCreated = False
  player=['default','password','1000000','0']
  
  while IsCreated == False:
    player_name = input('Enter your name to create player : ')
    if re.match("^[a-zA-Z0-9_]*$", player_name):
      if len(player_name) < 2:
        print('Player name should have at least 2 alphanumeric characters..')
      else:
        player[0] = player_name
        player_file = open('players.txt', 'a')
        player_file.write(str(player) + '\n')
        player_file.close()

        print('New player created. Your password is \'',  str(player[1]), '\'.')
        print('Use the command \'password\' to change password.\n')              
        print('\nWelcome',  player[0],  '! Your money awaits you ! \n')
        print('Use the command \'bank\' to view your investments.')
        print('Use the command \'market\' to view the stock market.')
        print('Use the command \'buy\' or \'sell\' to view the stock market.')
        print('User the command \'exit\' to exit game.')
        IsCreated = True  
        return player_name
    else:
        print('Player name should not contain special characters or space(s).')


