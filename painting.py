from animations import const_color
from animations.alternate import AlternateAnimation
from animations.rainbow import Rainbow
from boolean_func.const import ConstBooleanFunc
from float_func.const import ConstFloatFunc


def color(timing, hue, saturation=1.0, brightness=1.0):
    return const_color.const_color(timing, hue, saturation, brightness)


def gradient(timing, hue_start, hue_end):
    return Rainbow(timing, ConstFloatFunc(hue_start), ConstFloatFunc(hue_end))

