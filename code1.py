import os


def criaPasta(pasta):
    if os.path.exists(pasta)==False:
        os.makedirs(pasta)

