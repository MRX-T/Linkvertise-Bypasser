import random
from colorama import Fore, Back, Style
import requests 
import json
import os

options = ["bypasser.online", "bypasser.link", "thebypasser.com"]

# CMD ekranını temizle 
os.system('cls' if os.name == 'nt' else 'clear')
os.system('title 0x13 URL Bypasser')     
os.system(f'mode con cols=70 lines=30') 


# Yapımcıyı ASCII şeklinde yazdır  
print(Fore.LIGHTCYAN_EX + f"""
         ██████╗ ██╗  ██╗ ██╗██████╗ 
        ██╔═████╗╚██╗██╔╝███║╚════██╗
        ██║██╔██║ ╚███╔╝ ╚██║ █████╔╝
        ████╔╝██║ ██╔██╗  ██║ ╚═══██╗
        ╚██████╔╝██╔╝ ██╗ ██║██████╔╝
         ╚═════╝ ╚═╝  ╚═╝ ╚═╝╚═════╝ 
                             
{Fore.LIGHTYELLOW_EX}Discord:{Fore.LIGHTMAGENTA_EX}0x13#2893
{Fore.LIGHTYELLOW_EX}Git Hub:{Fore.LIGHTMAGENTA_EX}https://github.com/MRX-T
              """)  

                
print(Fore.CYAN + "Linkini bypass etmek istediğiniz bypass yöntemini seçiniz:")

for index, option in enumerate(options):
    print(f"{Fore.YELLOW}{index +1})"  + Fore.GREEN +f" {option}")

choice = int(input(Fore.CYAN + "Seçiminiz: "))

while True: 
    if choice < 1 or choice > len(options):
        print(Fore.RED + f"Lütfen geçerli bir seçim giriniz. {Style.RESET_ALL}")  
        choice = int(input(Fore.CYAN + "Seçiminiz: "))
    else:    
        break
method = options[choice-1] 
os.system('cls' if os.name == 'nt' else 'clear')
url = input(Fore.GREEN + f"Bypass edilecek linki giriniz: {Style.RESET_ALL}")

while True:       
    if url.startswith("http://") or url.startswith("https://"):
        break   
    else:        
       print(Fore.RED + "Lütfen geçerli bir URL giriniz.")
       url = input(Fore.GREEN + f"Bypass edilecek linki tekrar giriniz: {Style.RESET_ALL}")


if method == "bypasser.online":
    url = "https://bypass.pm/bypass2?url=" + url  
elif method == "bypasser.link":
    url = "https://bypass.bot.nu/bypass2?url=" + url
elif method == "thebypasser.com":
    url = "https://bypass.pm/bypass2?url=" + url
else:
    print("Geçersiz seçim.")
    exit()

response = requests.get(url)  
json_response = json.loads(response.text)
destination = json_response["destination"]

print(Fore.BLUE + f"Bypass edilmiş link:{Fore.LIGHTMAGENTA_EX}{destination} {Style.RESET_ALL}")
