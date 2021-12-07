<?php 

$input = $_GET['p1'];

$val1= str_replace("'","\'",$input);
$val2= str_replace('\"','\"',$val1);
$val3= str_replace("<","",$val2);
$val4= str_replace(">","",$val3);
$val5= str_replace("{","",$val4);
$val6= str_replace("$","",$val4);

if ( (strpos($val6, "`-alert(") === 0 ) or (strpos($val6,"`-confirm(") === 0) or (strpos($val6, "`-prompt(") === 0))  
{

    if( strrpos($val6, ")//", 0) !== false )
    {
    echo '<script>`'.$val6.'`</script>';
    echo '<center><img src="./img/busted.jpg"><h2>flag{loOks_You_ar3_xSs_mast3r_36eacd0a87f1aeb8ce2dc5429b3bacc9}</h2></center>';     
    }

}

?>