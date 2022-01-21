import random

def market():
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
    
  print('Latest stock market information: ')
  print('| Company  :', disp_stock, ' | Price per Share : $', disp_price, \
  '.00 | Shares Available :', disp_avail, '|') 