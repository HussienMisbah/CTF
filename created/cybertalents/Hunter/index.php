<!DOCTYPE html>
<?php
setcookie("flag","who_has_gohn_cookie",time() + (86400 * 30), "/");
setcookie("Ging_Freecss", base64_encode(base64_encode(base64_encode(base64_encode(base64_encode("try harder Gon!"))))), time() + (86400 * 30), "/");
setcookie("Hisoka", "6920616d206a7573742061207761737465206f662074696d65206a6f686e205e5f5e" , time() + (86400 * 30), "/");
setcookie("Killua", "pbbxvr_vf_jvgu_gur_rknzvare_Tbua" , time() + (86400 * 30), "/");
?> 
<html lang="en">

<head>
    <title>searching</title>
</head>

<body style="background-color:black;">



    <?php 
        if ( strtolower($_COOKIE["flag"]) === "satotz")
        {

               echo '<img src="./img/solution.gif" width="1000" height="600" style="position:relative; left:450px;" />';
               echo '<h1 style="color:white"><center>flag{Always_Trust_Your_Fr13nds}</center></h1>';
        }
        else 
        {
            echo '<h2 style="color: green;"><center>I WANT MY COOKIE !!</center></h2>';
            echo '<img src="./img/gohn.jfif" width="1000" height="600" style="position:relative; left:450px;" />';
            echo '<h2 style="color: red;"><center>:Follow me and stay focused. If you are deceived, you are dead</center></h2>';

        }

    ?>
 
</body>

</html>
