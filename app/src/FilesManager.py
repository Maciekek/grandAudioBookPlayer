import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))


def getAllFileNames():
    parts = os.listdir(os.path.join(THIS_FOLDER, '../book/'))
    parts.sort()
    return parts

