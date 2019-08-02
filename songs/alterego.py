from animations import brightness
from infra.animations_factory import color, effect
from infra.length import short, medium, long, soft, hard, total
from infra.stored_animations import save, beat, load
from led_objects.cabbages import cabbage1
from led_objects.led_object import all
from led_objects.flowers import flower1, flowers
from led_objects.objects_selector import elements
from led_objects.sticks import sticks1, single_sticks
from network.send_to_mqtt import send_to_mqtt
from infra.timing import song_settings, episodes, episode, cycle, cycle_beats
from infra.colors import *

song_settings(bpm=123, beats_per_episode=32)

episodes(0, 30)
elements(flower1)
cycle(beats=4)

cycle_beats(1.5, 2)
color.uniform((0.35, 0.9, 1.0))
effect.saw_tooth(1.0)

cycle_beats(2.5, 3)
color.uniform((0.4, 0.7, 1.0))
effect.saw_tooth(1.0)

episodes(1, 30)
effect.brightness(0.5)





episodes(1, 30)
elements(sticks1.all)
cycle(2)
color.gradient(0.3, 0.5)
effect.blink(medium)

episodes(2, 30)
effect.brightness(0.5)

send_to_mqtt("alterego")















