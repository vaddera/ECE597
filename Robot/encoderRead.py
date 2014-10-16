import Adafruit_BBIO.ADC as ADC #Similar to analog read
import time as T

# Voltage Multiplier:
Volt = 1.8

# Setting previous read:
prevA = 0
prevB = 0

ADC.setup() #may need to put argument

while True:

	#OUTA = ADC.read_raw("P9_37")
	#OUTB = ADC.read_raw("P9_39")

	# Another option:
	OUTA = ADC.read("P9_37") * Volt
	OUTB = ADC.read("P9_39") * Volt
	
	#OUTA = "%.3f" % OUTA
	#OUTB = "%.3f" % OUTB

	if OUTA != prevA:
		print('OUTA:')
		print(OUTA)

	if OUTB != prevB:
		print('OUTB:')
		print(OUTB)

	prevA = OUTA
	prevB = OUTB

	T.sleep(5)

'''
print('Printing value of OUTA:')
print(OUTA)
print('Printing value of OUTB:')
print(OUTB)
'''
