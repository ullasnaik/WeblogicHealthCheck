#!/bin/bash

wlst="/scratch/app/WP26DEV8/fmw/12.2.1.2.0/oracle_common/common/bin/wlst.sh"

if [ "$1" = "ServerStatus.py" ]
then
    sh $wlst ServerStatus.py $2 $3 $4 $5
elif [ "$1" = "AllDataSourceStatus.py" ]
then
    sh $wlst AllDataSourceStatus.py $2 $3 $4 $5
elif [ "$1" = "AllHeapThreadStatus.py" ]
then
    sh $wlst AllHeapThreadStatus.py  $2 $3 $4 $5
else
    echo "Please enter valid python script as argument"
fi



