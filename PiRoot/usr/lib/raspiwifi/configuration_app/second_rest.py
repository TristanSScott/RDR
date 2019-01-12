from flask import Flask, jsonify
from time import sleep
import StepperMotorParallel2
#import servo1.py
import sys

sys.path.append('/home/pi/tracer/python')

#Rest API
app = Flask("Yeehaw")

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/Motor")
def servohome():
    return "What do you want to do with the motor? open | close"	

@app.route('/Motor/open', methods=['GET'])
def motoropen():
	try:
		StepperMotorParallel2.open()
		return jsonify(funny = "bob")
	except (IndexError, IOError) as e:
		return jsonify({'error': e.message}), 503


@app.route('/Motor/close', methods=['GET'])
def motorclose():
	try:
		StepperMotorParallel2.close()
		return jsonify(funny = "bob")

	except (IndexError, IOError) as e:
		return jsonify({'error': e.message}), 503


# @app.route('/LED', methods=['GET'])
# def get_data():
# 	try:
# 		first_script.blink()
# 		return jsonify(funny = "bob")

# 	except (IndexError, IOError) as e:
# 		return jsonify({'error': e.message}), 503

# try:
# 	app.run()

# except KeyboardInterrupt:
# 	print ("\nCtrl-C pressed. Closing...")
# finally:
# 	print ("Bye.")
try:
	app.run('0.0.0.0')
except KeyboardInterrupt:
	print ("\nCtrl-C pressed. Closing...")
finally:
	print ("Bye.")