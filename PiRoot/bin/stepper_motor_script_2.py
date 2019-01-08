import RPi.GPIO as GPIO

# import the library
from RpiMotorLib import RpiMotorLib

GpioPinsLeft = [18, 23, 24, 25]
GpioPinsRight = [5, 6, 13, 19]
# Declare an named instance of class pass a name and motor type
mymotortest = RpiMotorLib.BYJMotor("MyMotorOne", "28BYJ")

# call the function pass the parameters
mymotortest.motor_run(GpioPinsLeft , .001, 512, False, False, "half", .05)
#mymotortest.motor_run(GpioPinsRight , .001, 512, False, False, "half", .05)
# good practise to cleanup GPIO at some point before exit
GPIO.cleanup()
