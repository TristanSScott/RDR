import os
from multiprocessing import Pool
from argparse import ArgumentParser

def run_process(process): 
	os.system('python {}'.format(process))

def open():
	primaryMotorRotation = "clockwise"
	secondaryMotorRotation = "CounterClockwise"
	print(primaryMotorRotation) 
	processes = ('StepperMotorLeft.py "' + primaryMotorRotation + '"', 'StepperMotorRight.py "' + secondaryMotorRotation + '"') 
	pool = Pool(processes=2) 
	pool.map(run_process, processes) 
def close():
	primaryMotorRotation = "counterclockwise"
	secondaryMotorRotation = "clockwise"
	print(primaryMotorRotation) 
	processes = ('StepperMotorLeft.py "' + primaryMotorRotation + '"', 'StepperMotorRight.py "' + secondaryMotorRotation + '"') 
	pool = Pool(processes=2) 
	pool.map(run_process, processes) 

