#!/bin/bash
#Positional Arguments in Bash Scripting
#$0= script's name
#$1= second argument
#$2= third argument

#echo "Hello $1,How are you doing?"

#echo "The first argument or the name of the script is: $0"
#echo "The second argument is $1"
#echo "The third argument is $2"
#echo "The fourth argument is $3"

#sum=$(($1 + $2))
#echo "the sum of $1 and $2 is: $sum"

#diff=$(($1-$2))
#echo "the diff of $1 and $2 is: $diff"
#div=$(($1/$2))
#echo " the div of $1 and $2 is: $div"
#mul=$(($1*$2))
#echo " the mul of $1 and $2 is : $mul"
#touch file3
#mkdir folder3
#mv "$1" "$2"
#echo $1 has been moved into $2
#touch file2
#mkdir folder2
#cp "$1" "$2"
#echo "$1 has been copied into $2"

#LOGICAL OR= || -o
#LOGICAL AND =&& -a
#LOGICAL NOT = !
#IF STATEMENTS IN BASH
# if [ condition ]
# then
#     statement 
# fi     
#if [ "$1" -gt 10  ] && [ "$2" -gt 10 ]
#then
#    echo "Both numbers are greater than 10"
#else
#    echo "Both numbers are not greater than 10 "
#fi         
#read name
#if [[ ! $name == "Admin" ]]; then
#    echo "Acess denied"
#else
#    echo "Acess granted"
#fi 

#WHILE LOOPS IN BASH

# # while [ condition ]
# # do
#     [command]
#     [command]
#     [command]
# # done

while true; do  
  echo "Enter a number 'q' to quit"
  read number
  
  if [[ "$number" == 'q' ]]; then
    break
  fi 

  echo "You entered. $number"   
done 

echo "Exiting the loop"
