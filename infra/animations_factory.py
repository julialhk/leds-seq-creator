import copy
from enum import Enum

from infra import timing, stored_animations
from animations.alternate_coloring import AlternateColoringAnimation
from animations.brightness import BrightnessAnimation
from animations.const_color import ConstColorAnimation
from animations.hue_shift import HueShiftAnimation
from animations.rainbow import Rainbow
from animations.snake import SnakeAnimation
from boolean_func.const import ConstBooleanFunc
from float_func.comb2 import Comb2FloatFunc
from float_func.const import ConstFloatFunc
from float_func.half import HalfFloatFunc
from float_func.linear import LinearFloatFunc
from float_func.repeat import RepeatFloatFunc
from float_func.sin import SinFloatFunc
from infra.length import short, medium, long, soft, hard, total
from led_objects.objects_selector import get_elements


class ColorFactory:

    def uniform(self, color):
        ConstColorAnimation(color).apply()

    def gradient(self, hue_start, hue_end):
        Rainbow(ConstFloatFunc(hue_start), ConstFloatFunc(hue_end)).apply()

    def alternate(self, color1, color2, number_of_pixels = 3):
        AlternateColoringAnimation(color1, color2, number_of_pixels).apply()


color = ColorFactory()


class BeatFeel(Enum):
    no_beat = 1
    background_beat = 2
    weak_beat = 3
    drama_beat = 4
    pair_beat = 5


class EffectFactory:

    def brightness(self, beats_per_cycle, beat_feel, energy=1.0):
        self._brightness(beats_per_cycle, beat_feel, energy).apply()

    def hue_shift(self, beats_per_cycle, beat_feel, energy=1.0):
        self._hue_shift(beats_per_cycle, beat_feel, energy).apply()

    def snake(self, tail):
        tail_length = {short: 0.25, medium: 1.0, long: 4.0}[tail]
        SnakeAnimation(LinearFloatFunc(0.0, 1.0 + tail_length), ConstFloatFunc(tail_length), ConstBooleanFunc()).apply()

    def blink(self, edge=0.5):
        if isinstance(edge, str):
            edge = {soft: 0.25, medium: 0.5, hard: 0.75, total: 1.0}[edge]
        return BrightnessAnimation(HalfFloatFunc(ConstFloatFunc(1.0), ConstFloatFunc(1.0 - edge))).apply()

    def breath(self, edge=0.6):
        if isinstance(edge, str):
            edge = {soft: 0.4, medium: 0.6, hard: 0.8, total: 1.0}[edge]
        return BrightnessAnimation(SinFloatFunc(1.0 - edge, 1.0, -0.25, 1)).apply()

    def saw_tooth(self, edge=0.6, reverse=False):
        if isinstance(edge, str):
            edge = {soft: 0.4, medium: 0.6, hard: 0.8, total: 1.0}[edge]
        min_val = 1.0 - edge if reverse else 1.0
        max_val = 1.0 if reverse else 1.0 - edge
        return BrightnessAnimation(LinearFloatFunc(min_val, max_val)).apply()

    def hue_blink(self, edge=0.5, reverse=False):
        if isinstance(edge, str):
            edge = {soft: 0.05, medium: 0.12, hard: 0.25, total: 0.5}[edge]
        if reverse:
            edge = -edge
        return HueShiftAnimation(HalfFloatFunc(ConstFloatFunc(1.0), ConstFloatFunc(1.0 - edge))).apply()

    def hue_breath(self, edge=0.1):
        if isinstance(edge, str):
            edge = {soft: 0.03, medium: 0.1, hard: 0.2, total: 0.5}[edge]
        return HueShiftAnimation(SinFloatFunc(-edge, edge, 0.0, 1)).apply()

    def hue_saw_tooth(self, edge=0.1, reverse=False):
        if isinstance(edge, str):
            edge = {soft: 0.04, medium: 0.08, hard: 0.2, total: 0.35}[edge]
        if reverse:
            edge = -edge
        return HueShiftAnimation(LinearFloatFunc(0.0, edge)).apply()


    def _hue_shift(self, beats_per_cycle, beat_feel, energy=1.0):
        t = timing.get_timing()

        if beat_feel == BeatFeel.no_beat:
            e1 = energy * 0.5
            e2 = energy * 0.18
            func1 = SinFloatFunc.from_timing(t, beats_per_cycle * 2.57, -e1, e1, -0.25)
            func2 = SinFloatFunc.from_timing(t, beats_per_cycle * 0.88, -e2, e2, 0.15)
            return HueShiftAnimation(Comb2FloatFunc(0.3, func1, 0.7, func2))

        elif beat_feel == BeatFeel.background_beat:
            e = 0.5 * energy
            return HueShiftAnimation(SinFloatFunc.from_timing(t, beats_per_cycle, -e, e, -0.25))

        elif beat_feel == BeatFeel.weak_beat:
            zigzag = HalfFloatFunc(LinearFloatFunc(-energy * 0.5, energy * 0.5),
                                   LinearFloatFunc(energy * 0.5, -energy * 0.5))
            return HueShiftAnimation(RepeatFloatFunc.from_timing(t, beats_per_cycle, zigzag))

        elif beat_feel == BeatFeel.drama_beat:
            return HueShiftAnimation(RepeatFloatFunc.from_timing(t, beats_per_cycle,
                                                                    LinearFloatFunc(energy * 0.5, 0.0)))

        elif beat_feel == BeatFeel.pair_beat:
            on_off = HalfFloatFunc(ConstFloatFunc(0.0), ConstFloatFunc(energy * 0.5))
            return HueShiftAnimation(RepeatFloatFunc.from_timing(t, beats_per_cycle, on_off))

        raise Exception("cannot handle beat feel with value ", beat_feel)

    def _apply(self, animation):
        for led_object in get_elements():
            led_object.add_animation(copy.deepcopy(animation))


effect = EffectFactory()

