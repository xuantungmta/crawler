#!/usr/bin/python3
# coding=utf-8

import os
import sys
import time
import datetime
import random
import hashlib
import re
import threading
import json
import getpass
import urllib
import importlib
import http.cookiejar as cookielib
from multiprocessing.pool import ThreadPool
try:
    import mechanize
except ImportError:
    os.system("pip install mechanize")
try:
    import requests
except ImportError:
    os.system("pip install requests")
from requests.exceptions import ConnectionError
from mechanize import Browser

logo = f"""
\033[1;91m┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐\033[1;91m
│ ██████╗██████╗  █████╗ ██╗    ██╗██╗     ███████╗██████╗     ████████╗ ██████╗  ██████╗ ██╗                          │
│██╔════╝██╔══██╗██╔══██╗██║    ██║██║     ██╔════╝██╔══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║                          │
│██║     ██████╔╝███████║██║ █╗ ██║██║     █████╗  ██████╔╝       ██║   ██║   ██║██║   ██║██║                          │
│██║     ██╔══██╗██╔══██║██║███╗██║██║     ██╔══╝  ██╔══██╗       ██║   ██║   ██║██║   ██║██║                          │
│╚██████╗██║  ██║██║  ██║╚███╔███╔╝███████╗███████╗██║  ██║       ██║   ╚██████╔╝╚██████╔╝███████╗                     │
│ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚══════╝╚══════╝╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝                     │
│                                                                                                                      │
│████████╗████████╗     █████╗ ███╗   ██╗███╗   ███╗              ██████╗ ██╗   ██╗ ██████╗ ███╗   ██╗ ██████╗ ██████╗ │
│╚══██╔══╝╚══██╔══╝    ██╔══██╗████╗  ██║████╗ ████║              ██╔══██╗██║   ██║██╔═══██╗████╗  ██║██╔═══██╗██╔══██╗│
│   ██║      ██║       ███████║██╔██╗ ██║██╔████╔██║    █████╗    ██████╔╝██║   ██║██║   ██║██╔██╗ ██║██║   ██║██║  ██║│
│   ██║      ██║       ██╔══██║██║╚██╗██║██║╚██╔╝██║    ╚════╝    ██╔══██╗╚██╗ ██╔╝██║▄▄ ██║██║╚██╗██║██║▄▄ ██║██║  ██║│
│   ██║      ██║       ██║  ██║██║ ╚████║██║ ╚═╝ ██║              ██████╔╝ ╚████╔╝ ╚██████╔╝██║ ╚████║╚██████╔╝██████╔╝│
│   ╚═╝      ╚═╝       ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝     ╚═╝              ╚═════╝   ╚═══╝   ╚══▀▀═╝ ╚═╝  ╚═══╝ ╚══▀▀═╝ ╚═════╝ │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
\033[1;97m╔══════════════════════════════════════════════╗
\033[1;97m║\033[1;93m* \033[1;32mTeam    \033[1;91m:\033[1;93m TT ANM - BVANQD \033[1;97m                  ║
\033[1;97m║\033[1;93m* \033[1;32mRecode  \033[1;91m:\033[1;96m m0lw9re         \033[1;97m                  ║
\033[1;97m╚══════════════════════════════════════════════╝                                                                                                             
"""

if sys.version[0] == '2':
    reload(sys)
    sys.setdefaultencoding("utf-8")

