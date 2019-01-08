import RPi.GPIO as GPIO
from argparse import ArgumentParser

parser = ArgumentParser()
#parser.add_argument("-r","--rotation", dest = "rotation",
#			help="direction of lead motor. Clockwise or CounterClockwise", metavar="ROTATION")
parser.add_argument("rotation", metavar='ROTATION', type=str)
args = parser.parse_args()
#print(args.rotation)

rotation = args.rotation.lower()

if rotation == "clockwise":
	 rotation = "Clockwise"
else:
	rotation = "CounterClockwise"

print(rotation) 

# import the library
from RpiMotorLib import RpiMotorLib

GpioPins = [18, 23, 24, 25]
# Declare an named instance of class pass a name and motor type
mymotortest = RpiMotorLib.BYJMotor("MyMotorOne", "28BYJ")

# call the function pass the parameters
if rotation == "Clockwise":
	mymotortest.motor_run(GpioPins , .001, 512, False, False, "half", .05)
else:
	mymotortest.motor_run(GpioPins , .001, 512, True, False, "half", .05)
# good practise to cleanup GPIO at some point before exit
GPIO.cleanup()
