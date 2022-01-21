from hello import hello
from logo import logo
from createplayer import createplayer
from changepwd import newpassword
from bank import bank
from market import market
from buy import buy
from sell import sell

import string
import re
import os

Stay_Up = True
Logged_In = False

hello();
logo();

while Stay_Up == True:

  if Logged_In == False:
    player_name = createplayer();
    Logged_In = True
  else:
    commands = input('What do you want to do? : ')
    
    commands = commands.lower()
    line = ''
    
    for letters in commands:
      for char in string.punctuation:
        letters = letters.replace(char, ' ')
      line = line + letters
    
    commands = line.split()
    count = len(commands)
    if count > 0:
      if commands[0] in 'password':
        newpass = input('Please enter new password : ')
        if re.match("^[a-zA-Z0-9_]*$", newpass) and len(newpass) > 6:
          newpassword(player_name,newpass)
        else:    
          print('Password can only contain at least 7 alphanumeric characters (a-z and 0-9).')
      elif commands[0] in 'bank':
        bank(player_name)
      elif commands[0] in 'market':
        market()
      elif commands[0] in 'buy':
        if count < 2:
          print('Please enter the amount of shares you wish to buy. For e.g. buy 500.')
        else:
          if re.match("^[0-9]*$", commands[1]):
            buy(player_name,commands[1])
          else:
            print('You have not entered a correct amount in numbers to buy.')
      elif commands[0] in 'sell':
        if count < 2:
          print('Please enter the amount of shares you wish to sell. For e.g. sell 500.')
        else:
          if re.match("^[0-9]*$", commands[1]):
            sell(player_name,commands[1])
          else:
            print('You have not entered a correct amount in numbers to sell.')
      elif commands[0] in 'exit':
        os._exit(0)
    else:
      print('Please enter a command or \'exit\' to quit.')
                
            
            
            