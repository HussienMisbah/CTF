the site doesn't seem to have parameters to playaround or input section . 
reviewing /robots.txt file found :

![image](https://user-images.githubusercontent.com/67979878/130718104-754ae93c-0b0b-4845-a5d1-473c9c14dd71.png)



`/s3cret.php`

![image](https://user-images.githubusercontent.com/67979878/130718153-b8a7a516-60dd-4241-9b69-00dde5e700fb.png)

so it needs a password. hmmm 

`/source.php`


````php

<?php


include('flag.php');

$password=$_POST['pass'];

if (strpos( $password, 'R_4r3@')!== FALSE){
    
    if (!preg_match('/^-?[a-z0-9]+$/m', $password)) {
    
        die('ILLEGAL CHARACTERS');
  
        }
echo $cipher;
    }
else 
{
    echo 'Wrong Password';
    }

?>
````

so the password must contain 'R_4r3@' however it must be form a-z,0-9 in the `preg_match` regex 

searching how to pypass this regex in preg_match 

![image](https://user-images.githubusercontent.com/67979878/130718264-c4e04916-d823-4a8b-80ae-065d1eb85a36.png)


try : `junk%0AR_4r3@`


####  note |when i try it in the page it doesn't work however worked in burpsuite :

![image](https://user-images.githubusercontent.com/67979878/130718654-e485d062-48db-4b85-9e3b-b15d938f4f40.png)

this is Brain FUCk code 
 
use :https://www.dcode.fr/brainfuck-language


![image](https://user-images.githubusercontent.com/67979878/130718826-87dcf3b3-8846-4651-ab98-75d950e06a11.png)




# done









