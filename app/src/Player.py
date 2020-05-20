import pygame
import logging
import pygame.display
import os
from mutagen.mp3 import MP3

from src.Logger import log

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))


class Player:
    mixer = pygame.mixer
    logger = logging.getLogger('grand_audio_book_player')
    isPaused = False

    def __init__(self, partEndEvent):
        self.mixer = pygame.mixer
        self.bookPartEndEvent = partEndEvent
        os.environ["SDL_VIDEODRIVER"] = "dummy"

        pygame.display.init()
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.set_volume(1)

    def play(self, fileToPlay):
        pygame.mixer.music.set_endevent(self.bookPartEndEvent)
        pygame.mixer.music.load(THIS_FOLDER + "/../book/" + fileToPlay)
        pygame.mixer.music.play()
        self.isPaused = False
        log("Playing next part: " + fileToPlay)

    def pause(self):
        if self.isPaused:
            pygame.mixer.music.unpause()
            self.isPaused = False
            log("UNPause")

            return self.isPaused
        else:
            pygame.mixer.music.pause()
            self.isPaused = True
            log("Pause")

            return self.isPaused

    def getPosition(self):
        position = round(pygame.mixer.music.get_pos() / 1000)

        log("Get position " + str(position) + "sec")
        return round(position)

    def getLength(self, musicFilePart):
        song = MP3(THIS_FOLDER + "/../book/" + musicFilePart)
        songLength = round(song.info.length)

        log("File part length " + str(songLength) + "sec")
        return songLength

    def setPosition(self, pos):
        pygame.mixer.music.set_pos(pos)

    def rewind(self):
        pygame.mixer.music.rewind()
        log('rewind?')



