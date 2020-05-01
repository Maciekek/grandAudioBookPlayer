from src.Logger import log
import RPi.GPIO as GPIO

import time

def debounce(s):
    """Decorator ensures function that can only be called once every `s` seconds.
    """
    def decorate(f):
        t = None

        def wrapped(*args, **kwargs):
            nonlocal t
            t_ = time.time()
            if t is None or t_ - t >= s:
                result = f(*args, **kwargs)
                t = time.time()
                return result
        return wrapped
    return decorate

class Button:
    def __init__(self, buttonGPIO):
        self.buttonGPIO = buttonGPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(buttonGPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(buttonGPIO, GPIO.RISING, callback=self.button_callback)  # Setup event on pin 10 rising edge

    @debounce(2)
    def button_callback(self):
        log('presed presedpresedpresedpresedpresedpresedpresed')

    def onPressed(self):
        log('PRESED BUTTON ' + self.buttonGPIO)