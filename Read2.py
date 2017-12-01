#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522
import requests

reader = SimpleMFRC522.SimpleMFRC522()

while True: 
    id, text = reader.read()
    print(id)
    print(text)

    r = requests.get('http://listen-for-badge-returned.azurewebsites.net/api/badge?badge-id=' + str(id))
    print(r)

GPIO.cleanup()
