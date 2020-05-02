import RPi.GPIO as GPIO
import time
from src.Logger import log
from src.Utils import debounce


class Button:
    def __init__(self, buttonGPIO, ledGPIO, callbackButtonPressed):
        self.buttonGPIO = buttonGPIO
        self.callbackButtonPressed = callbackButtonPressed
        self.ledGPIO = ledGPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(buttonGPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.ledGPIO, GPIO.OUT)
        GPIO.add_event_detect(buttonGPIO, GPIO.RISING,
                              callback=self.button_callback)  # Setup event on pin 10 rising edge

    @debounce(0.5)
    def button_callback(self, channel):
        log('Play/Pause button pressed')
        self.callbackButtonPressed()

    def toggleLed(self, isTurnedOn):
        if isTurnedOn:
            log("Turning led ON")
            GPIO.output(self.ledGPIO, GPIO.HIGH)
        else:
            log("Turning led OFF")
            GPIO.output(self.ledGPIO, GPIO.LOW)

    def makeSignal(self, numberOfBlinks):
        for x in range(0, numberOfBlinks):
            GPIO.output(self.ledGPIO, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(self.ledGPIO, GPIO.LOW)
            time.sleep(1)

