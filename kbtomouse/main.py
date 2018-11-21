import keyboard
import pyautogui

from threading import *
from config import Config
from directions import DirectionMapper

def key_listener(key):

    while True:
        keyboard.wait(key, suppress=True)
    
        if key == 'ctrl+space': pyautogui.click()
        else: pyautogui.moveRel(m[key]['x'], m[key]['y'])
 
if __name__ == '__main__':

    map = DirectionMapper()
    
    m = map.input_map()
    threads = [Thread(target=key_listener, kwargs={"key":key}) for key in m]

    for thread in threads:
        thread.start()