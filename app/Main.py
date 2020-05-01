import pygame
from src.Player import Player
from src.Logger import loggerInit, log, error
from src.FilesManager import getAllFileNames

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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == BOOK_PART_END:
            loadNextPart()




