from animations.animation import Animation

import boolean_func.equal_spreads as equal_spreads
from float_func.const import ConstFloatFunc


class AlternateAnimation(Animation):

    name = "alternate"

    def __init__(self, timing, number_of_pixels, state_func, hue_shift_func):
        super(AlternateAnimation, self).__init__(timing)
        self.number_of_pixels = number_of_pixels
        self.state_func = state_func
        self.hue_shift_func = hue_shift_func

    def get_params_json(self):
        return {
            "numPix": self.number_of_pixels,
            "stateFunc": self.state_func.to_json_obj(),
            "hueShiftFunc": self.hue_shift_func.to_json_obj()
        }


def change_on_cycle_adjacent_hues(timing, number_of_pixels = 3):
    return AlternateAnimation(timing, number_of_pixels, equal_spreads.change_on_cycle(timing), ConstFloatFunc(0.1))

