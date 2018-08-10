#!/usr/bin/bash

#conections_per_secondsの最大値
max_per_seconds=1000

#number_of_conectionsの最大値
max_conections=5000

#conections_per_secondsの初期値
conections_per_seconds=200

#number_of_conectionsの初期値
number_of_conections=1000


while [ "$number_of_conections" -le "$max_conections" ]	
do
	while [ "$conections_per_seconds" -le "$max_per_seconds" ]
	do
		mkdir -p ${conections_per_seconds}_${number_of_conections}

		for i in `seq 1 240`
		do
		#echo ${i} > ./sec${i}.log
		netstat -an -p tcp | grep "10.1.200.10:" >> ./${conections_per_seconds}_${number_of_conections}/sec${i}.log
		sleep 1
		done
		python /home/sumire/netstatlog/log_graph.py /home/sumire/netstatlog/${conections_per_seconds}_${number_of_conections}
		conections_per_seconds=`expr $conections_per_seconds + 100`
	done
	conections_per_seconds=200
        number_of_conections=`expr $number_of_conections + 500`
done


