from animations import brightness
from infra.animations_factory import color, effect
from infra.length import short, medium, long, soft, hard, total
from infra.stored_animations import save, beat, load
from led_objects.she import she
from led_objects.they import they1
from network.send_to_mqtt import send_to_mqtt
from infra.timing import song_settings, episodes, episode, cycle, cycle_beats
from led_objects.objects_selector import elements
from infra.colors import *

song_settings(bpm=60, beats_per_episode=1)

#heart = [they1.part1(), they2.part4()]


episode(0)
elements(they1.part1())
color.gradient(blue, red)
cycle(1)
effect.snake()

elements(they1.part2())
color.gradient(blue, red)
cycle(1)
effect.snake(tail=1.0, switch_direction=True)

episode(1)
elements(they1.part3())
color.gradient(purple_strip, pink_strip)
cycle(1)
effect.snake()

elements(they1.part4())
color.gradient(purple_strip, pink_strip)
cycle(1)
effect.snake(tail=1.0, switch_direction=True)


send_to_mqtt("hound")



