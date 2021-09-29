# nmap room THM | OSCP studyning 


> export IP=10.10.67.181

# Task 1 

## deployed . 

# Task 2

## What networking constructs are used to direct traffic to the right application on a server?

```
ports
```
## How many of these are available on any network-enabled computer?
 
```
65535
``` 
## [Research] How many of these are considered "well-known"? (These are the "standard" numbers mentioned in the task)

```
1024
```

# Task 3 

## What is the first switch listed in the help menu for a 'Syn Scan' (more on this later!)?

```
-sS
```

## Which switch would you use for a "UDP scan"?
 
```
-sU
``` 
## If you wanted to detect which operating system the target is running on, which switch would you use?
```
-O
``` 

## Nmap provides a switch to detect the version of the services running on the target. What is this switch?
```
-sV
```

## The default output provided by nmap often does not provide enough information for a pentester. How would you increase the verbosity?

```
-v
```

## Verbosity level one is good, but verbosity level two is better! How would you set the verbosity level to two?(Note: it's highly advisable to always use at least this option)
```
-vv
```
## What switch would you use to save the nmap results in three major formats?

```
-oA
```

## What switch would you use to save the nmap results in a "normal" format?

```
-oN
```
## A very useful output format: how would you save results in a "grepable" format?
```
-oG
```

## Sometimes the results we're getting just aren't enough. If we don't care about how loud we are, we can enable "aggressive" mode. This is a shorthand switch that activates service detection, operating system detection, a  traceroute and common script scanning. How would you activate this setting?

```
-A
```
## Nmap offers five levels of "timing" template. These are essentially used to increase the speed your scan runs at. Be  careful though: higher speeds are noisier, and can incur errors! How would you set the timing template to level 5?

```
-t5
```

## How would you tell nmap to only scan port 80?
```
-p80
```
## How would you tell nmap to scan ports 1000-1500?
```
-p 1000-1500
```

## How would you tell nmap to scan all ports?

```
-p-
```
## How would you activate a script from the nmap scripting library (lots more on this later!)?

```
--script
```
## How would you activate all of the scripts in the "vuln" category?
```
--script=vuln*
```

# Task 4 

## read


# Task 5 

```
if Nmap sends a TCP request with the SYN flag set to a closed port, the target server will respond with a TCP packet with the RST (Reset) flag set. By this response, Nmap can establish that the port is closed.

If, however, the request is sent to an open port, the target will respond with a TCP packet with the SYN/ACK flags set. Nmap then marks this port as being open (and completes the handshake by sending back a TCP packet with ACK set).

Many firewalls are configured to simply drop incoming packets. Nmap sends a TCP SYN request, and receives nothing back. This indicates that the port is being protected by a firewall and thus the port is considered to be filtered.
```

## Which RFC defines the appropriate behaviour for the TCP protocol?
```
RFC 793
```
## If a port is closed, which flag should the server send back to indicate this?
```
RST
```

# Task 6 



## There are two other names for a SYN scan, what are they?
```
half-open , stealth
```
## Can Nmap use a SYN scan without Sudo permissions (Y/N)?
```
Y
```

# Task 7 
```
When a packet is sent to an open UDP port, there should be no response. When this happens, Nmap refers to the port as being open|filtered. In other words, it suspects that the port is open, but it could be firewalled. If it gets a UDP response (which is very unusual), then the port is marked as open. 

when a packet is sent to a closed UDP port, the target should respond with an ICMP (ping) packet containing a message that the port is unreachable
```

## if a UDP port doesn't respond to an Nmap scan, what will it be marked as?
```
open|filtered 
```

## When a UDP port is closed, by convention the target should send back a "port unreachable" message. Which protocol would it use to do so?

```
icmp
```


# Task 8 


```
Many firewalls are configured to drop incoming TCP packets to blocked ports which have the SYN flag set (thus blocking new connection initiation requests). By sending requests which do not contain the SYN flag, we effectively bypass this kind of firewall.

NULL scans (-sN) are when the TCP request is sent with no flags set at all. As per the RFC, the target host should respond with a RST if the port is closed.


FIN scans (-sF) work in an almost identical fashion; however, instead of sending a completely empty packet, a request is sent with the FIN flag (usually used to gracefully close an active connection). Once again, Nmap expects a RST if the port is closed.

Xmas scans (-sX) send a malformed TCP packet and expects a RST response for closed ports. It's referred to as an xmas scan as the flags that it sets (PSH, URG and FIN) give it the appearance of a blinking christmas tree when viewed as a packet capture in Wireshark. 


The expected response for open ports with these scans is also identical, and is very similar to that of a UDP scan. If the port is open then there is no response to the malformed packet. Unfortunately (as with open UDP ports), that is also an expected behaviour if the port is protected by a firewall, so NULL, FIN and Xmas scans will only ever identify ports as being open|filtered, closed, or filtered. If a port is identified as filtered with one of these scans then it is usually because the target has responded with an ICMP unreachable packet.

```
## Which of the three shown scan types uses the URG flag?

```
Xmas
```
## Why are NULL, FIN and Xmas scans generally used?

```
firewall evasion
```
## Which common OS may respond to a NULL, FIN or Xmas scan with a RST for every port?
```
Microsoft Windows
```

# Task 9 


##  How would you perform a ping sweep on the 172.16.x.x network (Netmask: 255.255.0.0) using Nmap? (CIDR notation)
```
-sn switch tells Nmap not to scan any ports ,  forcing it to rely primarily on ICMP echo packets (or ARP requests on a local network, if run with sudo or directly as the root user) to identify targets.

```
```
nmap -sn 172.16.0.0/16

```
# Task 10



## What language are NSE scripts written in?

```
Lua
```
## Which category of scripts would be a very bad idea to run in a production environment?
```
intrusive
```
# Task 11

##  What optional argument can the ftp-anon.nse script take?

```
@https://nmap.org/nsedoc/scripts/ftp-anon.html
maxlist 
```

# Task 12


## Search for "smb" scripts in the /usr/share/nmap/scripts/ directory using either of the demonstrated methods. What is the filename of the script which determines the underlying OS of the SMB server?
```bash
$ cat /usr/share/nmap/script.db | grep -i 'smb'

# smb-os-discovery.nse
```
## Read through this script. What does it depend on?

```

smb-brut
```
# Task 13


## Which simple (and frequently relied upon) protocol is often blocked, requiring the use of the -Pn switch?
```
ICMP
```
## [Research] Which Nmap switch allows you to append an arbitrary length of random data to the end of packets?

```
--data-length
```
# Task 14



## Does the target (MACHINE_IP)respond to ICMP (ping) requests (Y/N)?
```
N
```
## Perform an Xmas scan on the first 999 ports of the target -- how many ports are shown to be open or filtered?

```
$ sudo nmap -sX $IP -vvv --top-ports 999 

999
```
## There is a reason given for this -- what is it?
```
no response
```

## Perform a TCP SYN scan on the first 5000 ports of the target -- how many ports are shown to be open? 

```bash
$ sudo nmap -Pn -sS -vvv --top-ports 5000 $IP
#5
```
## Open Wireshark (see Cryillic's Wireshark Room for instructions) and perform a TCP Connect scan against port 80 on the  target, monitoring the results. Make sure you understand what's going on.
```
done
```
## Deploy the ftp-anon script against the box. Can Nmap login successfully to the FTP server on port 21? (Y/N)

```bash
$ sudo nmap -Pn -sS -vvv -p 21 --script=ftp-anon.nse $IP    

# Y

```


# Task 15


## done ^^ 
