import string

def bank(player_name):
    
  player=['','','','']
  player_file = open('players.txt','r')

  for player_record in player_file:
    num = 0
    player_record = player_record.rstrip()       
    for char in string.punctuation:
      player_record = player_record.replace(char,' ')
    record = player_record.split()

    for fields in record:
      player[num] = fields
      num = num + 1
            
    stored_name = player[0]
    stored_name = stored_name.lower()
    player_name = player_name.lower()

    if stored_name == player_name:
      disp_money =  '{:7}'.format('{}'.format(str(player[2]))) 
      disp_shares = '{:7}'.format('{}'.format(str(player[3])))

      print('Your stock broker returns with the following information: ')                
      print('| Money  : $', disp_money, ' | Shares owned : ', disp_shares, ' |') 
  
      break
    else:
      pass

  player_file.close()