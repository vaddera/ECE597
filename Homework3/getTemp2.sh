#!/bin/bash

Temp=$(i2cget -y 1 0x4a 0)

echo $Temp #For debugging purposes
echo "The temperature in Celsius:"
echo $(($Temp))

echo "The temperature in Fahrenheit:"
echo $((($Temp)*9/5 + 32))

