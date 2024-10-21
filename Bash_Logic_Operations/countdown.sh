#!/bin/bash
 
 while true; do
   echo "Enter a number or type q to quit"
   read number 

if [[ "$number" == "q" ]]; then
  break
fi    

  echo "You entered $number"
done  