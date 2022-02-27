import requests
import time
import colorama
from colorama import *
init()


with open('usernames.txt', 'r', encoding='UTF-8', errors='replace') as u:
    usernames = u.read().splitlines()
    all_usernames = len(usernames)
    if all_usernames == 0:
        print(f'{Fore.LIGHTRED_EX} [!] No usernames found!\n Make sure to paste them into usernames.txt and save.{Fore.RESET}')
        quit()



def banner():
    print(f'''{Fore.LIGHTCYAN_EX}
   _____       _       _                    
  / ____|     | |     | |                   
 | (___   ___ | | ___ | |_ ___              
  \___ \ / _ \| |/ _ \| __/ _ \             
  ____) | (_) | | (_) | || (_) |            
 |_____/_\___/|_|\___(_)__\___/             
       / ____| |             | |            
      | |    | |__   ___  ___| | _____ _ __ 
      | |    | '_ \ / _ \/ __| |/ / _ \ '__|
      | |____| | | |  __/ (__|   <  __/ |   
       \_____|_| |_|\___|\___|_|\_\___|_|   {Fore.RESET}
    ''')



def check():
    while True:

        for username in usernames:
            r = requests.get(f"https://www.solo.to/{username}", headers={'Connection': 'keep-alive', 'User-Agent': 'TikTok 17.4.0 rv:174014 (iPhone; iOS 13.6.1; sv_SE) Cronet'}, timeout=60)
            check = r.status_code
            if check == 404:
                print(f" [ {Fore.LIGHTGREEN_EX}+{Fore.RESET} ] Username: {username} Available")
                with open('available.txt', "a") as f:
                    f.write(f"{username}\n")

            elif check == 200 or 204:
                print(f" [ {Fore.LIGHTRED_EX}-{Fore.RESET} ] Username: {username} Taken")

            elif check == 429:
                print(f" [ {Fore.YELLOW}!{Fore.RESET} ] Rate Limited, Waiting 30 Seconds to Complete")
                time.sleep(30)
            else:
                pass



banner()
check()



        