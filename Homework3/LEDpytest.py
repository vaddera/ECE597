import time
import Image
import ImageDraw

from Adafruit_LED_Backpack import Matrix8x8

import Adafruit_BBIO.GPIO as GPIO

GPIO.setup("P9_21",GPIO.IN)
GPIO.setup("P9_23",GPIO.IN)
GPIO.setup("P9_24",GPIO.IN)
GPIO.setup("P9_27",GPIO.IN)
GPIO.setup("P9_30",GPIO.IN)
GPIO.add_event_detect("P9_21", GPIO.FALLING)
GPIO.add_event_detect("P9_23", GPIO.FALLING)
GPIO.add_event_detect("P9_24", GPIO.FALLING)
GPIO.add_event_detect("P9_27", GPIO.FALLING)
GPIO.add_event_detect("P9_30", GPIO.FALLING)

display = Matrix8x8.Matrix8x8(address=0x70, busnum=1)

display.begin()

display.clear()
display.write_display()

while True:
	if GPIO.event_detected("P9_21"):
		for i in range(8):
			display.set_pixel(i,i,1)
			time.sleep(0.5)
			display.write_display()

	if GPIO.event_detected("P9_23"):
		for i in range(8):
			display.set_pixel(5,i,1)
			time.sleep(0.5)
			display.write_display()

	if GPIO.event_detected("P9_24"):
		for i in range(8):
			display.set_pixel(i,5,1)
			time.sleep(0.5)
			display.write_display()

	if GPIO.event_detected("P9_27"):
		display.set_pixel(0,3,1)
		time.sleep(0.5)
		display.write_display()

	if GPIO.event_detected("P9_30"):
		display.set_pixel(7,1,1)
		time.sleep(0.5)
		display.write_display()

#display.write_display()
