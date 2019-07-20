from animations.animation import Animation
from float_func.sin import SinFloatFunc


class BrightnessAnimation(Animation):

    name = "brightness"

    def __init__(self, timing, brightness_func):
        super(BrightnessAnimation, self).__init__(timing)
        self.brightness_func = brightness_func

    def get_params_json(self):
        return {"brightness": self.brightness_func.to_json_obj() }


def on_cycle_sin(timing, hue = 0.0, sat = 1.0, val = 1.0):
    return BrightnessAnimation(timing, SinFloatFunc.from_timing(timing, 0.0, 1.0, 0.25))

