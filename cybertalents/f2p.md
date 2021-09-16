**F2up challenge**

Prerequisites & Requirements :

- understanding of SSRF

What will you learn?

- wget File Upload/SSRF exploit

Description

this is the most secure way to file upload is it ?

**Discovery**

We can see it accepts an image url and display it in the page let’s try intercept the request and see what is going on

![Aspose Words 6d8517ca-87bb-4179-ae64-f4a03f9da6be 001](https://user-images.githubusercontent.com/67979878/133670443-8e1a13f7-73ee-4580-9c56-cdc4bc2040d5.jpeg)

- We can see that in the request uses a POST method  to /wget.php with a parameter url
- Response :

![Aspose Words 6d8517ca-87bb-4179-ae64-f4a03f9da6be 002](https://user-images.githubusercontent.com/67979878/133670556-35c176b5-532e-4fc3-9337-0d4e27ce25d0.png)

Let’s visit it  :


http://ec2-35-158-236-11.eu-central-1.compute.amazonaws.com/f2up/images/g7Jo79Dh_400x400.jpg


We can see our photo has been uploaded successfully

![Aspose Words 6d8517ca-87bb-4179-ae64-f4a03f9da6be 003](https://user-images.githubusercontent.com/67979878/133670582-53b06ec4-cbfb-4092-a098-5366f402260e.jpeg)

**Exploitation**

Hence it has a parameter url which will fetch the image it looks like a ssrf environment

- Let’s try uploading a simple php code enabling RCE
- We can use pastebin or github to host our simple code :

![Aspose Words 6d8517ca-87bb-4179-ae64-f4a03f9da6be 004](https://user-images.githubusercontent.com/67979878/133670675-aa05a9e0-5bb0-4c7d-8cf0-1a8c17cc65b9.png)

- Let’s pass this url to url parameter in the page and see response :

![Aspose Words 6d8517ca-87bb-4179-ae64-f4a03f9da6be 005](https://user-images.githubusercontent.com/67979878/133670697-12599303-5c39-4e06-8709-98ef9d3afa57.png)

- We know this url fetches the data with wget and it checks if this is an image , we can use  wget File Upload/SSRF Trick . which exactly achieves our purpose .
- Check : <https://book.hacktricks.xyz/pentesting-web/file-upload#wget-file-upload-ssrf-trick>
- Note : you may need to change the character multiplied by 232 due to other talents' uploaded payloads .

![Aspose Words 6d8517ca-87bb-4179-ae64-f4a03f9da6be 006](https://user-images.githubusercontent.com/67979878/133670722-1d27b101-01a1-4b9d-903b-8c2f413472bb.png)


- We can use github to upload the file or setting ngrok http server which I will use to monitor logs and requests .
```bash
$./ngrok http 1234
$python3 -m http.server 1234   “ on file directory”
```
- File has been uploaded successfully !

![Aspose Words 6d8517ca-87bb-4179-ae64-f4a03f9da6be 008](https://user-images.githubusercontent.com/67979878/133670827-1e104aa6-607b-44d4-ae3a-ee6aabc2481a.jpeg)

- Monitoring our ngrok http server we can see a request is made

![Aspose Words 6d8517ca-87bb-4179-ae64-f4a03f9da6be 009](https://user-images.githubusercontent.com/67979878/133670846-ad91d9d5-116b-4b5a-b7df-ee43563db5ba.png)

- Now we have a RCE which can be used by requesting our uploaded payload and sending the commands in the cmd parameter .

![Aspose Words 6d8517ca-87bb-4179-ae64-f4a03f9da6be 010](https://user-images.githubusercontent.com/67979878/133670872-788dc3f7-5882-441e-8929-83c05c7fc293.jpeg)
