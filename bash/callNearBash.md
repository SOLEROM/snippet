# call some script relative to full path of running one

```
myPath=$(readlink -f $0)
myDir=`dirname $myPath`
nextScript="$myDir/someScriptNearME.sh"
```
