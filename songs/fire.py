from animations import brightness
from infra.animations_factory import color, effect
from infra.length import short, medium, long, soft, hard, total
from infra.stored_animations import save, beat, load
from led_objects.objects_selector import elements
from led_objects.they import they

from network.send_to_mqtt import send_to_mqtt
from infra.timing import song_settings, episodes, episode, cycle, cycle_beats, beats
from infra.colors import *

song_settings(bpm=60, beats_per_episode=15)

# 🔥 flame animation
flame_out = [they.flame1_out(), they.flame2_out()]
flame_in = [they.flame1_in(), they.flame2_in()]
flame = [flame_in, flame_out]

# flames color - gradient (inner flame should be blue)
beats(0, 60)
elements(flame_out)  # outer flame color
color.gradient(0.97, 1.07)
elements(flame_in)  # inner flame color
color.gradient(0.4, 0.6)

# appearing of flames
beats(0, 4)
elements(flame)
effect.fade_in()

# burning flames
beats(4,56)
cycle(2)
elements(flame_out)
effect.breath(edge=0.7)
elements(flame_in)
cycle(2)
effect.hue_breath(edge=0.2)

# disappearing of flames
beats(56, 60)
elements(flame)
effect.fade_out()
# end of flame animation 🔥


send_to_mqtt("fire")