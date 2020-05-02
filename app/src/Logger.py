import logging
import os 

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

def loggerInit():
    logger = logging.getLogger('grand_audio_book_player')
    hdlr = logging.FileHandler(THIS_FOLDER + '/../logs/log.log')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.DEBUG)


def log(text):
    logger = logging.getLogger('grand_audio_book_player')
    print(text)
    logger.info(text)

def error(text):
    logger = logging.getLogger('grand_audio_book_player')
    print(text)
    logger.error(text)


