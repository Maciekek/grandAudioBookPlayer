import pygame
from src.Player import Player
from src.Logger import loggerInit, log, error
from src.FilesManager import getAllFileNames

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(24, GPIO.OUT)
GPIO.output(24, GPIO.LOW)

BOOK_PART_END = pygame.USEREVENT + 1

loggerInit()

log("--- APP STARTED ---")
player = Player(BOOK_PART_END)

allParts = getAllFileNames()
currentPlaying = 0

if len(allParts) == 0:
    error("There is no book to play!")


player.play(allParts[0])


def loadNextPart():
    global currentPlaying
    print(currentPlaying)
    log('End of part: ' + str(currentPlaying))
    currentPlaying += 1
    player.play(allParts[currentPlaying])


while True:

    input_state = GPIO.input(18)
    if input_state == False:
        print('Button Pressed')
        time.sleep(0.2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == BOOK_PART_END:
            loadNextPart()




