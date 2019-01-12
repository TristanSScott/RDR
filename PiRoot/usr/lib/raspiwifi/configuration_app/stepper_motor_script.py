import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
ControlPin=[7,11,13,15]

for pin in ControlPin:
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin,False)

step_seq_num=0
#rot-spd=0.001
rotate=4096
#rotate_dir=1

seq=[ [1,0,0,0],
	[1,1,0,0],
	[0,1,0,0],
	[0,1,1,0],
	[0,0,1,0],
	[0,0,1,1],
	[0,0,0,1],
	[1,0,0,1],
	 ]
rotateF=float(input("Enter revolutions(0.00041 +):"))
rotate_dir=input("Enter direction (1CW/-1 CW) :")
rot_spd=input("Enter speed (1-0.001):")

rotate=int(rotateF * 4096)
if rotate < 1: rotate=4096
rotate_dir=int(rotate_dir)
if rotate_dir !=1 and rotate_dir !=-1 : rotate_dir=1
rot_spd=float(rot_spd)
if rot_spd > 1 or rot_spd < 0.001 : rot_spd = 2.00
print(rotate,rotate_dir,rot_spd)

for i in range(0,(rotate+1)):
	for pin in range(0,4):
		Pattern_Pin=ControlPin[pin]
		if seq[step_seq_num][pin] ==1:
			GPIO.output(Pattern_Pin,True)
		else:
			GPIO.output(Pattern_Pin,False)

	step_seq_num+=rotate_dir
	if(step_seq_num >=8):
		step_seq_num=0
	elif step_seq_num <0:
		step_seq_num=7


	time.sleep(rot_spd)

GPIO.cleanup() 
