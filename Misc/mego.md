
# cybertalents | Egypt national ctf | 09 OCT 2021 | MEGO | medium | 100 pts


description :
```
Mego has something at the Desktop however he leaves his secret on cloud
```


we have a memory dump so first :

```bash
python2 ~/tools/volatility/vol.py -f memdump.mem  imageinfo
```
output :
```bash
Suggested Profile(s) : Win7SP1x64, Win7SP0x64,.  ..  
```


```bash
python2 ~/tools/volatility/vol.py -f memdump.mem --profile=Win7SP1x64 filescan | grep -i "flag"

Volatility Foundation Volatility Framework 2.6.1
0x0000000050dc4370     16      0 RW---- \Device\HarddiskVolume2\Users\admin\Downloads\flag.txt.zip
0x0000000051c31070     16      0 -W-r-- \Device\HarddiskVolume2\Users\admin\AppData\Local\Temp\VirtualBox Dropped Files\2021-06-28T00_22_19.499460900Z\flag.txt.zip
0x000000005f7c64c0     16      0 RW-rw- \Device\HarddiskVolume2\Users\admin\AppData\Roaming\Microsoft\Windows\Recent\flag.txt.lnk
0x000000005fd82710     16      0 RW-rw- \Device\HarddiskVolume2\Users\admin\AppData\Roaming\Microsoft\Windows\Recent\flag.txt (2).lnk
                                                                                                                                             
````

we can dump the flag.txt.zip file :

```bash
python2 ~/tools/volatility/vol.py -f memdump.mem --profile=Win7SP1x64 dumpfiles -Q 0x0000000050dc4370 --name file -D .

```
we can see :

```bash
file flag.zip                                     

flag.zip: Zip archive data, at least v5.1 to extract
```

> But it needs a password , tried to crack it with john but failed , remember the description ?

```bash
python2 ~/tools/volatility/vol.py -f memdump.mem --profile=Win7SP1x64 iehistory 

```

in the output this part keep appearing :
```bash
Record length: 0x480
Location: Visited: admin@https://www.google.com/search?hl=ar-AE&source=hp&q=aHR0cHM6Ly9naXN0LmdpdGh1Yi5jb20vZWd5Y29uZG9yL2VlYTQyZWZkY2M4YWZmZjZlY2E3ODllZmFkMDkyNGY0&btnG=%D8%A8%D8%AD%D8%AB+Google%E2%80%8F&iflsig=AINFCbYAAAAAYNklB-nHZ11BsWPswjKaNT4sXGZcL73d&gbv=1
Last modified: 2021-06-28 00:25:40 UTC+0000


```

```bash
echo "aHR0cHM6Ly9naXN0LmdpdGh1Yi5jb20vZWd5Y29uZG9yL2VlYTQyZWZkY2M4YWZmZjZlY2E3ODllZmFkMDkyNGY0" | base64 -d
https://gist.github.com/egycondor/eea42efdcc8afff6eca789efad0924f4      
```
we can see the link is a big worldlist of passwords , we can crack now 

```bash
zip2john flag.zip | tee hash_ctf
john --wordlist=pass.txt hash_ctf

```
output :
```bash
zipal.zip/flag.txt:g=ax6w{JPtHL./FdE&8ASVbu$rcmG?zZ:flag.txt:zipal.zip:zipal.zip

```
now we can extract it and see the flag :

```
flag{FF571983C5693A57024858E6529A7408D16791846918}

```
