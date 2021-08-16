# 16 AUG 2021

## category | digital forensics

![Anubis_Cover](https://user-images.githubusercontent.com/67979878/129636371-e5b0b463-ce75-45be-98e4-fd8b82931e9d.jpg)

challenge link : https://drive.google.com/file/d/1GMF9IgpfDxKfzbJ5TCjUNsdTRm7Eamzr/view?fbclid=IwAR2L03osXYPsrI_E5ZMkspkFjzLNedLSxqlJj2FarpSspHn_hd_96GIwlT0

it is a pcapng file so let's check it with wireshark :) 

there are some hints on the packet comments maybe help 

after some investeagting , found that it is a simple http server running on a file has a .rar file and another device connected to it and get it 

you can see that here 

![image](https://user-images.githubusercontent.com/67979878/129635277-3332e257-51a9-4f8d-98da-24cb421ecfa7.png)


let's get this rar !

file > exportObjects > HTTPs

![image](https://user-images.githubusercontent.com/67979878/129635552-6fe50c91-8a7b-4960-8026-75f897dc17a6.png)

we can extract it easily without password 

found :

![image](https://user-images.githubusercontent.com/67979878/129635696-032db5c4-ce1b-4949-a8b3-5768bccaf062.png)


the jpg seemed a rabbit hole i tried stegseek and some steganography extraction techniques but with no promising lead :( 

let's focus on the .apk  

i have no experince on the mobile applications pentesting but let's see my luck there ;) 

after some searching find that a .apk file can be extracted so i simply `unzip anubuis.apk`  found alot of files 

there are alot of ways to deal with the apk file like mount it on  a .apk player or on an android environment or other emulating apps for windows and kali 

however that is what i did :

- i know start of the flag : 'Flag' 
- let's search for it :) and see my luck
- ` grep -ri "flag" .`  r : recursively on all files , i for case senstive 
- 
![image](https://user-images.githubusercontent.com/67979878/129636189-de5dec20-0fc8-4bbd-bc06-611ec25811b7.png)



![image](https://user-images.githubusercontent.com/67979878/129636284-185041b9-8d60-4b2f-907b-49cc4736dc75.png)


# done
























