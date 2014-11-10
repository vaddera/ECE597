import Adafruit_BBIO.ADC as ADC #Similar to analog read
import time as T

# Useful Lists:
IR1list = []
IR2list = []
IR3list = []
IR4list = []
IR5list = []

# General purpose variables:
count = 0
samples = 20
mult = 20

ADC.setup() #may need to put argument

while True:

	# Reading analog inputs:
	IR1 = ADC.read("P9_40")
	IR2 = ADC.read("P9_39")
	IR3 = ADC.read("P9_38")
	IR4 = ADC.read("P9_37")
	IR5 = ADC.read("P9_33")

	for i in range(samples):
		count = count + 1

		IR1list.append(round(IR1*mult,1))
		IR2list.append(IR2)
		IR3list.append(IR3)
		IR4list.append(IR4)
		IR5list.append(IR5)

		if (count == samples):
			# Calculating the average of 3 readings:
			avgIR1 = sum(IR1list) / len(IR1list)
			avgIR2 = sum(IR2list) / len(IR2list)
			avgIR3 = sum(IR3list) / len(IR3list)
			avgIR4 = sum(IR4list) / len(IR4list)
			avgIR5 = sum(IR5list) / len(IR5list)
			
			# Clearing each list:
			IR1list = []
			IR2list = []
			IR3list = []
			IR4list = []
			IR5list = []
			count = 0

	#print(round(avgIR1*mult,1))
	print(avgIR1)

	T.sleep(1)
	
	#OUTA = "%.3f" % OUTA
	#OUTB = "%.3f" % OUTB
'''
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

#print('IR1: ' + str(IR1))
#print(IR1)
#print('IR2 ')
#print(OUTB)

