import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import time
import random as rand
from IRread import IRread, distanceCalc

# Global Variables:

# Wall position:
sideWall = 0

# Encoder variable:
encoder = 0
prevEncoder = 0
timeoutFlag = 0

# IR sensor threasholds (in cm):
frontLimit = 12
fLeftLower = 19
fRightLower = 15
fLeftHigh = fLeftLower + 5
fRightHigh = fRightLower + 5

# Right and left sensors' min and max thresholds still need to be defined after they are placed in the robot.

#rightLower = 0 --> To be determined
#leftLower = 0 ---> To be determined
#rightHigh = rightLower + 5
#leftHigh = leftLower + 5

# Encoder setup:
GPIO.setup("P9_11", GPIO.IN) #OUTA
GPIO.setup("P9_12", GPIO.IN) #OUTB
GPIO.add_event_detect("P9_11", GPIO.RISING)
GPIO.add_event_detect("P9_12", GPIO.RISING)

while True:

	# Reads each of the IR sensors:
	front, fLeft, fRight, right, left = IRread()

	# Calculates their values in cm:
	cmFront = distanceCalc(front)
	cmFleft = distanceCalc(fLeft) # Use this only for turns
	cmFright = distanceCalc(fRight) # Use this only for turns
	cmRight = distanceCalc(right)
	cmLeft = distanceCalc(left)
	

	if cmFront > frontLimit and cmFleft > fLeftHigh and cmFright > fRightHigh and cmRight > rightHigh and cmLeft > leftHigh:
		
		# When no walls are detected in any of the sensors, the robot takes a random direction to follow
		# until an obstacle is detected.

		r = rand.randrange(3)

		if r == 0:
			# Move forward
		elif r == 1:
			# Turn right
		else:
			# Turn left

	if cmFront > frontLimit:

		# No walls ahead were detected

		if (cmFleft > fLeftLower and cmFleft < fLeftHigh) or (cmFright > fRightLower and cmFright < fRightHigh):
			
			# In case the front right or left sensors detect a side wall.
			# To keep the robot near the wall but not too close, the following routine is taken:

			if cmLeft < leftLower:
				# Slight right turn
			elif cmLeft > leftHigh and cmRight > cmLeft:
				# slight left turn
			elif cmRight < rightLower:
				# slight left turn
			elif cmRight > rightHigh and cmLeft > cmRight:
				# slight right turn
			else:
				# Move robot forward
		else:

			# In case the right and left sensors detect a side wall.

			if (cmLeft > leftLower and cmLeft < leftHigh) or (cmRight > rightLower and cmRight < rightHigh):

				# Picks which side to turn into depending on the position of the wall.

				if cmLeft < cmRight:
					sideWall = 1
				else:
					sideWall = 2
				# Move robot forward
			else:
				if sideWall == 1:
					# Turn left
				elif sideWall == 2:
					# Turn right
				else:
					# Stop robot - unexpected behavior!			

	else:

		# When an obstacle is found in front of the robot, picks which side to turn.

		if cmLeft > cmRight:
			# Turn Left
		elif cmRight > cmLeft:
			# Turn right
		else:
			r = rand.randrange(x)

			if r == 0:
				# Turn right
			else:
				# Turn Left

	# In case the robot gets stuck on tight spaces, trigger timeout and take random careful action:
	# If this is too much, please disconsider and remove from the main code.
	# This is the only use I found for the encoders though.

	if GPIO.event_detected("P9_11") or GPIO.event_detected("P9_12"):
		prevEncoder = encoder
		encoder = encoder + 1

		if encoder > 49:
			encoder = 0

	if encoder == prevEncoder:

		if timeoutFlag == 0:
			beginTimeout = time.time()
			timeoutFlag = 1
		else:
			timeout = time.time() - beginTimeout

			if timeout > 5:
				r = rand.randrange(2)
				if r == 0:
					# Slow forward left turn
				else:
					# Slow forward right turn
				timeoutFlag = 0

