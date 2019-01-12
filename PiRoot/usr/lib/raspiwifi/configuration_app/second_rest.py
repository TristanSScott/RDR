from flask import Flask, jsonify
from time import sleep
import first_servo
#import servo1.py
import sys

sys.path.append('/home/pi/tracer/python')

#Rest API
app = Flask("Yeehaw")

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/Servo")
def servohome():
    return "What do you want to do with the servo? min | mid | max!"	

@app.route('/Servo/max', methods=['GET'])
def servomax():
	try:
		first_servo.max()
		return jsonify(funny = "bob")
	except (IndexError, IOError) as e:
		return jsonify({'error': e.message}), 503


@app.route('/Servo/mid', methods=['GET'])
def servomid():
	try:
		first_servo.mid()
		return jsonify(funny = "bob")

	except (IndexError, IOError) as e:
		return jsonify({'error': e.message}), 503

@app.route('/Servo/min', methods=['GET'])
def servomin():
	try:
		first_servo.min()
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