The codes related to question 1 from homework 3 are the following:
	1. hw3e1-4.js - The script which reads the temperature values from 
			TMP101 whenever ALERT is high.

		1.a. setTMP101-1.sh - Shell script which sets Thigh, Tlow and
				      configuration registers from TMP101

		1.b. getTemp1.sh & getTemp2.sh - Shell scripts that reads the
						 temperature measured by TMP101

	2. readTMP006.py - This python script simply reads the temperatures
			   measured from TMP006 through an API.

The code for question 2, the etch-a-sketch using the LED backpack is the following:

	LEDetch.py

It uses a python API to control the LED Backpack. Although that seems very practrical, the API has a lot of faults such as not clearly being defined which inputs have pullup resistors pre-defined. For instance, the hardware configuration that is capable of making it work is the following:

	P9_21 --> BUTTON --> GND
	P9_23 --> BUTTON --> VDD
	P9_24 --> BUTTON --> GND
	P9_27 --> BUTTON --> VDD
	P9_30 --> BUTTON --> VDD

Another issue is that in the API, the array of LEDs is arranged in the following order:

	  1 2 3 4 5 6 7 0 <--- Isn't in the right order (manually tested).
	0
	1
	2
	3
	4
	5
	6
	7	
