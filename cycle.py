from animations.brightness import BrightnessAnimation
from animations.hue_shift import HueShiftAnimation
from animations.snake import SnakeAnimation
from boolean_func.const import ConstBooleanFunc
from float_func.comb2 import Comb2FloatFunc
from float_func.const import ConstFloatFunc
from float_func.half import HalfFloatFunc
from float_func.linear import LinearFloatFunc
from float_func.repeat import RepeatFloatFunc
from float_func.sin import SinFloatFunc

from enum import Enum


class BeatFell(Enum):
    no_beat = 1
    background_beat = 2
    weak_beat = 3
    drama_beat = 4
    pair_beat = 5


def brightness(beats_per_cycle, timing, beat_feel, energy = 1.0):

    if beat_feel == BeatFell.no_beat:
        func1 = SinFloatFunc.from_timing(timing, beats_per_cycle * 2.57, 1.0 - energy * 0.7, 1.0, -0.25)
        func2 = SinFloatFunc.from_timing(timing, beats_per_cycle * 0.88, 1.0 - energy * 0.5, 1.0, 0.15)
        return BrightnessAnimation(timing, Comb2FloatFunc(0.3, func1, 0.7, func2))

    elif beat_feel == BeatFell.background_beat:
        return BrightnessAnimation(timing, SinFloatFunc.from_timing(timing, beats_per_cycle, 1.0 - energy, 1.0, -0.25))

    elif beat_feel == BeatFell.weak_beat:
        zigzag = HalfFloatFunc(LinearFloatFunc(1.0 - energy, 1.0), LinearFloatFunc(1.0, 1.0 - energy))
        return BrightnessAnimation(timing, RepeatFloatFunc.from_timing(timing, beats_per_cycle, zigzag))

    elif beat_feel == BeatFell.drama_beat:
        return BrightnessAnimation(timing, RepeatFloatFunc.from_timing(timing, beats_per_cycle, LinearFloatFunc(1.0 - energy, 1.0)))

    elif beat_feel == BeatFell.pair_beat:
        on_off = HalfFloatFunc(ConstFloatFunc(1.0), ConstFloatFunc(1.0 - energy))
        return BrightnessAnimation(timing, RepeatFloatFunc.from_timing(timing, beats_per_cycle, on_off))

    raise Exception("cannot handle beat feel with value ", beat_feel)


def hue_shift(beats_per_cycle, timing, beat_feel, energy = 1.0):

    if beat_feel == BeatFell.no_beat:
        e1 = energy * 0.5
        e2 = energy * 0.18
        func1 = SinFloatFunc.from_timing(timing, beats_per_cycle * 2.57, -e1, e1, -0.25)
        func2 = SinFloatFunc.from_timing(timing, beats_per_cycle * 0.88, -e2, e2, 0.15)
        return HueShiftAnimation(timing, Comb2FloatFunc(0.3, func1, 0.7, func2))

    elif beat_feel == BeatFell.background_beat:
        e = 0.5 * energy
        return HueShiftAnimation(timing, SinFloatFunc.from_timing(timing, beats_per_cycle, -e, e, -0.25))

    elif beat_feel == BeatFell.weak_beat:
        zigzag = HalfFloatFunc(LinearFloatFunc(-energy * 0.5, energy * 0.5), LinearFloatFunc(energy * 0.5, -energy * 0.5))
        return HueShiftAnimation(timing, RepeatFloatFunc.from_timing(timing, beats_per_cycle, zigzag))

    elif beat_feel == BeatFell.drama_beat:
        return HueShiftAnimation(timing, RepeatFloatFunc.from_timing(timing, beats_per_cycle, LinearFloatFunc(energy * 0.5, 0.0)))

    elif beat_feel == BeatFell.pair_beat:
        on_off = HalfFloatFunc(ConstFloatFunc(0.0), ConstFloatFunc(energy * 0.5))
        return HueShiftAnimation(timing, RepeatFloatFunc.from_timing(timing, beats_per_cycle, on_off))

    raise Exception("cannot handle beat feel with value ", beat_feel)


def snake(beats_per_cycle, timing, beat_feel, energy = 1.0):

    tail_length = energy * 8.0
    head = RepeatFloatFunc.from_timing(timing, beats_per_cycle, LinearFloatFunc(0.0, 1.0 + tail_length))

    if beat_feel == BeatFell.no_beat:
        return SnakeAnimation(timing, head, ConstFloatFunc(tail_length), ConstBooleanFunc())

    raise Exception("cannot handle beat feel with value ", beat_feel)
