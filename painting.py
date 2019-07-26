import copy

import timing
from animations import const_color
from animations.rainbow import Rainbow
from float_func.const import ConstFloatFunc


def color(hue, saturation=1.0, brightness=1.0):
    return const_color.const_color(timing.get_timing(), hue, saturation, brightness)


def gradient(hue_start, hue_end):
    return Rainbow(timing.get_timing(), ConstFloatFunc(hue_start), ConstFloatFunc(hue_end))

