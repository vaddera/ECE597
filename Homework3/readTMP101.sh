#!/bin/bash

Temp1=$(i2cget -y 1 0x48 0)
Temp2=$(i2cget -y 1 0x4a 0)

echo "The temperature in Hex:"
echo $Temp1
echo $Temp2

echo "The temperature in C:"
echo $(($Temp1))
echo $(($Temp2))

echo "The temperature in F:"
echo $((($Temp1)*9/5 + 32))
echo $((($Temp2)*9/5 + 32))
