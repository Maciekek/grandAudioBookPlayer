import pygame
import time
from src.Player import Player
from src.Logger import loggerInit, log, error
from src.FilesManager import getAllFileNames
from src.Button import Button

#
# GPIO.setup(24, GPIO.OUT)
# GPIO.output(24, GPIO.LOW)

BOOK_PART_END = pygame.USEREVENT + 1

loggerInit()
log("--- APP STARTED ---")
player = Player(BOOK_PART_END)

allParts = getAllFileNames()
currentPlaying = 0

if len(allParts) == 0:
    error("There is no book to play!")

player.play(allParts[0])



def buttonPressed():
    log('Button pressed received from Main')
    isPaused = player.pause()
    button.toggleLed(isPaused)


button = Button(18, 24, buttonPressed)
button.toggleLed(False)

def loadNextPart():
    global currentPlaying
    print(currentPlaying)
    log('End of part: ' + str(currentPlaying))
    currentPlaying += 1
    player.play(allParts[currentPlaying])


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == BOOK_PART_END:
            loadNextPart()
