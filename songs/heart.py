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

# ❤️ heart animation
episodes(0,2000)
elements(they.heart1_half(), they.heart2_half())
color.gradient(0.8, 1.0)  # color

elements(they.heart_full())
cycle(30)

# Snake
cycle_beats(0, 2)
effect.snake(tail=2.0)
cycle_beats(2, 4)
effect.snake(tail=2.0)
cycle_beats(4, 6)
effect.snake(tail=2.0)
cycle_beats(6, 8)
effect.snake(tail=2.0)
cycle_beats(8, 10)
effect.snake(tail=2.0)
# breathe
cycle_beats(10, 14)
effect.breath(edge=1.0)
cycle_beats(14, 18)
effect.breath(edge=1.0)
cycle_beats(18, 22)
effect.breath(edge=1.0)
cycle_beats(22, 26)
effect.breath(edge=1.0)
cycle_beats(26, 30)
effect.breath(edge=1.0)
# end of️ heart animation ❤️

send_to_mqtt("heart")

