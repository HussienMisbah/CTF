## 2 SEP 2021 | cybertalents


# 1- one click | 25 pts
``` 
-Type of malicious exploit of a website where unauthorized commands are submitted from a user that the web application trusts .
CSRF
```

# 2- where is the flag | 50 pts
```
in page source code :
Can you see the flag
	VGgzRmxhZzFzSDNyM0JyMA%3D%3D
  
it is base64 encoded let's decode it :
echo "VGgzRmxhZzFzSDNyM0JyMA==" | base64 -d
flag :Th3Flag1sH3r3Br0   
```

# 3- catch toka  | 50 pts
![image](https://user-images.githubusercontent.com/67979878/131999513-d567d9fc-d47d-4071-b7ff-e422ae78a903.png)

```
- try to modify request by : X-Forwarded-For: german_ip  but doesn't work 
- then i changed Accept language header to german hence it only talks german xD 
  check :https://www.websitepulse.com/kb/http_accept_language
  so in request : Accept-Language: de
```
![image](https://user-images.githubusercontent.com/67979878/132000126-f6c6f56a-a6e3-4ee7-b785-ebef8da38300.png)

# 4- wanna some biscuits | 50 pts 

![image](https://user-images.githubusercontent.com/67979878/132000336-77588af6-8497-48bc-a1f5-7d04e1443bd5.png)

```
source code doesn't contain any thing helpful however we have a cookie !
```
![image](https://user-images.githubusercontent.com/67979878/132000466-423f1156-2d82-4bd3-9b26-3fba151f4db6.png)


```
looks like insecure deserialization :D , let's modify these values (username, isAdmin)

O:4:"User":2:{s:8:"userName";s:9:"anonymous";s:7:"isAdmin";b:0;}

to

O:4:"User":2:{s:8:"userName";s:5:"admin";s:7:"isAdmin";b:1;}
```
![image](https://user-images.githubusercontent.com/67979878/132000676-4e983b9a-7367-4140-b176-270883a20b94.png)


# 5- Pasta Code | 100 pts

```
when visit it will get restricted port to open hence it runs on port 6000

great link to bypass :https://www.specialagentsqueaky.com/blog-post/r5iwj96j/2012-02-20-how-to-remove-firefoxs-this-address-is-restricted/

```

![image](https://user-images.githubusercontent.com/67979878/132001325-2f804a8d-0f0e-498d-8dae-c436c1f53e7f.png)

```
register and login with your credits you will notice a JWT in request 

eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFkbWluMiJ9.xh8kwc0iNg97vgw9JTENTIpvrw_JrPrYyuLbwz0ax6A

let's bruteforce it and get our secret !

```
![image](https://user-images.githubusercontent.com/67979878/132001884-84457cb9-44cb-4dbc-8853-7832afeb32ef.png)
![image](https://user-images.githubusercontent.com/67979878/132001978-746b2d5f-4667-4a9d-a1d4-38e5b71ef086.png)

```
moidfying JWT value will reveal the flag 
```

# 6- Notes | 100 pts




# 7- grocery bot | 200 pts
