[*] This challenge is my first challenge ever in the cyber security field so i am really excited about it :)

[*]Analyzing source code

After anaylzing the page source code i have found the js script as follows :
```
var _0xae5b=         
["\x76\x61\x6C\x75\x65",
"\x75\x73\x65\x72",
"\x67\x65\x74\x45\x6C\x65\x6D\x65\x6E\x74\x42\x79\x49\x64",
"\x70\x61\x73\x73",
"\x43\x79\x62\x65\x72\x2d\x54\x61\x6c\x65\x6e\x74",     
"\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x43\x6F\x6E\x67\x72\x61\x74\x7A\x20\x0A\x0A", 
"\x77\x72\x6F\x6E\x67\x20\x50\x61\x73\x73\x77\x6F\x72\x64"]; 
```
the previous block defines array _0xae5b with 7 elemnts .

[*]hex to text converter :

value,user,getElementById,pass,Cyber-Talent,Congratz,wrong Password
```
function check(){
var _0xeb80x2=document[_0xae5b[2]](_0xae5b[1])[_0xae5b[0]];
var _0xeb80x3=document[_0xae5b[2]](_0xae5b[3])[_0xae5b[0]];

```
this blocks store the user in _0xeb80x2 

and the pass in _0xeb80x3

```
if(_0xeb80x2==_0xae5b[4] && _0xeb80x3==_0xae5b[4])        
{alert(_0xae5b[5]);}     
else {alert(_0xae5b[6]);}  
}

```
we know the following :

|_0xae5b[4] |  Cyber-Talent |

|_0xae5b[5] | Congratz |

|_0xae5b[6] | wrong password |

so this blocks checks if user = Cyber-Talent && pass = Cyber-Talent then will execute the alert printing Congratz

else will get us a wrongpassword alert 

After logging in with the user and pass Cyber-Talent , you will get an alert  with the flag .


