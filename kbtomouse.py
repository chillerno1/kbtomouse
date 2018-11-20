import keyboard
import math
import pyautogui
from threading import *

screen_height, screen_width = pyautogui.size()
travel_proportion = 0.01
modifier = "ctrl"

def key_listener(key):

    while True:    
        keyboard.wait(key, suppress=True)
    
        if key == 'ctrl+space': pyautogui.click()
        else: pyautogui.moveRel(m[key]['x'], m[key]['y'])

def set_directions_and_sizes():
    """
    Sets movement of cursor in proportion to screen size.
        Up, down, left and right travel at approx 1% screen size.
        Diagonal moves travel 3%.
    """

    x = math.ceil(screen_height * travel_proportion)
    y = math.ceil(screen_width * travel_proportion)

    movements = {
        'left' : {'x' : -x, 'y' : 0},
        'down' : {'x' : 0, 'y' : y},
        'right' : {'x' : x, 'y' : 0},
        'up' : {'x' : 0, 'y' : -y},
    }

    directions = [d for d in movements]

    # diagonals
    for first_move in directions:
        for second_move in directions:
            if first_move != second_move:
                name = '{}+{}'.format(first_move, second_move)
                x = (movements[first_move]['x'] + movements[second_move]['x']) * 3
                y = (movements[first_move]['y'] + movements[second_move]['y']) * 3

                if name not in movements: movements[name] = {'x' : x, 'y' : y}
    
    # adds modifier to key names
    if len(modifier) > 0:
        moves = [m for m in movements]

        for move in moves:
            movements['{}+{}'.format(modifier,move)] = movements[move]
            del movements[move]

    # adds ctrl+space for click function
    movements['ctrl+space'] = {'x': 0, 'y': 0}

    return movements
 
if __name__ == '__main__':

    m = set_directions_and_sizes()    
    threads = [Thread(target=key_listener, kwargs={"key":key}) for key in m]

    for thread in threads:
        thread.start()
