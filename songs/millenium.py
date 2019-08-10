from animations import brightness
from infra.animations_factory import color, effect
from infra.length import short, medium, long, soft, hard, total
from infra.stored_animations import save, beat, load
from led_objects.cabbages import cabbage1, cabbage6, brain7, cup_cake4, cabbage5, cabbages, donut1, donut3, \
    brains, twists, donuts
from led_objects.flood import cup_cakes, cup_cake3
from led_objects.groups import group1, group2, group3, group4, group5, group6, group7, group8
from led_objects.led_object import all
from led_objects.flowers import flower6, flowers, paper5, papers, bottles, flower1, paper2
from led_objects.objects_selector import elements
from led_objects.stands import sticks8, single_sticks, sticks7, sticks3, lifas5, lifas1, lifas4, sticks, lifas, stands, \
    single_stands
from network.send_to_mqtt import send_to_mqtt
from infra.timing import song_settings, episodes, episode, cycle, cycle_beats, beats
from infra.colors import *

song_settings(bpm=124, beats_per_episode=64)



#ביט
episodes(0, 1)
cycle(2)
cycle_beats(0,1)
elements(group1)
color.uniform(light_coral)
effect.breath(soft)
cycle_beats(1,2)
elements(group4)
color.uniform(light_purple_string)
effect.breath(total)


# # #צפירה#
episodes (0+8/64, 1)
cycle(16)
cycle_beats(0,4)
elements(sticks)
color.gradient(0.11,0.05)
effect.breath(medium)
# ביט

episodes(1, 3)
elements(paper2,flowers,cup_cake3, bottles)
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
episodes(1, 3)
elements(single_sticks,single_stands)
cycle(32)
cycle_beats(1,7)
color.alternate(yellow_strip,orange_strip,10)
effect.snake()
cycle_beats(17,20)
color.alternate(yellow_strip,orange_strip,10)
effect.snake()


# episode3-4
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

color.uniform(red)
effect.saw_tooth(total)

beats(256,257)
elements(single_stands)
color.uniform(red)
effect.snake(1,switch_direction=True)

beats(256,262)
elements(cup_cake4,cup_cake4,cabbages,paper2)
color.uniform(yellow_string)
effect.snake(1,switch_direction=True)
#
# episodes(4.125,4.5)
# cycle(1)
# elements(all)
# color.alternate(light_pink_strip,coral)
# effect.blink()
# cycle(8)
# effect.hue_saw_tooth(edge=soft)

episodes (4.125,6)
cycle(8)

def light_one(start_beat, element):
    cycle_beats(start_beat, start_beat + 1)
    elements(element)
    color.uniform(blue)
    effect.saw_tooth(edge=soft)

light_one(0, cabbage1)
light_one(1, cabbage5)
light_one(2, brain7)
light_one(3, sticks8)
light_one(4, donut3)
light_one(5, cup_cake4)
light_one(6, paper2)
light_one(7, flower1)



elements(all)

for i in range(1, 16):
    episodes(4 + i / 8.0, 4 + (i+1) / 8.0)
    effect.hue_shift(i / 6.0)

beats(384,385)
elements(single_stands)
color.uniform(red)
effect.snake(1,switch_direction=True)



#Equalizer
episode(6)
elements(paper2,flowers,cup_cake3, bottles)
cycle(2)
cycle_beats(0,1)
color.uniform(purple_string)
cycle_beats(1,2)
color.uniform(indigo)
effect.random_saturation()

elements(stands)
cycle(1.5)
color.gradient(orange_strip[0], yellow_strip[0])
effect.snake_down_up(1.0)




#
send_to_mqtt("millenium")
# start_song("millenium", 0*1000)

#shift+fn f10-