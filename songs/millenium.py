from animations import brightness
from infra.animations_factory import color, effect
from infra.length import short, medium, long, soft, hard, total
from infra.stored_animations import save, beat, load
from led_objects.cabbages import cabbage1, cabbage6, brain7, brain4, cabbage5, cabbages, brains, donut1, donut3
from led_objects.led_object import all
from led_objects.flowers import flower6, flowers, paper5
from led_objects.objects_selector import elements
from led_objects.stands import sticks8, single_sticks, sticks7, sticks3, lifas5, lifas1, lifas4
from network.send_to_mqtt import send_to_mqtt
from infra.timing import song_settings, episodes, episode, cycle, cycle_beats
from infra.colors import *

song_settings(bpm=124, beats_per_episode=32)

episodes(0, 30)
elements(all)
color.uniform(red)
effect.breath()

# elements(sticks1)
# effect.brightness(beats_per_cycle=2, beat_feel=BeatFeel.drama_beat, energy=1.0)

# episodes(1, 2)
# elements(sticks1)
# color.uniform(red)

# for i in range(30):
#     episodes(i, i+1)
#     elements(sticks1.stick(1), flower1)
#     color.uniform(((i / 50.0), 1.0, 1.0))
#     effect.hue_shift(1 + i % 2, BeatFeel.background_beat, 0.5)

send_to_mqtt("millenium")
