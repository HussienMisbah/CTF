#!/bin/bash

s=$(cat all_payload_url_decoded )

i=0
while true

do

dummy=$(echo $s |base64 -d | sed s/'\\n'//g | sed s/'{"payload": "'//g | sed s/'"}'//g)
s=$dummy

# check substr "flag" in the output 
if [[ $dummy == *'flag'* ]]
then
echo $dummy
break
fi
done


