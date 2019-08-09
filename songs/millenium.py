from animations import brightness
from infra.animations_factory import color, effect
from infra.length import short, medium, long, soft, hard, total
from infra.stored_animations import save, beat, load
from led_objects.cabbages import cabbage1, cabbage6, brain7, cup_cake4, cabbage5, cabbages, donut1, donut3, \
    brains, twists, donuts
from led_objects.flood import cup_cakes, cup_cake3
from led_objects.groups import group1, group2, group3, group4, group5, group6, group7, group8
from led_objects.led_object import all
from led_objects.flowers import flower6, flowers, paper5, papers, bottles, flower1
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
color.uniform(light_coral)
effect.breath(soft)
cycle_beats(1,2)
elements(flower1)
color.uniform(light_purple_string)
effect.breath(total)


# # #צפירה#
beats(9,61)
cycle(16)
cycle_beats(1,4)
elements(sticks)
color.gradient(0.74,0.98)
effect.breath(medium)
# ביט

episodes(1, 4)
elements(flower1,flower6)
cycle(2)
cycle_beats(0,1)
color.uniform(purple_string)
cycle_beats(1,2)
color.uniform(indigo)
effect.random_saturation()

episodes(2, 3)
elements(cabbages)
cycle(1/3)
color.uniform(light_pink_strip)
effect.breath(soft)


#effect.saw_tooth (medium)

#צפירה
episodes(1, 2)
elements(single_sticks)
cycle(32)
cycle_beats(1,7)
color.alternate(yellow_strip,orange_strip,10)
effect.snake()
cycle_beats(17,20)
color.alternate(yellow_strip,orange_strip,10)
effect.snake()


# beats(186,248)
wanted_elements = [group1, group2, group3, group4, group5, group6, group7, group8]
current_elements = []
current_beat = 192
for element in wanted_elements:
    current_elements.append(element)
    beats(current_beat, current_beat + 8)
    cycle(1/2)
    elements(current_elements)
    color.uniform(indigo)
    effect.saw_tooth(soft)
    current_beat += 8

color.uniform(purple)
effect.saw_tooth(total)

#
# beats(210,218)
# elements(stands)
# color.uniform(light_blue)
# effect.saw_tooth(soft)
#
# beats(218,226)
# elements(stands)
# color.uniform(light_turquoise_strip)
# effect.saw_tooth(soft)
#
# beats(226,234)
# elements(stands)
# color.uniform(light_green)
# effect.saw_tooth(soft)
#
#
# beats(234,242)
# elements(stands)
# color.uniform(aquamarine)
# effect.saw_tooth(medium)
#
#
# beats(242,250)
# elements(stands)
# color.uniform(coral)
# effect.saw_tooth(medium)
#
#
# beats(250,258)
# elements(stands)
# color.uniform(turquoise_strip)
# effect.saw_tooth(medium)
#
#
# beats(258,266)
# elements(stands)
# color.uniform(blue)
# effect.saw_tooth(medium)
#
#
# beats(266,274)
# elements(stands)
# color.uniform(dark_green)
# effect.saw_tooth(hard)
#
# beats(274,282)
# elements(stands)
# color.uniform(dark_blue)
# effect.saw_tooth(hard)



#
send_to_mqtt("millenium")

#shift+fn f10-