notes:
```
In order for a CSRF attack to be possible:
- A relevant action - email change functionality
- Cookie based session handling - session cookie
- No unpredictable request parameters - ex:csrf_token . satisfied here

Testing CSRF Tokens:
---------------------
1. Remove the CSRF token and see if application accepts request
2. Change the request method from POST to GET
3. See if csrf token is tied to user session

Testing CSRF Tokens and CSRF cookies:
--------------------------------------------
1. Check if the CSRF token is tied to the CSRF cookie
   - Submit an invalid CSRF token
   - Submit a valid CSRF token from another user
2. Submit valid CSRF token and cookie from another user

In order to exploit this vulnerability, we need to perform 2 things:
---------------------------------------------------------------------
1. Inject a csrfKey cookie in the user's session (HTTP Header injection) - satisfied
2. Send a CSRF attack to the victim with a known csrf token


Testing Referer header for CSRF attacks:
------------------------------------------
1. Remove the Referer header
2. Check which portion of the referrer header is the application validating

```


# [1] CSRF vulnerability with no defenses

----------------------------------------

- we can make the html payload with burpsuite pro edition 
Engament tools > "CSRF POC" option ,or we can do it our selves ,you can check the payload in the /labs file .

- all the idea that we host the code on a server and when the victim is logged in at the targeted website we can now change his email associated while he doesn't know only be visiting our link .

- Could lead to account take over or doing actions weren't intended by the user  




# [2] CSRF where token validation depends on request method

--------------------------------------------------------

- this time we can see in the post request while changing the email 

```bash

email=test5%40test.caaffa&csrf=fLSqGT0NVimplk3yvxYaSaZ99KpMEPTu

```
there is a csrf parameter is sent with a radnom value , if we try to set it as empty or put random value we got 

```bash

"Invalid CSRF token"

```
- changing request method to GET and ignoring the csrf parameter return ``302 found`` so working on same previous payload and changing request to GET solved the issue :) 


# [3] CSRF where token validation depends on token being present

-----------------------------------------------------------

we can also see the same parameters are sent :
```bash
email=test5%40test.caaffa&csrf=fLSqGT0NVimplk3yvxYaSaZ99KpMEPTu
```

However when i removed the csrf token it was accepted so i used same lab01.html paylaod 



# [4] CSRF where token is not tied to user session

------------------------------------------------

- we can see in the request :
```bash

email=test%40testers.com&csrf=1b1sCz9anKw5ntyktgAUEr2YgpPWcEXA

```

- same as last 2 labs , however when i tried to remove csrf param from POST or GET i got "csrf missed" or "not found" in POST
  and GET requests respctively .

- **behavior noticed :** with every request a new csrf is generated so we have to make a reqeust , get the csrf , drop it so it still be valid .


- we have 2 accounts , we can see each one has his one csrf_token , trying to use csrf_1 for account_2 and it returns 
``302 found`` so a hacker can make an account and set his csrf_token to replace the user's and make same as previous techinque .

wiener:peter
carlos:montoya

consider wiener is the hacker , carlos is the victim  .
 
- using wiener csrf token we take and drop reqeust , re-use it in the html payload , worked ! 
- so session is not tied to the csrf token .

- check /labs/lab04.html



# [5] CSRF where token is tied to non-session cookie
-----------------------------------------------------

in the request we can see :

```bash

Cookie: session=IqAZdzeu6CvRHCAtQIhpmlKscegPOXA1; csrfKey=f6juWPCiJJuRZqslAP15Z9giRpgYibzs
Upgrade-Insecure-Requests: 1

email=test%40tester&csrf=IEhLfNjY2rlIehD1sZEAUFjifQiTpX3z

```
wiener :hacker
carlos :victim 

tried to change carlos csrfkey with wiener but "bad request"
tried to change carlos csrf    with wiener but "invalid csrf token"
tried to change carlos session with wiener and got accepted , and wiener email whose got changed .
- so indeed csrf key is tied to csrf parameter 

**behavior noted:** we can make more than one reqeust with same csrf value .


can we change both csrfkey and csrf parameter with a hacker values then we can craft our payload .


## If the web site contains any behavior that allows an attacker to set a cookie in a victim's browser, then an attack is possible .

--> we can see in the image [[ payloads/lab5_1.png ]] that when we search for smth it set-cookie: the smth , we can abuse that by setting a cookie for csrfkey .

%0d%0a : new line 
```bash
https://ac001f1b1e0a940f809e2740007a00b2.web-security-academy.net/?search=hat%0d%0aSet-Cookie:%20csrfKey=uTfxHfa8p5clUZA772gMSM1xDXYtw1GS
```
 now in our payload we need to set the cookie and change csrf value 


# [6] CSRF where token is duplicated in cookie


the request when we want to change the email :

```bash

Cookie: session=9cnbU9FtHPaqSqqoDAur8Q3tLIPnN4vC; csrf=0HS2OuoJncwLJqf2EIZS319lJJjDHn2g

email=wiener2%40me.net&csrf=0HS2OuoJncwLJqf2EIZS319lJJjDHn2g

```

after testing values for both csrf and csrfkey , they are compared to be the same or not , so we can change Both with any random value , so we will use same previous payload . with same value at both 



# CSRF where Referer validation depends on header being present

request "highlight lines"
```bash
POST /my-account/change-email HTTP/1.1
Host: acbb1f7f1f3148c7c0c523c50008000c.web-security-academy.net
Origin: https://acbb1f7f1f3148c7c0c523c50008000c.web-security-academy.net
Referer: https://acbb1f7f1f3148c7c0c523c50008000c.web-security-academy.net/my-account
Cookie: session=6uY9sbjr14KS6pwRK4OcAK9zXLRol5yr

email=test5%40test.caaffa

```



if we change referere value we have a bad request , However if we deleted it , it will be accepted . 
our payload will work only if we deleted the referer header 
```bash
 
 <meta name="referrer" content="no-referrer" />

```

we will use same previous payload but add this header at <head> tag 



# CSRF with broken Referer validation


we can see same request is sent as last one however , when we remove the referer header it returns ``"Invalid referer header"`` 

removing some parts and didn't work . try :
```bash

Referer: https://blablabla.ace11f801ea038f6c0d7656300e8004b.web-security-academy.net/my-account

```
so it checks if the ``ace11f801ea038f6c0d7656300e8004b.web-security-academy.net/my-account`` part of referer or not .


```js 
history.pushState("", "", "/?ace11f801ea038f6c0d7656300e8004b.web-security-academy.net")       
```



# done * ___ *