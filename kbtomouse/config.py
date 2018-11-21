import pyautogui

class Config(object):
    SCREEN_HEIGHT = pyautogui.size()[0]
    SCREEN_WIDTH = pyautogui.size()[1]
    TRAVEL_DIST = 0.01 # % of screen to move on each keypress
    MODIFIER = 'ctrl'
    SHOW_LOG = True
