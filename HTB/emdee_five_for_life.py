#!/usr/bin/python

import hashlib
import requests
import re 
"""
task : 
1- extract the string <h3 align='center'>ALNYaFCln6by5kakiLFM</h3>
2- then make md5    -> hashlib.md5("whatever your string is").hexdigest()
3- then submit it to the page 
"""
url = 'http://68.183.41.74:32575/'
cookie = {"PHPSESSID":"ifugm96e0049gtnf1rnov5pk96"}

# start a session hence we will send more than 1 request .
r = requests.Session()
# first get intial string 
s= r.get(url,cookies=cookie)
content = s.content.decode('utf-8')

# [1] extract the string 
m = re.search("<h3 align='center'>(.+?)</h3>",content)
string = m.group(1)
print(f"[+] string to hash {string}")

# [2] hash it
hash_value = hashlib.md5(string.encode('utf-8')).hexdigest()
print(f"[+] hashed value :{hash_value}")
parmas = { 'hash': hash_value }

# [3] post the hash 
# note : data is for post requests and params are used when get request is made .
while  True :
	s =r.post(url=url,cookies=cookie,data=parmas)
	flag = re.search("<p align='center'>(.+?)</p>",s.text).group(1)
	if flag[:3] == "HTB" :
		break 

print(f"[+] flag is :{flag}")
