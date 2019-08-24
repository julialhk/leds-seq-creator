from animations import brightness
from animations.hue_shift import hue_shift_jump_on_cycle
from infra.animations_factory import color, effect
from infra.length import short, medium, long, soft, hard, total
from infra.stored_animations import save, beat, load
from led_objects.cabbages import cabbage1, cabbage6, brain7, cup_cake4, cabbage5, cabbages, donut1, donut3, \
    brains, twists, donuts
from led_objects.flood import cup_cakes
from led_objects.led_object import all
from led_objects.flowers import flower6, flowers, paper5, papers, bottles, paper2, flower1
from led_objects.objects_selector import elements
from led_objects.stands import sticks8, single_sticks, sticks7, sticks3, lifas5, lifas1, lifas4, sticks, lifas, stands, \
    single_lifas, single_stands, single_stands_per_stand
from network.send_to_mqtt import send_to_mqtt, start_song
from infra.timing import song_settings, episodes, episode, cycle, cycle_beats, beats
from infra.colors import *

song_settings(bpm=128, beats_per_episode=32, start_offset=3)

elements(all)

beats(0, 2)
color.uniform((0.0, 0.9, 1.0))
single_sticks
stands
import random
def pattern(first_beat, main_color=coral, second_color=indigo, standing_elem=sticks8):
    beats(first_beat,first_beat+8)
    cycle(8)
    offset = 0
    def turn_on_stick(first_addition, second_addition):
        curr_elem_list = single_stands_per_stand[random.randint(0, len(single_stands_per_stand)-1)]
        curr_stand = curr_elem_list[random.randint(0,len(curr_elem_list)-1)]
        cycle_beats(offset+first_addition, offset + second_addition)
        elements(curr_stand)  # standing_elem.stand(1))
        color.uniform(main_color)

    max_index_of_sticks = len(single_stands_per_stand)-1
    def pattern_inner(offset, main_color=pink_string):
        turn_on_stick(offset + 0, offset + 0.25)
        turn_on_stick(offset + 0.25, offset + 0.5)
        turn_on_stick(offset + 0.5, offset + 0.75)
        turn_on_stick(offset + 0.75, offset + 1.25)
        turn_on_stick(offset + 1.25, offset +  1.75)
        turn_on_stick(offset + 1.75, offset +  2)
        turn_on_stick(offset + 2, offset + 2.5)
        turn_on_stick(offset + 2.5, offset + 3)
        """
        
        
        curr_elem = single_stands_per_stand[random.randint(0, max_index_of_sticks)]
        cycle_beats(offset + 0.25, offset + 0.5)
        elements(curr_elem)  #elements(standing_elem.stand(2))
        color.uniform(main_color)

        curr_elem = single_stands_per_stand[random.randint(0, max_index_of_sticks)]
        cycle_beats(offset + 0.5, offset + 0.75)
        elements(curr_elem)  #elements(standing_elem.stand(3))
        color.uniform(main_color)

        curr_elem = single_stands_per_stand[random.randint(0, max_index_of_sticks)]
        cycle_beats(offset + 0.75, offset + 1.25)
        elements(curr_elem)  #elements(standing_elem.stand(4))
        color.uniform(main_color)

        curr_elem = single_stands_per_stand[random.randint(0, max_index_of_sticks)]
        cycle_beats(offset + 1.25, offset + 1.75)
        elements(curr_elem)  #elements(standing_elem.stand(5))
        color.uniform(main_color)

        curr_elem = single_stands_per_stand[random.randint(0, max_index_of_sticks)]
        cycle_beats(offset + 1.75, offset + 2)
        elements(curr_elem)  #elements(standing_elem.stand(1))
        color.uniform(main_color)

        curr_elem = single_stands_per_stand[random.randint(0, max_index_of_sticks)]
        cycle_beats(offset + 2, offset + 2.5)
        elements(curr_elem)  #elements(standing_elem.stand(2))
        color.uniform(main_color)

        curr_elem = single_stands_per_stand[random.randint(0, max_index_of_sticks)]
        cycle_beats(offset + 2.5, offset + 3)
        elements(curr_elem)  #elements(standing_elem.stand(3))
        color.uniform(main_color)
        """

    pattern_inner(0)#, standing_elem)

    turn_on_stick(3,3.5)
    """
    curr_elem = single_stands_per_stand[random.randint(0, max_index_of_sticks)]
    cycle_beats(3, 3.5)
    elements(curr_elem)  #elements(standing_elem.stand(4))
    color.uniform(second_color)
    """


    turn_on_stick(3.5,4)
    """
    curr_elem = single_stands_per_stand[random.randint(0, max_index_of_sticks)]
    cycle_beats(3.5, 4)
    elements(curr_elem)  #elements(standing_elem.stand(5))
    color.uniform(main_color)
    """
    

    pattern_inner(4)#, standing_elem)
    turn_on_stick(7, 8)
    """
    curr_elem = single_stands_per_stand[random.randint(0, max_index_of_sticks)]
    cycle_beats(7, 8)
    elements(curr_elem)  #elements(standing_elem.stand(4))
    color.uniform(main_color)
    """


pattern(2, standing_elem=sticks8, main_color=light_indigo)
pattern(10, standing_elem=sticks7, main_color=light_indigo)

"""
beats(2, 18)
color.gradient(0.0, 2.0)

cycle(8)
elements(single_stands)
cycle_beats(0, 4)
effect.snake(1.0, True)
cycle_beats(4, 8)
effect.snake(1.0, False)

"""


elements(all)

beats(18, 52)
color.uniform((0.7, 0.9, 1.0))

beats(52, 80)
color.uniform((0.2, 0.9, 1.0))

beats(80, 112)
color.uniform((0.9, 0.9, 1.0))

beats(112, 116)
color.uniform((0.6, 0.9, 1.0))

beats(116, 182)
color.uniform((0.1, 0.9, 1.0))

beats(182, 216)
color.uniform((0.8, 0.9, 1.0))

beats(216, 244)
color.uniform((0.2, 0.9, 1.0))

beats(244, 280)
color.uniform((0.7, 0.9, 1.0))

beats(280, 348)
color.uniform((0.0, 0.9, 1.0))




send_to_mqtt("under")
start_song("under", 0)


