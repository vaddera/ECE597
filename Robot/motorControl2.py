import Adafruit_BBIO.GPIO as GPIO
import time

speed = 0.005
#speed = 0
pwmPeriod = speed


H1 = "P8_43"
H2 = "P8_45"
H3 = "P8_41"
H4 = "P8_39"

#def motorSetup():
GPIO.setup(H1, GPIO.OUT)
GPIO.setup(H2, GPIO.OUT)
GPIO.setup(H3, GPIO.OUT)
GPIO.setup(H4, GPIO.OUT)

GPIO.output(H1, GPIO.LOW)
GPIO.output(H2, GPIO.LOW)
GPIO.output(H3, GPIO.LOW)
GPIO.output(H4, GPIO.LOW)
	
#def stop():
#	motorSetup()

#	GPIO.output(H1, GPIO.LOW)
#        GPIO.output(H2, GPIO.LOW)
#        GPIO.output(H3, GPIO.LOW)
#        GPIO.output(H4, GPIO.LOW)

#def movingForward(pwmPeriod):

	#motorSetup()
while True:

	for i in range(1000):
		GPIO.output(H1, GPIO.HIGH)
		GPIO.output(H3, GPIO.HIGH)
		time.sleep(pwmPeriod)
		GPIO.output(H1, GPIO.LOW)
		GPIO.output(H3, GPIO.LOW)
		time.sleep(pwmPeriod)

#def movingBackward(pwmPeriod):

	#motorSetup()
	for i in range(1000):
		GPIO.output(H2, GPIO.HIGH)
		GPIO.output(H4, GPIO.HIGH)
		time.sleep(pwmPeriod)
		GPIO.output(H2, GPIO.LOW)
		GPIO.output(H4, GPIO.LOW)
		time.sleep(pwmPeriod)

#def turnRight(pwmPeriod):

#def turnLeft(pwmPeriod):
'''

while True:

	for i in range(1000):
		movingForward(speed)
		GPIO.cleanup()

	stop()

	for i in range(1000):
		movingBackward(speed)
		GPIO.cleanup()

'''
