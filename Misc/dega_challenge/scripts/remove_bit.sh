#!/bin/bash

mkdir clean
for i in $(ls | grep -v "clean" | grep -v "remove_bit.sh" | grep -v "renamer.sh" | grep -v "data_only.sh")
do

cat $i | cut -d '=' -f 2 > clean/$i

done


echo "[+] done "
