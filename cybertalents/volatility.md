# 9 SEP 2021 | pre-national ctf


## discovery 


`$ python2 ~/tools/volatility/vol.py -f ~/Desktop/memdump1.mem imageinfo`

![image](https://user-images.githubusercontent.com/67979878/132720029-708504d8-1d50-411b-b247-ee47964cebab.png)


we know it is the desktop let's try :

`$ python2 ~/tools/volatility/vol.py -f ~/Desktop/memdump1.mem --profile=WinXPSP2x86 consoles`



![image](https://user-images.githubusercontent.com/67979878/132720239-bb07fdbe-f87d-4a68-8cf8-bc586e2eb48c.png)

let's take this files in the flag directory and start manipulating it to sort it somehow 

![image](https://user-images.githubusercontent.com/67979878/132720553-5a1515a8-fec2-4b7d-9716-851f93bd4b2a.png)

we can sort it by the time modified so:

![image](https://user-images.githubusercontent.com/67979878/132720772-bbdd1c21-9f51-4a67-8242-f7ebeffcfaa8.png)

we can also remove `02:`

![image](https://user-images.githubusercontent.com/67979878/132721119-906f0218-4078-4ca5-9d15-c3cc9ee09e22.png)

![image](https://user-images.githubusercontent.com/67979878/132721565-271230c9-45ae-4f5b-9aef-c86ca3d9d35d.png)

```python
#!/usr/bin/python 


my_list=[]
with open("voly",'r') as handler :
	for line in handler :
		tmp=(line.replace('\n','').split('  ')[0],line.split('  ')[1].replace('\n',''))
		my_list.append(tmp)
	my_list.sort()
	for x in range(len(my_list)) :
		print(my_list[x][1],end='')


		#fagl{egr_at_now_ouy_knowabo_tuvaillotity}   
		#flag{great_now_you_know_about_volatility}
                                                                                                                                              

```
