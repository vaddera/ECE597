#!/bin/bash

echo "Setting T-high and T-low of TMP101 registers"

echo $(i2cset -y 1 0x48 1 0x64)
echo $(i2cset -y 1 0x4a 1 0x64)
echo $(i2cset -y 1 0x48 2 0x18)
echo $(i2cset -y 1 0x48 3 0x22)
echo $(i2cset -y 1 0x4a 2 0x18)
echo $(i2cset -y 1 0x4a 3 0x22)
