from infra.animations_factory import color
from led_objects.flowers import flower6
from led_objects.objects_selector import elements
from led_objects.stands import sticks8
from network.send_to_mqtt import send_to_mqtt
from infra.timing import song_settings, episodes
from infra.colors import *

song_settings(bpm=124, beats_per_episode=32)

episodes(0, 50)
elements(flower6, sticks8)
color.alternate(red, blue)

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
