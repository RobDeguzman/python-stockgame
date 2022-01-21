#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 09:49:14 2020

@author: kennethchaw
"""
import string
import random
import math
import time

from tkinter import * 
from GUI_logo import createlogo

player_name = ''
        
def end_main():
    main_window.destroy()
    
def gotogame():
    game_window = Tk()
    game_window.geometry("1050x500")
    game_window.title("In The Game")
    game_window.configure(bg="green", bd="40")
    
    def clear1():
        first_in.delete(first="0", last="100")
        output["text"] = str(" ")
    
    def end_game():
        game_window.destroy()

           
    def message(msg_title, msg):
        messagebox.showinfo(msg_title, msg)
        
    def market():
        if str(first_in.get()) != "" :   
            stock = ['','','']
    
            stock_name = 'ABC'
            stock[0] = stock_name
                
            stock_price = random.randrange(1,10)  
            stock[1] = str(stock_price)
    
            stock_amount = random.randrange(1000,1000000)
            stock[2] = str(stock_amount)
    
            stock_file = open('stocks.txt', 'w')
            stock_file.writelines(str(stock) + '\n')
            stock_file.close()
    
            disp_stock  = '{:7}'.format('{}'.format(str(stock[0])))   
            disp_price = '{:1}'.format('{}'.format(str(stock[1])))     
            disp_avail  = '{:7}'.format('{}'.format(str(stock[2])))     
            
            output["text"] = 'Latest stock market information:\n \
            | Company  : ' + disp_stock + ' | Price per Share : $ ' + disp_price + \
            '.00 | Shares Available : ' + disp_avail + '|'
        else:
            msg_title = 'ERROR!!'
            msg = 'You have not created a new player!'
            message(msg_title, msg)    
          
    def bank():
        if str(first_in.get()) != "" :        
          player=['','','','']
          player_file = open('players.txt','r')
          player_name = str(first_in.get())
        
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
        
              output["text"] = 'Your stock broker returns with the following information:\n \
              | Money  : $' + disp_money + ' | Shares owned : ' + disp_shares + ' |' 
          
              break
            else:
              pass
        
          player_file.close() 
        else:
              
          msg = 'You have not created a new player!'
          message(msg_title, msg)          
        
    def createplayer():

        player=['default','password','1000000','0']
        player_name = str(first_in.get())
      
        if re.match("^[a-zA-Z0-9_]*$", player_name):
          if len(player_name) < 2:
            output["text"] = 'Player name should have at least 2 alphanumeric characters..'
          else:
            player[0] = player_name
            player_file = open('players.txt', 'w')
            player_file.write(str(player) + '\n')
            player_file.close()
        
            output["text"] = 'New player created. Your password is \'' +  str(player[1]) + '\'.\n \
            Enter command \'password\' to change password.\n\n WELCOME ' +  player[0] +  '! YOUR MONEY AWAITS YOU ! \n\n \
            Enter command \'bank\' to view your investments.\n \
            Enter command \'market\' to view the stock market.\n \
            Enter command \'buy\' or \'sell\' to view the stock market.\n \
            Enter command \'exit\' to exit game.'

            firstField = Label(game_window, text='Your player name is:' , padx="3", pady="3", width="20", relief="ridge", bd="2")
            firstField.grid(column="0", row="0")
            msg_title = 'CONGRATULATIONS!!'
            msg = 'Your player \'' + player_name + '\' has been created!'
            message(msg_title, msg)
            
            return player_name
        else:
            output["text"] = 'Player name should not contain special characters or space(s).'  

    def newpassword():
        if str(first_in.get()) != "" :
            pwd_window = Tk()
            pwd_window.geometry("900x200")
            pwd_window.title("Change Password")
            pwd_window.configure(bg="red", bd="40")
    
            def end_pwd():
                pwd_window.destroy()
            
            def changepass():
                player=['','','','']
                result = ''
                with open("players.txt") as player_file:
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
                        pname = str(first_in.get()).lower()
                        
                        if stored_name == pname:    
                            player[1] = str(pwd_in.get())
                            result += str(player) + '\n'
                        else:
                            result += str(player) + '\n'                
            
                f = open("players.txt", 'w') 
                f.writelines(result)
                f.close()
                output["text"] = 'Password changed successfully. Your new password is \'' + str(pwd_in.get()) + '\'.\n \
                Click on \'Quit\' button to close window.'
    
    
            firstField = Label(pwd_window, text="Enter new password :", padx="3", pady="3", width="20", relief="ridge", bd="2")
            #    secondField = Label(game_window, text="Bank Information :", padx="3", pady="3", width="20", relief="ridge", bd="2")
            result = Label(pwd_window, text="Change Status :", padx="3", pady="3", width="20", relief="ridge", bd="2")
            output = Label(pwd_window, bd="2", relief="ridge", padx="70", pady="3", width="50")
                
            pwd_in = Entry(pwd_window, relief="sunken", bd="2")
            click_password = Button(pwd_window, width="20", text="Password", command=changepass)
            end_me = Button(pwd_window, width="20", text="QUIT", command=end_pwd)
                
            firstField.grid(column="0", row="0")
            result.grid(column="0", row="3")
            output.grid(column="1", row="3")
            pwd_in.grid(column="1", row="0")
            click_password.grid(sticky="W", row="10")
            
            output["text"] = 'Your current player name is ' + str(first_in.get())
            
            end_me.grid(sticky="W", row="12")
    
            pwd_window.mainloop()
        else:
            msg_title = 'ERROR!!'
            msg = 'You have not created a new player!'
            message(msg_title, msg)
            
    def buy():
        if str(first_in.get()) != "" :
            buy_window = Tk()
            buy_window.geometry("950x150")
            buy_window.title("Buy Stocks")
            buy_window.configure(bg="yellow", bd="40")
    
            def end_buy():
                buy_window.destroy()
            
            def buynow():
              amount = str(buy_in.get())
              player_name = str(first_in.get())
              
              if re.match("^[0-9]*$", amount):
                  amount = int(amount) 
    
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
                    output["text"] = 'You can\'t buy more than what the market (' + str(stock_avail) + ' share(s)) can offer!'
                  elif int(cost) > int(money_avail):
                    max_amount = math.floor(int(money_avail)/int(stock_pric))
                    output["text"] = 'You don\'t have enough money to buy ' + str(amount) +' share(s)!\n \
                    You can only buy ' + str(max_amount) + ' (max) share(s). Re-enter amount.'
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
                    
                    msg_title = 'CONGRATULATIONS!!'
                    msg = 'You have bought ' + str(amount) + ' ABC shares.'   
                    message(msg_title, msg)
                    
                    end_buy()                         
              else:
                    output["text"] = 'Only numbers are accepted. Try again.'
    
            firstField = Label(buy_window, text="Enter number of stocks to buy :", padx="3", pady="3", width="30", relief="ridge", bd="2")
            result = Label(buy_window, text="Buy Status :", padx="3", pady="3", width="20", relief="ridge", bd="2")
            output = Label(buy_window, bd="2", relief="ridge", padx="70", pady="3", width="50")
                
            buy_in = Entry(buy_window, relief="sunken", bd="2")  
            click_buy = Button(buy_window, padx="3", pady="3", width="20", text="Buy", command=buynow)
                
            firstField.grid(column="0", row="0")
            result.grid(column="0", row="3")
            output.grid(column="1", row="3")
            buy_in.grid(column="1", row="0")
            click_buy.grid(column="1", row="4")
            
            output["text"] = 'Enter the amount of stocks you wish to buy, ' + str(first_in.get()) + '.'
            
            end_me.grid(sticky="W", row="12")
    
            buy_window.mainloop()
        else:
            msg_title = 'ERROR!!'
            msg = 'You have not created a new player!'
            message(msg_title, msg)

    def sell():
        if str(first_in.get()) != "" :
            sell_window = Tk()
            sell_window.geometry("950x150")
            sell_window.title("Sell Stocks")
            sell_window.configure(bg="brown", bd="40")
    
            def end_sell():
                sell_window.destroy()
            
            def sellnow():  
              amount = str(sell_in.get())
              player_name = str(first_in.get())
              
              if re.match("^[0-9]*$", amount):
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
                    
                  profit = int(amount) * int(stock_pric)
                
                  if int(amount) > int(shares_own):
                    output["text"] = 'You can\'t sell more than what you have (' + shares_own + ' share(s)) can offer!'
                  else:
                    shares_own = int(shares_own) - int(amount)
                    stock_avail = int(stock_avail) + int(amount)
                    money_avail = int(money_avail) + profit
                        
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
    
                    msg_title = 'CONGRATULATIONS!!'
                    msg = 'You have sold ' +  str(amount) +  ' ABC shares and made $' + str(profit) + '!'
                    message(msg_title, msg)
                    
                    end_sell()                
            
              else:
                    output["text"] = 'Only numbers are accepted. Try again.'
                    
        
            firstField = Label(sell_window, text="Enter number of stocks to sell :", padx="3", pady="3", width="30", relief="ridge", bd="2")
            result = Label(sell_window, text="Sell Status :", padx="3", pady="3", width="20", relief="ridge", bd="2")
            output = Label(sell_window, bd="2", relief="ridge", padx="70", pady="3", width="50")
                    
            sell_in = Entry(sell_window, relief="sunken", bd="2")  
            click_sell = Button(sell_window, padx="3", pady="3", width="20", text="Sell", command=sellnow)
                    
            firstField.grid(column="0", row="0")
            result.grid(column="0", row="3")
            output.grid(column="1", row="3")
            sell_in.grid(column="1", row="0")
            click_sell.grid(column="1", row="4")
                
            output["text"] = 'Enter the amount of stocks you wish to sell, ' + str(first_in.get()) + '.'
    
            end_me.grid(sticky="W", row="12")
        
            sell_window.mainloop()
        else:
            msg_title = 'ERROR!!'
            msg = 'You have not created a new player!'
            message(msg_title, msg)            

###### BELOW HERE IS WHERE YOU ADD YOUR GUI INTERFACE FOR THE STOCKMARKET GAME ######################

    firstField = Label(game_window, text="Enter Name To Create Player:", padx="3", pady="3", width="20", relief="ridge", bd="2")          
    first_in = Entry(game_window, relief="sunken", bd="2")
    click_createplayer = Button(game_window, width="20", padx="3", pady="3", text="Create Player", command=createplayer)
    click_buy = Button(game_window, width="20", padx="3", pady="3", text="Buy", command=buy)
    click_password = Button(game_window, width="20", padx="3", pady="3", text="Password", command=newpassword)
    click_market = Button(game_window, width="20", padx="3", pady="3", text="Market", command=market)
    click_sell = Button(game_window, width="20", padx="3", pady="3", text="Sell", command=sell)
    click_bank = Button(game_window, width="20", padx="3", pady="3", text="Bank", command=bank)
    clear_me = Button(game_window, width="20", padx="3", pady="3", text="CLEAR", command=clear1)
    end_me = Button(game_window, width="20", padx="3", pady="3", text="QUIT", command=end_game)
    messages = Label(game_window, text="$$$$$$$  Stock Market Messages  $$$$$$$ ", padx="3", pady="3", width="70", relief="ridge", bd="2")
    output = Label(game_window, text="", padx="70", pady="3", width="50", relief="ridge", bd="2")
   
# The following codes defines the locations of each of the above labels, input fields and the buttons on the calculator window
   
    firstField.grid(column="0", row="0")
    first_in.grid(column="1", row="0")
    click_createplayer.grid(column="0", row="1")
    click_buy.grid(column="0", row="2")
    click_password.grid(column="0", row="3")
    click_market.grid(column="0", row="4")
    click_sell.grid(column="1", row="1")
    click_bank.grid(column="1", row="2")
    clear_me.grid(column="1", row="3")
    end_me.grid(column="1", row="4")
    messages.grid(column="2", row="0")
    output.grid(column="2", row="1")
    
##### ABOVE HERE IS WHERE YOU ADD YOUR GUI INTERFACE FOR THE STOCKMARKET GAME #########################    
   
    game_window.mainloop()
    
main_window = Tk()
main_window.geometry("900x900")
main_window.title("The Stock Market Game!")
main_window.configure(bg="blue", bd="40")

container1 = Frame(main_window) 

createlogo(container1)

Label(container1, text="Welcome to the Stock Market Game! You are playing a game that will make you a millionaire!").pack(pady=0)

button1 = Button(container1, text="Create Player", width="20", background="green", command=gotogame).pack(padx="2", pady="2") 
end_me = Button(container1, text="QUIT", width="20", background="red", command=end_main).pack(padx="2", pady="2")


container1.pack(side=TOP, fill=X)
print ('Main window')
main_window.mainloop()