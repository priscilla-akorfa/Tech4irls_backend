#!/bin/bash
echo "Give three numbers"
read "number 1"
read "number 2"
read "number 3"
sum=$(( $number1 + $number2 ))
product=$(( sum * $number3 ))

echo "The sum of $number1 and $nmuber2 is:$sum"
echo "The product of $number3 and $sum is:$product"

