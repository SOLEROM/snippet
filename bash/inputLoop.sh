#!/bin/bash

while [[ $# -gt 0 ]]
do
key="$1"
case $key in
    -a|--aaa) 			#example1
	echo -a/-aaa with no params 
	shift # past argument
	;;
    -b|--bbb)                   #example2
        echo -b/-bbb enter with param=$2 
        shift # past argument
        shift # past value
        ;;	 
    *)  			#example3
	echo else input
    	shift # past argument
    	;;
esac
done
