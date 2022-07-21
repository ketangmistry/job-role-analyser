#!/bin/bash

file=$(env | grep GOOGLE | awk -F'=' '{print $2}')

while IFS= read -r line
do
    key=$(echo $line | awk -F':' '{print $1}' | sed 's/\"//g')
    if [ $key == 'project_id' ]
    then
       project_id=$(echo $line | awk -F':' '{print $2}')
       echo $project_id | sed 's/\"//g' | sed 's/,//g'
    fi
done < $file