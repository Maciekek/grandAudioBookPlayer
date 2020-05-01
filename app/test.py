import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(24, GPIO.OUT)
GPIO.output(24, GPIO.LOW)

def button_callback(channel):
    print("Button was pushed!")

GPIO.add_event_detect(18,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge


while True:
    input_state = GPIO.input(18)
    if input_state == False:
        print('Button Pressed')
        time.sleep(0.2)

