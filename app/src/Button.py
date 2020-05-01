from src.Logger import log
import RPi.GPIO as GPIO

import time
from threading import Timer


def debounce(wait):
    """Postpone a functions execution until after some time has elapsed

    :type wait: int
    :param wait: The amount of Seconds to wait before the next call can execute.
    """

    def decorator(fun):
        def debounced(*args, **kwargs):
            def call_it():
                fun(*args, **kwargs)

            try:
                debounced.t.cancel()
            except AttributeError:
                pass

            debounced.t = Timer(wait, call_it)
            debounced.t.start()

        return debounced

    return decorator


class Button:
    def __init__(self, buttonGPIO):
        self.buttonGPIO = buttonGPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(buttonGPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(buttonGPIO, GPIO.RISING, callback=self.button_callback)  # Setup event on pin 10 rising edge

    @debounce(2)
    def button_callback(self, channel):
        log('presed presedpresedpresedpresedpresedpresedpresed')

    def onPressed(self):
        log('PRESED BUTTON ' + self.buttonGPIO)