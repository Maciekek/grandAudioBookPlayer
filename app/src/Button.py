from src.Logger import log
import RPi.GPIO as GPIO

import time
from threading import Timer



class Button:
    def __init__(self, buttonGPIO):
        self.buttonGPIO = buttonGPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(buttonGPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(buttonGPIO, GPIO.RISING, callback=self.button_callback)  # Setup event on pin 10 rising edge

    def button_callback(self, channel):
        log('presed presedpresedpresedpresedpresedpresedpresed')

    def onPressed(self):
        log('PRESED BUTTON ' + self.buttonGPIO)