#!/bin/bash

for file in  $(ls )

do

data=$(file $file | cut -d ":" -f 2 | cut -d "," -f 1 | tr -d " ")

if [ $data == "HTMLdocument" ]
then

rm -f  $file

fi


done


echo "[+] done"
