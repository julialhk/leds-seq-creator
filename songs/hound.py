from animations import brightness
from infra.animations_factory import color, effect
from infra.length import short, medium, long, soft, hard, total
from infra.stored_animations import save, beat, load
from led_objects.she import she
from led_objects.they import they
from network.send_to_mqtt import send_to_mqtt
from infra.timing import song_settings, episodes, episode, cycle, cycle_beats, beats
from led_objects.objects_selector import elements
from infra.colors import *

song_settings(bpm=60, beats_per_episode=20)


# 👻👻 souls animation
beats(0, 20)
cycle(4)
cycle_beats(0,2)
elements(they.soul1_out(), they.soul1_in())  # soul 1 pulse # ☺️ add head
color.gradient(0.3, 0.7)
effect.snake(tail=3.0)

cycle_beats(2,4)
elements(they.soul2_out(), they.soul2_in()) # soul 2 pulse # ☺️ add head
color.gradient(0.7, 1.2)
effect.snake(tail=3.0)

beats(20,60)
elements(they.soul1(), they.soul2())
color.gradient(0.0, 3.0)

beats(20, 22)
effect.fill()

beats(22, 60)
effect.hue_saw_tooth(edge=20.0)

beats(50,60)
elements(they.all_random())
effect.snake_out(tail=1.0)


send_to_mqtt("hound")



