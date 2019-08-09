from animations import brightness
from infra.animations_factory import color, effect
from infra.length import short, medium, long, soft, hard, total
from infra.stored_animations import save, beat, load
from led_objects.cabbages import cabbage1, cabbage6, brain7, cup_cake4, cabbage5, cabbages, donut1, donut3, \
    brains, twists, donuts
from led_objects.flood import cup_cakes
from led_objects.led_object import all
from led_objects.flowers import flower6, flowers, paper5, papers, bottles
from led_objects.objects_selector import elements
from led_objects.stands import sticks8, single_sticks, sticks7, sticks3, lifas5, lifas1, lifas4, sticks, lifas, stands
from network.send_to_mqtt import send_to_mqtt
from infra.timing import song_settings, episodes, episode, cycle, cycle_beats, beats
from infra.colors import *

song_settings(bpm=124, beats_per_episode=64)
#ביט
episodes(0, 1)
cycle(2)
cycle_beats(0,1)
elements(cup_cake3)
color.uniform(light_blue)
effect.breath(soft)
cycle_beats(1,2)
elements(flower1)
color.uniform(light_green)
effect.breath(total)

# # #צפירה#
episodes(9/64,61/64)
cycle(16)
cycle_beats(1,4)
elements(stands)
color.alternate(yellow_strip,orange_strip,10)
effect.breath(medium)
# ביט
episodes(1, 2)
elements(flower1,flower6)
cycle(2)
cycle_beats(0,1)
color.uniform(yellow_string)
cycle_beats(1,2)
color.uniform(red)
effect.saw_tooth (total)

# episodes(1, 2)
# elements(stands)
# cycle(32)
# cycle_beats(2,7)
# color.alternate(yellow_strip,orange_strip,10)
# effect.breath(medium)
#
# cycle_beats(17,20)
# color.alternate(yellow_strip,orange_strip,10)

episodes(2.625,3.875)
elements(stands)
cycle(8)
color.uniform(light_aquamarine)
effect.saw_tooth(soft)
cycle(None)
effect.hue_saw_tooth(3.0)
# cycle(8)
# color.uniform(light_coral)
# effect.saw_tooth(soft)
# cycle(8)
# color.uniform(light_blue)
# effect.saw_tooth(soft)
# cycle(8)
# color.uniform(light_turquoise_strip)
# effect.saw_tooth(soft)
# cycle(8)
# color.uniform(light_green)
# effect.saw_tooth(soft)
# cycle(8)
# color.uniform(aquamarine)
# effect.saw_tooth(medium)
# cycle(8)
# color.uniform(coral)
# effect.saw_tooth(medium)
# cycle(8)
# color.uniform(turquoise_strip)
# effect.saw_tooth(medium)
# cycle(8)
# color.uniform(blue)
# effect.saw_tooth(medium)
# cycle(8)
# color.uniform(dark_green)
# effect.saw_tooth(hard)
# cycle(8)
# color.uniform(dark_blue)
# effect.saw_tooth(hard)



#
send_to_mqtt("millenium")

#shift+fn f10-