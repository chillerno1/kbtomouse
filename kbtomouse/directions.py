from math import ceil
from config import Config

class DirectionMapper(object):

    def __init__(self,):
        self.h = Config.SCREEN_HEIGHT
        self.w = Config.SCREEN_WIDTH
        self.td = Config.TRAVEL_DIST
        self.mod = Config.MODIFIER

        self.x = ceil(self.h * self.td)
        self.y = ceil(self.w * self.td)

        self.key_inputs = {
                    'left' : {'x' : -self.x, 'y' :  0},
                    'down' : {'x' :  0, 'y' :  self.y},
                    'right': {'x' :  self.x, 'y' :  0},
                    'up'   : {'x' :  0, 'y' : -self.y},
                }

    def _set_diagonals(self):
        """
        Sets diagonal coordinates (travel dist is multiplied by 3).
        """

        base_directions = [d for d in self.key_inputs]

        for first_move in base_directions:
            for second_move in base_directions:
                if first_move != second_move:
                    name = '{}+{}'.format(first_move, second_move)
                    x = (self.key_inputs[first_move]['x'] + self.key_inputs[second_move]['x']) * 3
                    y = (self.key_inputs[first_move]['y'] + self.key_inputs[second_move]['y']) * 3

                    if name not in self.key_inputs: self.key_inputs[name] = {'x' : x, 'y' : y}
    
    def _set_movement_modifier(self):
        
        inputs = [d for d in self.key_inputs if len(self.mod) > 0]

        for input in inputs:
            self.key_inputs['{}+{}'.format(self.mod, input)] = self.key_inputs[input]
            del self.key_inputs[input]

    def _set_click(self):
        self.key_inputs['ctrl+space'] = {'x': 0, 'y': 0}

    def input_map(self):
        """
        Returns a dict with relative coordinates for each key based on config.py parameters.
        """

        self._set_diagonals()
        self._set_movement_modifier()
        self._set_click()

        return self.key_inputs

    def __repr__(self):
        return "DirectionalMapper({}, {}, {}, {}, {}, {})".format(self.h, self.w, self.td, self.mod, self.x, self.y)

    def __str__(self):
        return "Init Map Vars: Height: {} Width: {} Travel Dist: {} Mod: {} X: {} Y: {}".format(self.h, self.w, self.td, self.mod, self.x, self.y)