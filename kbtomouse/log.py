from config import Config

def info(message):
    if Config.SHOW_LOG == True: print("[info] :: {}".format(message))