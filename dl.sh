#!/bin/bash
ur=/usr/local/test23/data.txt
while true
do

vm5=$(md5sum /usr/local/test23/data.txt|cut -d' ' -f1)
if [ "${vm5}" == `egrep -v "^$" /root/m5.txt`  ];then
    echo "$(date)" >> /root/log.txt
    sleep 8
else
    echo "${vm5}"
    echo "${vm5}" >/root/m5.txt
    lj=$(egrep -v "^$" /usr/local/test23/data.txt|tail -1)
    egrep "^http|^https" "${ur}" >> /root/log.txt 
    if [ `egrep "^http|^https" ${ur}|grep -v grep|wc -l` -gt 0 ];then
        echo "---       $lj" >> /root/log.txt
    	wget -c -r -np -k -L -p  -P /home/download    $lj
    	sleep 5
    fi
    sleep 3
fi
done
