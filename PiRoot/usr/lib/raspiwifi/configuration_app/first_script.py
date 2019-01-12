#!/usr/bin/python

#LED light (blink)
# import RPi.GPIO as GPIO
# import time
# def blink():
# 	GPIO.setmode(GPIO.BCM)
# 	GPIO.setup(18, GPIO.OUT)
# 	GPIO.output(18, True)
# 	while True:
# 		print("light on")
# 		time.sleep(3)
# 		print("light off")
# 		GPIO.output(18, False)
# 		time.sleep(3)
# 		GPIO.output(18, True)
from gpiozero import Servo
from time import sleep

def blink():
	myGPIO=24
	myServo = Servo(myGPIO)
	while True:
		myServo.max()
		sleep(1)
		myServo.min()
		sleep()