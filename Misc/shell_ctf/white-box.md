## Extractor :

```py
   # vulnerbale query
   query = "Select * FROM users WHERE user='{}' AND pass='{}'".format(username,password)
```

## ILLUSION :

```py
def checker():
    user_input = request.args.get("inn")
    li = ['c','d','l','s','f','l','a','g','.','t','x',';',' ']
   
    for i in user_input.lower():
        if i not in li:
            user_input = ''
    
    if "ls" in user_input:
        user_input = user_input.replace("ls","")        
    if "cd" in user_input:
        user_input = user_input.replace("cd","")
    if "d .." in user_input:
        user_input = user_input.replace("d ..","d ")
```

## More_illusion :

```py
def checker():
    user_input = request.args.get("Th1nK_Tw1c3")
    li = ['c','d','l','s','f','l','a','g','.','t','x',';',' ','-','_','u','p','r','e','n','t','i','z','h','/']
   
    for i in user_input.lower():
        if i not in li:
            user_input = ''
    if "du" in user_input:
        user_input = user_input.replace("du","")
    if "ls" in user_input:
        user_input = user_input.replace("ls","")        
    if "cd" in user_input:
        user_input = user_input.replace("cd","")
    if "d .." in user_input:
        user_input = user_input.replace("d ..","d ")
    if "../" in user_input:
        user_input = ""
 ```
