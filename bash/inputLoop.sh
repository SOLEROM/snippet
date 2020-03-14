#!/bin/bash

POSITIONAL=()

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
	echo unknown option 
	POSITIONAL+=("$1") # save it in an array for later
   	shift # past argument
    	;;
esac
done


set -- "${POSITIONAL[@]}" # restore positional parameters


echo "rest input params"
echo paramNum1=$1
echo paramNum2=$2
