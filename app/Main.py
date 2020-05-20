import pygame
from src.Player import Player
from src.Logger import loggerInit, log, error
from src.FilesManager import getAllFileNames
from src.Button import Button

BOOK_PART_END = pygame.USEREVENT + 1

loggerInit()
player = Player(BOOK_PART_END)
log("--- APP STARTED ---")

allParts = getAllFileNames()
currentPartPlaying = 0
isInitiallyMode = True

if len(allParts) == 0:
    error("There is no book to play!")


def buttonPressed():
    global isInitiallyMode
    log('Button pressed received from Main')
    if isInitiallyMode:
        isInitiallyMode = False
        player.play(allParts[0])
        button.toggleLed(True)
        return

    isPaused = player.pause()
    button.toggleLed(not isPaused)

def rewButtonPressed():
    log('Rew button pressed')
    player.checkPosition()


button = Button(18, 24, buttonPressed)
button.makeSignal(3)

rewButton = Button(23, 20, rewButtonPressed)

def loadNextPart():
    global currentPartPlaying
    print(currentPartPlaying)
    log('End of part: ' + str(currentPartPlaying))
    currentPartPlaying += 1
    player.play(allParts[currentPartPlaying])


while True:
    # player.checkPosition()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == BOOK_PART_END:
            loadNextPart()
