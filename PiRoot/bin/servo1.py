from gpiozero import Servo
from time import sleep
myGPIO=24
myServo = Servo(myGPIO)

def min():
	while True:
		myServo.mid()
		sleep(1)
		myServo.max()
		sleep(1)


def mid():
myGPIO=24
myServo = Servo(myGPIO)

while True:
	myServo.mid()
	sleep(1)
	myServo.min()
	sleep(1)

def max():
myGPIO=24
myServo = Servo(myGPIO)

while True:
	myServo.max()
	sleep(1)
	myServo.min()
	sleep()

