#!/bin/bash

mv  '%2f' '0'
for packet  in ` ls |  grep -E -v "*.sh" `

# | sed s/'%2f('//g | sed s/')'//g`

do

mv $packet $(ls $packet | sed s/'%2f('//g | sed s/')'//g)

#dump=$(ls $packet | sed s/'%2f('//g | sed s/')'//g)


#echo "packet name $packet , and after will be $dump"

done


echo "[+] done"
