# get the pcap file and export http object to have the data packets

> steps to get the flag :

1 - remove the requests and just have the data packets " data_only.sh script"
2 - rename packets  "renamer.sh will make your life easy"
3 - remove first bit form each file "n=" "remove_bit.sh script"
4 - stick all payload together by : 
```bash
for i in $(seq 0 +4 400) ;do cat $i | tr -d '\n' >> all_payload  ;done
```
5- we need to url decode it before base64 decode it

output is massive no site online will accept it , even replace in the sublime crash 

with bash all is easy bezzy :

```bash
cat all_payload | sed s/'%0A'//g | sed s/'%3D'/'='/g > all_payload_url_decoded
```
6- if we start base64 decode it now will notice the following :

> {"payload": "  
> \n 
> "}

these things are added each time to the output so we will need to remove them frequently 

```bash
cat test | sed s/'\\n'//g | sed s/'{"payload": "'//g | sed s/'"}'//g 
```

7- get flag script will take care of you well ^^ 


# done .
