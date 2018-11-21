import pyautogui

class Config(object):
    """
    Note: 
        TRAVEL_DIST: is the percentage of screen size to move on each keypress (i.e. 1 = 1%).
                     diagonal moves multiply this by 3 for ease of moving around.  
        MODIFIER: Can be set to 'alt', 'ctrl', 'shift' etc. 
        SHOW_LOG: Enables console logging of inputs.
    """
    
    SCREEN_HEIGHT = pyautogui.size()[0]
    SCREEN_WIDTH = pyautogui.size()[1]
    TRAVEL_DIST = 1
    MODIFIER = 'ctrl'
    SHOW_LOG = True