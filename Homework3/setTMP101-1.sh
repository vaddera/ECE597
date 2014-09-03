#!/bin/bash

echo "Setting T-high and T-low of TMP101 registers"

# The configuration register is set to 0x04
# OS/ALERT = 0; R1 = 0; R0 = 0; F1 = 0; F0 = 0; POL = 1; TM = 0; SD = 0;
echo $(i2cset -y 1 0x48 1 0x04)
echo $(i2cset -y 1 0x4a 1 0x04)
echo $(i2cset -y 1 0x48 2 0x1a)
echo $(i2cset -y 1 0x48 3 0x1b)
echo $(i2cset -y 1 0x4a 2 0x1a)
echo $(i2cset -y 1 0x4a 3 0x1b)
