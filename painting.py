import copy

import timing
from animations import const_color
from animations.rainbow import Rainbow
from float_func.const import ConstFloatFunc


class ColorEffects:

    def __init__(self, led_object):
        self.led_object = led_object

    def uniform(self, hue, saturation=0.75, brightness=1.0):
        self.led_object.add_animation(const_color.const_color(timing.get_timing(), hue, saturation, brightness))

    def gradient(self, hue_start, hue_end):
        self.led_object.add_animation(Rainbow(timing.get_timing(), ConstFloatFunc(hue_start), ConstFloatFunc(hue_end)))

