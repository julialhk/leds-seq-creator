from animations.animation import Animation
from float_func.linear import LinearFloatFunc
from float_func.sin import SinFloatFunc


class BrightnessAnimation(Animation):

    name = "brightness"

    def __init__(self, brightness_func):
        super(BrightnessAnimation, self).__init__()
        self.brightness_func = brightness_func

    def get_params_json(self):
        return {"brightness": self.brightness_func.to_json_obj() }


def on_cycle_sin(timing, phase = 0.25):
    return BrightnessAnimation(timing, SinFloatFunc.from_timing(timing, 0.0, 1.0, phase))

def fade_in(timing):
    return BrightnessAnimation(timing, LinearFloatFunc(0.0, 1.0))

def fade_out(timing):
    return BrightnessAnimation(timing, LinearFloatFunc(1.0, 0.0))