br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [
    ('User-Agent', 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36')]


def loading():
    tiload = ['.   ', '..  ', '... ']
    for o in tiload:
        print("\r\033[1;91m[●] \033[1;92mLoading \033[1;97m"+o),
        sys.stdout.flush()
        time.sleep(1)


def failed():
    print("\033[1;91m[!] Exit")
    os.sys.exit()


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(00000.1)


def menu():
    os.system('clear')
    try:
        fb_token = open('login.txt', 'r').read()
    except IOError:
        os.system('clear')
        print("\033[1;91m[!] Token not found")
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()
    try:
        otw = requests.get(
            'https://graph.facebook.com/me?access_token='+fb_token)
        a = json.loads(otw.text)
        fb_name = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print("\033[1;91m[!] \033[1;93mAccount Checkpoint")
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()
    except requests.exceptions.ConnectionError:
        print("\033[1;91m[!] No connection")
        failed()
    os.system("reset")
    print(logo)
    print("║\033[1;91m[\033[1;96m✓\033[1;91m]\033[1;97m Name \033[1;91m: \033[1;92m"+fb_name+"\033[1;97m")
    print(
        "║\033[1;91m[\033[1;96m✓\033[1;91m]\033[1;97m ID \033[1;91m: \033[1;92m"+id)
    print("\033[1;97m╚"+40*"═")
    print("\033[1;97m║--\033[1;91m> \033[1;92m1.\033[1;97m User information")
    print("\033[1;97m║--\033[1;91m> \033[1;92m2.\033[1;97m Get Id/email/hp")
    print("\033[1;97m║--\033[1;91m> \033[1;92m3.\033[1;97m Hack facebook account")
    print("\033[1;97m║--\033[1;91m> \033[1;92m4.\033[1;97m Bot       ")
    print("\033[1;97m║--\033[1;91m> \033[1;92m5.\033[1;97m Others           ")
    print("\033[1;97m║--\033[1;91m> \033[1;92m6.\033[1;97m Show token           ")
    print("\033[1;97m║--\033[1;91m> \033[1;92m7.\033[1;97m Update           ")
    print("\033[1;97m║--\033[1;91m> \033[1;92m8.\033[1;97m Delete trash          ")
    print("\033[1;97m║--\033[1;91m> \033[1;92m9.\033[1;97m LogOut            ")
    print("\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Exit the programs")
    print("║")
    choices()


def choices():
    pick = input("\033[1;97m╚═\033[1;91m>>> \033[1;97m")
    if pick == "":
        print("\033[1;91m[!] Wrong input")
        choices()
    elif pick == "8":
        os.remove('out')
    elif pick == "9":
        os.system('rm -rf login.txt')
        os.system('xdg-open https://www.facebook.com/rizz.magizz')
        failed()
    elif pick == "0":
        failed()
    else:
        print("\033[1;91m[!] Wrong input")
        choices()


def login():
    os.system('clear')
    try:
        fb_token = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print(logo)
        print('\033[1;91m[☆] \033[1;92mLOGIN AKUN FACEBOOK \033[1;91m[☆]')
        id = input(
            '\033[1;91m[+] \033[1;36mID\033[1;97m|\033[1;96mEmail\033[1;97m \033[1;91m:\033[1;92m ')
        pwd = getpass.getpass(
            '\033[1;91m[+] \033[1;36mPassword \033[1;91m:\033[1;92m ')
        loading()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print("\n\033[1;91m[!] No connection")
            failed()
        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id + \
                    'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + \
                    pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {"api_key": "882a8490361da98702bf97a021ddc14d", "credentials_type": "password", "email": id, "format": "JSON", "generate_machine_id": "1",
                        "generate_session_cookies": "1", "locale": "en_US", "method": "auth.login", "password": pwd, "return_ssl_resources": "0", "v": "1.0"}
                x = hashlib.new("md5")
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = "https://api.facebook.com/restserver.php"
                r = requests.get(url, params=data)
                z = json.loads(r.text)
                pick = open("login.txt", 'w')
                pick.write(z['access_token'])
                pick.close()
                print(
                    '\n\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mLogin successfully')
                menu()
            except requests.exceptions.ConnectionError:
                print("\n\033[1;91m[!] No connection")
                failed()
        if 'checkpoint' in url:
            print("\n\033[1;91m[!] \033[1;93mAccount Checkpoint")
            os.system('rm -rf login.txt')
            time.sleep(1)
            failed()
        else:
            print("\n\033[1;91m[!] Login Failed")
            os.system('rm -rf login.txt')
            time.sleep(0.01)
            login()


def tool_main_function():
    os.system('clear')
    login()


if __name__ == '__main__':
    tool_main_function()
