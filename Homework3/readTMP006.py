import Adafruit_TMP.TMP006 as TMP006

sensor = TMP006.TMP006()

sensor.begin()

objTempC = sensor.readObjTempC()
dieTempC = sensor.readDieTempC()

objTempF = objTempC*9/5 + 32
dieTempF = dieTempC*9/5 + 32


print '\nObject Temperature in Celsius: '
print objTempC

print 'Object Temperature in Fahrenheit: '
print objTempF

print 'Die temperature in Celsius: '
print dieTempC

print 'Die Temperature in Fahrenheit: '
print dieTempF
print' '
