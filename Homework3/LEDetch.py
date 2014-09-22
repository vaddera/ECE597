import time
import Image
import ImageDraw
import Adafruit_BBIO.GPIO as GPIO

from Adafruit_LED_Backpack import Matrix8x8

# Creates display instance and initializes it
display = Matrix8x8.Matrix8x8(address=0x70, busnum=1)
#display = Matrix8x8.Matrix8x8()
display.begin()

# Setting up input
GPIO.setup("P9_21", GPIO.IN) # Up
GPIO.setup("P9_23", GPIO.IN) # Down
GPIO.setup("P9_24", GPIO.IN) # Left
GPIO.setup("P9_27", GPIO.IN) # Right
GPIO.setup("P9_30", GPIO.IN) # Clear

# Setting up event detection
GPIO.add_event_detect("P9_21", GPIO.RISING)
GPIO.add_event_detect("P9_23", GPIO.RISING)
GPIO.add_event_detect("P9_24", GPIO.RISING)
GPIO.add_event_detect("P9_27", GPIO.RISING)
GPIO.add_event_detect("P9_30", GPIO.RISING)

# Initializing etch-a-sketch variables
rowSize = 8
colSize = 8
#panel = [[0 for x in xrange(rowSize)]for x in xrange(colSize)]
curr_row = 4
curr_col = 4
first_stroke = 0 # flag to detect first sketch

# Clearing the LED matrix to begin:
display.clear()

while True:
	# Updates the LED display:
	display.write_display()

	if GPIO.event_detected("P9_21"):
		if curr_row <= 0:
			curr_row = 0
		else:
			curr_row = curr_row - 1
		first_stroke = 1

	if GPIO.event_detected("P9_23"):
		if curr_row >= 7:
			curr_row = 7

			curr_row = curr_row + 1
		first_stroke = 1

	if GPIO.event_detected("P9_24"):
		if curr_col <= 0:
			curr_col = 0
		else:
			curr_col = curr_col - 1
		first_stroke = 1

	if GPIO.event_detected("P9_27"):
		if curr_col >= 7:
			curr_col = 7
		else:
			curr_col = curr_col + 1
		first_stroke = 1

	if GPIO.event_detected("P9_30"):
		display.clear()
		first_stroke = 0
	
	if first_stroke != 0:
		display.set_pixel(curr_row, curr_col, 1)

	display.write_display()

