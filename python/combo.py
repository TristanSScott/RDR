from flask import Flask, render_template, request, jsonify
import subprocess
import os
import sys
sys.path.insert(0, '/usr/lib/raspiwifi/reset_device')

import stepper_motor_parallel
import reset_lib

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
     return "Hello World!"

@app.route('/motor', methods=['GET'])
def motor_home():
	return "What do you want to do with the motor? open | close"

@app.route('/motor/open', methods=['GET'])
def motor_open():
	try:
		stepper_motor_parallel.open()
		return jsonify(door = "open")

	except (IndexError, IOError) as e:
		return jsonify({'error': e.message}), 503

@app.route('/motor/close', methods=['GET'])
def motor_close():
	try:
		stepper_motor_parallel.close()
		return jsonify(door = "close")

	except (IndexError, IOError) as e:
		return jsonify({'error': e.message}), 503

@app.route('/reset', methods=['GET'])
def rdr_reset():
	reset_lib.reset_to_host_mode()	
	return "Are you subscribed to pewdiepie? Yes | No"


@app.route('/setup')
def rdr_setup():
    wifi_ap_array = scan_wifi_networks()

    return render_template('app.html', wifi_ap_array = wifi_ap_array)

######## FUNCTIONS ##########

def scan_wifi_networks():
    iwlist_raw = subprocess.Popen(['iwlist', 'scan'], stdout=subprocess.PIPE)
    ap_list, err = iwlist_raw.communicate()
    ap_array = []

    for line in ap_list.decode('utf-8').rsplit('\n'):
        if 'ESSID' in line:
            ap_ssid = line[27:-1]
            if ap_ssid != '':
                ap_array.append(ap_ssid)

    return ap_array

def create_wpa_supplicant(ssid, wifi_key):
    temp_conf_file = open('wpa_supplicant.conf.tmp', 'w')

    temp_conf_file.write('ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev\n')
    temp_conf_file.write('update_config=1\n')
    temp_conf_file.write('\n')
    temp_conf_file.write('network={\n')
    temp_conf_file.write('	ssid="' + ssid + '"\n')

    if wifi_key == '':
        temp_conf_file.write('	key_mgmt=NONE\n')
    else:
        temp_conf_file.write('	psk="' + wifi_key + '"\n')

    temp_conf_file.write('	}')

    temp_conf_file.close

    os.system('mv wpa_supplicant.conf.tmp /etc/wpa_supplicant/wpa_supplicant.conf')

def set_ap_client_mode():
    os.system('rm /etc/cron.raspiwifi/aphost_bootstrapper')
    os.system('cp /usr/lib/raspiwifi/reset_device/static_files/apclient_bootstrapper /etc/cron.raspiwifi/')
    os.system('chmod +x /etc/cron.raspiwifi/apclient_bootstrapper')
    os.system('mv /etc/dnsmasq.conf.original /etc/dnsmasq.conf')
    os.system('mv /etc/dhcpcd.conf.original /etc/dhcpcd.conf')
    os.system('cp /usr/lib/raspiwifi/reset_device/static_files/isc-dhcp-server.apclient /etc/default/isc-dhcp-server')
    os.system('reboot')

def config_file_hash():
    config_file = open('/etc/raspiwifi/raspiwifi.conf')
    config_hash = {}

    for line in config_file:
        line_key = line.split("=")[0]
        line_value = line.split("=")[1].rstrip()
        config_hash[line_key] = line_value

    return config_hash


if __name__ == '__main__':
    config_hash = config_file_hash()

    if config_hash['ssl_enabled'] == "1":
        app.run(host = '0.0.0.0', port = config_hash['server_port'], ssl_context='adhoc')
    else:
        app.run(host = '0.0.0.0', port = config_hash['server_port'])




#if __name__ == "__main__":
#    app.run(host="0.0.0.0", port=80)
