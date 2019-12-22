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

# Test heart
beats(0,2000)
elements(they.heart_full())
color.uniform(red)

#Test flame
# beats(10,20)
# elements(they.flame2_out(), they.flame2_in(), they.flame1_out(), they.flame1_in())
# color.uniform(red)

#Test kite
# beats(0,2000)
# elements(they.kite())
# color.uniform(red)
# elements(they.kite_line1_out(), they.kite_line1_in(), they.kite_line2_in(),they.kite_line2_out())
# color.uniform(blue)


send_to_mqtt("Test")
