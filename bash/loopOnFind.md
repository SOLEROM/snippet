# loop on find

```
find . -name "*.txt" -print0 | while read -d $'\0' file
do
    …code using "$file"
done
```

* The loop will execute while the find command is executing. 
* work even if a file name is returned with whitespace in it.
* won't overflow line buffer
* The -print0 will use the NULL as a file separator instead of a newline
* the -d $'\0' will use NULL as the separator while reading.
