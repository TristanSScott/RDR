import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
ControlPin=[7,11,13,15]

for pin in ControlPin:
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin,False)

seq=[ [1,0,0,0],
	[1,1,0,0],
	[0,1,0,0],
	[0,1,1,0],
	[0,0,1,0],
	[0,0,1,1],
	[0,0,0,1],
	[1,0,0,1],
	 ]

while True:
	print("motor on")
	time.sleep(3)
	print("motor off")
	GPIO.output(pin,False)
	time.sleep(3)
	GPIO.output(pin,True)
