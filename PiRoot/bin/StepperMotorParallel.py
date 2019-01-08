import os
from multiprocessing import Pool
from argparse import ArgumentParser

parser = ArgumentParser()
#parser.add_argument("-r","--rotation", dest = "rotation",
#			help="direction of lead motor. Clockwise or CounterClockwise", metavar="ROTATION")
parser.add_argument("rotation", metavar='ROTATION', type=str)
args = parser.parse_args()
#print(args.rotation)

primaryMotorRotation = args.rotation.lower()
secondaryMotorRotation = "Clockwise"

if primaryMotorRotation == "clockwise":
	primaryMotorRotation = "Clockwise"
	secondaryMotorRotation = "CounterClockwise"
else:
	primaryMotorRotation = "CounterClockwise"

print(primaryMotorRotation) 

processes = ('StepperMotorLeft.py "' + primaryMotorRotation + '"', 'StepperMotorRight.py "' + secondaryMotorRotation + '"') 
#other = ('StepperMotorLeft.py', )

def run_process(process): 
	os.system('python {}'.format(process))

 
pool = Pool(processes=2) 
pool.map(run_process, processes) 
#pool.map(run_process, other) 

