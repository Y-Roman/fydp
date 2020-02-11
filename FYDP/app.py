from flask import Flask, render_template
import RPi.GPIO as GPIO
import os
import datetime
app = Flask(__name__, template_folder = 'templates')
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
ds18b20 = '28-04163395faff' 

def destroy():
	pass
			
def readTemperature():
	#global ds18b20
	location = '/sys/bus/w1/devices/' + ds18b20 + '/w1_slave'
	tfile = open(location)
	text = tfile.read()
	tfile.close()
	secondline = text.split("\n")[1]
	temperaturedata = secondline.split(" ")[9]
	temperature = float(temperaturedata[2:])
	temperature = temperature / 1000
	return temperature
def loop():
	while True:
	    if readTemperature() != None:
                t = readTemperature()
                print("%.2f"%t)
  
@app.route("/")
def index():
    currentTemperature = round(readTemperature(),2)
    #temperatureInString = str(currentTemperature)
    templateData = {
    'temperature'  : currentTemperature
    }
    return render_template('index.html',**templateData )

if __name__ == '__main__':
	try:
		#setup()
		app.run(host='0.0.0.0', port=80, debug=True)
		#loop()
	except KeyboardInterrupt:
		destroy()
		
  
