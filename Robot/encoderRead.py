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
	#OUTA = round((ADC.read("P9_36") * Volt), 3)
	#OUTB = round((ADC.read("P9_33") * Volt), 3)
	OUTA = ADC.read("P9_36")
	OUTB = ADC.read("P9_33")
	
	#OUTA = "%.3f" % OUTA
	#OUTB = "%.3f" % OUTB
	'''
	if OUTA != prevA:
		print('OUTA:')
		print(OUTA)

	if OUTB != prevB:
		print('OUTB:')
		print(OUTB)
	'''

	print 'OUTA: ' + str(OUTA)
	#print 'OUTB: ' + str(OUTB)

	T.sleep(0.5)

'''
print('Printing value of OUTA:')
print(OUTA)
print('Printing value of OUTB:')
print(OUTB)
'''
