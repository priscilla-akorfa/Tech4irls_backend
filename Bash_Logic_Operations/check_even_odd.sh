#!/bin/bash
read number

if (( "$number" % 2 == 0 )) 
then 
    echo "The number $number is an even number"
else
    echo "The number $number is an odd number"
fi         