#!/usr/bin/python
# -*- utf-8 -*-
import time
import json
import requests
import sys

url = "http://133.2.113.168/pi"
con = requests.session()

def sendJson(sensor):
    dict = {"sensor": sensor}
    jsonString = json.dumps(dict)
    con.post(url,data=jsonString)

def reading(sensor):
    import RPi.GPIO as GPIO

    GPIO.setwarnings(False)

    GPIO.setmode(GPIO.BCM)
        
    if sensor == 0:
        GPIO.setup(17,GPIO.OUT)
        GPIO.setup(27,GPIO.IN)
        GPIO.output(17,GPIO.LOW)

        time.sleep(0.3)

        GPIO.output(17,True)

        time.sleep(0.00001)

        GPIO.output(17,False)

        while GPIO.input(27) == 0:
            signaloff = time.time()

        while GPIO.input(27) == 1:
            signalon = time.time()

        timepassed = signalon - signaloff
            
        # cm display
        distance = round(timepassed * 17000 / 100, 2)
	
        sendJson(distance)
        print distance    
        GPIO.cleanup()
            
    else:
        print "Incorrect usonic() function varible."

reading(0)
    
