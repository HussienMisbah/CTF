all i got is a .pcap file , it was large and i try to anaylze it just find out it uses TFTP protocol .

i tried to follow a udp stream and just figured it looks like a .tar.gz file .

## wireshark :

we can get a benifit from file > export > TFTP 

![1-3](https://user-images.githubusercontent.com/67979878/126604418-3adc8149-fd09-47e8-960d-970add62933f.PNG)

now we can download it all and see what is going on :

instructions.txt :

TFTPDOESNTENCRYPTOURTRAFFICSOWEMUSTDISGUISEOURFLAGTRANSFER.FIGUREOUTAWAYTOHIDETHEFLAGANDIWILLCHECKBACKFORTHEPLAN


plan.txt

GSGCQBRFAGRAPELCGBHEGENSSVPFBJRZHFGQVFTHVFRBHESYNTGENAFSRE.SVTHERBHGNJNLGBUVQRGURSYNTNAQVJVYYPURPXONPXSBEGURCYNA

seems encryptrd in base64 , However it is not :) it is a ROT13 !

plan / I USED THE PROGRAM AND HID IT WITH- "DUEDILIGENCE". CHECKOUT THE PHOTOS

instructions/TFTP DOESNT ENCRYPT OUR TRAFFIC SO WE MUST DISGUISE OUR FLAG TRANSFER. FIGURE OUT A WAY TO HIDE THE FLAG AND I WILL CHECK BACK FOR THE PLAN

`$steghide extract -sf picture3.bmp `

now you will find flag.txt

