# loop on inputs

```

while [[ $# -gt 0 ]]
do
key="$1"
case $key in
    -a|--aaa)                   #example1
        echo -a/-aaa with no params 
        shift # past argument
        ;;
    -b|--bbb)                   #example2
        echo -b/-bbb enter with param=$2 
        shift # past argument
        shift # past value
        ;;
    *)                          #example3
        echo else input
        shift # past argument
        ;;
esac
done


```



## run examples

```
./inputLoop.sh aaa
unknown option



./inputLoop.sh -a 1
-a/-aaa with no params
unknown option


./inputLoop.sh -a -b 4 
-a/-aaa with no params
-b/-bbb enter with param=4


./inputLoop.sh --aaa --bbb 3
-a/-aaa with no params
-b/-bbb enter with param=3
```
