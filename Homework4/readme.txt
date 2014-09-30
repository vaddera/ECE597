Student: Alexandre van der Ven de Freitas
CM: 1453

In this Homework assignment 4, the Memory Map diagram can be found in the Memo. 
As for the GPIO mmap C program can be found in the /mmap directory where gpioToggle.c was modified for the purposes of this assigment.

The modified etch-a-sketch that uses the encoders can be found in the directory /etch_a_sketch/LEDetch.py. To avoid setting up the encoders everytime the BBB is booted, I've put all the configuration files within the directory as well as a Shell script in which runs them. The LEDetch.py calls encoderSetup.py whenever it is executed to automatically configure the encoders.

For the web-based control part of the assignment, I copied the exercises/realtime/ directory into the Homework4 directory and altered matrixLED.js, matrixLED.css and matrixLED.html in order to meet with the requirements of the Homework.

The /encoder directory was used only for purposes of understanding and setting up the encoders for the first time.
