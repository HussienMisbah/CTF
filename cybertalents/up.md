ejxc{T0nY0J_BsUMS4}

### hint : Every time you go up you will gain one ballon

so as a small test we can see ejxc = flag word so to under stand the process :

a b c d e f g h i j k l m n o q r s t u v w x y z

pseudo code 
```
shift =1
e->f
shift =2
j->l
shift =3
x->a 'wrap around'
shift=4
c->g
shift=5
..
... 
....
```
i write a simple code taking in consider just modify the letters and keep special characters and numbers :
```
#!/usr/bin/env python3
#challenge up -cyber talents
text='ejxc{T0nY0J_BsUMS4}'
print(text)
count=1
out=""
for i in range(len(text)) :
    
    if text[i].isupper() :
        out +=  chr((ord(text[i]) + count-65) % 26 + 65)
    elif text[i].islower() :
        out +=  chr((ord(text[i]) + count-97) % 26 + 97)
    elif text[i].isdigit():
        out+=text[i]
    else :
        out+=text[i]
        continue
    
    count +=1

print(out)



```

run the script and the flag will be there for you 
