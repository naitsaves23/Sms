"""

Author:Gheris :)

"""
#!/usr/bin/python3
from pystyle import Colors, Colorate, Write #pip install pystyle
import requests # pip install requests
import os
from colorama import init, Fore # pip install colorama


os.system('cls' if os.name == 'nt' else 'clear')

# colors
init()
GREEN = Fore.GREEN
RED = Fore.RED
print("ponga el numero gay cacorro")
def main():
    phone = int(Write.Input("[*] Enter number of the victim : ",Colors.red))
    print(f">>> {phone}")
    message = Write.Input("[*] ENTER YOUR MSG :",Colors.blue)
    print(f">>> {message}")
    resp = requests.post('https://textbelt.com/text', {
    'phone': f'{phone}',
    'message': f'{message}',
    'key': 'textbelt',
    })
    print("\n")
    print(f"{GREEN} {resp.json()}")


if __name__ == "__main__":
    main()
