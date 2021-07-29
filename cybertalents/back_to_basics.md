visting link provided will redirect you to google search page so let's see requests with curl commnad to investigate what is happening :) 

## $curl http://35.197.254.240/backtobasics/ -vvv  #this is a get requst by default .

results aren't interesting just normal stuff 


#### http://35.197.254.240/backtobasics/ vs http://35.197.254.240/backtobasics
##### without / we are searching for a document called backtobasics
##### with   /  we are searching for http://35.197.254.240/backtobasics/index.html

## $ curl -X POST http://35.197.254.240/backtobasics/ -vvv



I've found this : 
```
<!--
var _0x7f88=["","join","reverse","split","log","ceab068d9522dc567177de8009f323b2"];function reverse(_0xa6e5x8[3]](_0x7f88[0])[_0x7f88[2]]()[_0x7f88[1]](_0x7f88[0])}console[_0x7f88[4]]= reverse;console[_0x7f88[4]](_0x
* Connection #0 to host 35.197.254.240 left intact
-->                  
```
it seems this is an obfuscation js os let's beautify it :) 

using 

https://lelinhtinh.github.io/de4js/

````
function reverse(_0xa6e5x2) {
    flag = _0xa6e5x2.split('').reverse().join('')
}
console.log = reverse;
console.log('ceab068d9522dc567177de8009f323b2')
````

modify it  :
```
function reverse() {
    flag = 'ceab068d9522dc567177de8009f323b2'.split('').reverse().join('')
    console.log(flag);
}
reverse()

```
$node test.js

### now we can read the flag .
