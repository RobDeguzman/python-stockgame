import string
import math

def buy(player_name, amount):
  player = ['','','','']
  stock = ['','','']
  player_file = open('players.txt', 'r')
  for player_record in player_file:
    num = 0
    player_record = player_record.rstrip()
    for char in string.punctuation:
      player_record = player_record.replace(char, ' ')
    record = player_record.split()
      
    for fields in record:
      player[num] = fields
      num = num + 1
    stored_name = player[0]
    stored_name = stored_name.lower()
    player_name = player_name.lower()
        
    if stored_name == player_name:
      money_avail = player[2]
      shares_own = player[3]
      break
        
  player_file.close()
    
  stocks_file = open('stocks.txt', 'r')
  for stock_record in stocks_file:
    num = 0
    stock_record = stock_record.rstrip()
    for char in string.punctuation:
      stock_record = stock_record.replace(char, ' ')
    record = stock_record.split()
        
    for fields in record:
      stock[num] = fields
      num = num + 1
        
    stock_name = stock[0]
    stock_pric = stock[1]
    stock_avail = stock[2]

  stocks_file.close()
    
  cost = int(amount) * int(stock_pric)

  if int(amount) > int(stock_avail):
    print('You can\'t buy more than what the market (', stock_avail, ' share(s)) can offer!')
  elif int(cost) > int(money_avail):
    max_amount = math.floor(int(money_avail)/int(stock_pric))
    print('You don\'t have enough gold to buy',amount,'share(s)!')
    print('You can only buy',max_amount,' (max) share(s).')
  else:
    stock_avail = int(stock_avail) - int(amount)
    shares_own = int(shares_own) + int(amount)
    money_avail = int(money_avail) - cost
        
    result = ""
    with open("players.txt") as player_file:
      for player_record in player_file:
        player_record = player_record.rstrip()
        num = 0
        for char in string.punctuation:
          player_record = player_record.replace(char, ' ')
                
        record = player_record.split()
                
        for fields in record:
          player[num] = fields
          num = num + 1
        stored_name = player[0]
        stored_name = stored_name.lower()
        player_name = player_name.lower()
                
        if stored_name == player_name:
          player[2] = str(money_avail)
          player[3] = str(shares_own)
    
          result += str(player) + '\n'
        else:
          result += str(player) + '\n'
    
    player_file = open("players.txt", 'w') 
    player_file.writelines(result)
    player_file.close()    
        
    result = ""
    with open("stocks.txt") as stocks_file:
      for stock_record in stocks_file:
        stock_record = stock_record.rstrip()
        num = 0
        for char in string.punctuation:
          stock_record = stock_record.replace(char, ' ')
                
        record = stock_record.split()
                
        for fields in record:
          stock[num] = fields
          num = num + 1
    
        if stock[0] == 'ABC':
          stock[2] = str(stock_avail)
          result += str(stock) + '\n'
        else:
          result += str(stock) + '\n'
    
    f = open("stocks.txt", 'w') # should be in 'wt or 'w' mode
    f.writelines(result)
    f.close()     
    
    print('You have bought',  amount,  'ABC shares.')