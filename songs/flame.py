from animations import brightness
from infra.animations_factory import color, effect
from infra.length import short, medium, long, soft, hard, total
from infra.stored_animations import save, beat, load
from led_objects.objects_selector import elements
from led_objects.they import they

from network.send_to_mqtt import send_to_mqtt
from infra.timing import song_settings, episodes, episode, cycle, cycle_beats
from infra.colors import *

song_settings(bpm=60, beats_per_episode=15)

episodes(0, 500)

elements(they.first(), they.second())
color.gradient(0.0, 1.0)
cycle(1)
effect.hue_shift_cycle()

# elements([they.first_left(), they.first_right(), they.second_left(), they.second_right()])
# color.gradient(0.0, 0.5)
#
# elements([they.first_left(), they.first_right(), they.second_left(), they.second_right()])
#
# cycle(5)
# effect.snake()

send_to_mqtt("flame")

