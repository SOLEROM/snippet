# run function on list memeber

```
#!/bin/bash

function func1
{
  echo $1
}


arr=(
"aaa"
"bbb"
"ccc"
)

for i in "${arr[@]}"
do
   # do whatever on $i
   func1 $i
done

```


