from animations import brightness
from infra.animations_factory import color, effect
from infra.length import short, medium, long, soft, hard, total
from infra.stored_animations import save, beat, load
from led_objects.cabbages import cabbage1, cabbage6, brain7, cup_cake4, cabbage5, cabbages, donut1, donut3, \
    brains, twists, donuts
from led_objects.flood import cup_cakes
from led_objects.groups import group1, group2, group3, group4, group5, group6, group7, group8
from led_objects.led_object import all
from led_objects.flowers import flower6, flowers, paper5, papers, bottles, paper2, flower1, bottle4
from led_objects.objects_selector import elements
from led_objects.stands import sticks8, single_sticks, sticks7, sticks3, lifas5, lifas1, lifas4, sticks, lifas, stands
from network.send_to_mqtt import send_to_mqtt, start_song
from infra.timing import song_settings, episodes, episode, cycle, cycle_beats, beats
from infra.colors import *

song_settings(bpm=73.5, beats_per_episode=16)

def yellowopening():

    elements(group5)
    cycle(beats=16)
    cycle_beats(0, 1)
    color.uniform(light_yellow_strip)
    effect.saw_tooth(1.0, False)

    elements(group1)
    cycle(beats=16)
    cycle_beats(2, 3)
    color.uniform(light_yellow_strip)
    effect.saw_tooth(1.0, False)

    elements(group6)
    cycle(beats=16)
    cycle_beats(4, 5)
    color.uniform(light_yellow_strip)
    effect.saw_tooth(1.0, False)

    elements(group2)
    cycle(beats=16)
    cycle_beats(6, 7)
    color.uniform(light_yellow_strip)
    effect.saw_tooth(1.0, False)

    elements(group4)
    cycle(beats=16)
    cycle_beats(8, 9)
    color.uniform(light_yellow_strip)
    effect.saw_tooth(1.0, False)

    elements(group7)
    cycle(beats=16)
    cycle_beats(10, 11)
    color.uniform(light_yellow_strip)
    effect.saw_tooth(1.0, False)

    elements(group3)
    cycle(beats=16)
    cycle_beats(12, 13)
    color.uniform(light_yellow_strip)
    effect.saw_tooth(1.0, False)

    elements(group8)
    cycle(beats=16)
    cycle_beats(14, 15)
    color.uniform(light_yellow_strip)
    effect.saw_tooth(1.0, False)

episode(0)
yellowopening()

def coloropening():
    elements(cabbages)
    cycle(beats=16)
    cycle_beats(0, 16)
    color.uniform(coral)
    effect.saw_tooth(1.0, False)

    elements(sticks)
    cycle(beats=16)
    cycle_beats(2, 16)
    color.uniform(red)
    effect.saw_tooth(1.0, False)

    elements(flowers)
    cycle(beats=16)
    cycle_beats(4, 16)
    color.uniform(magenta)
    effect.saw_tooth(1.0, False)

    elements(brains, donuts)
    cycle(beats=16)
    cycle_beats(6, 16)
    color.uniform((0.995, 0.85, 1.0))
    effect.saw_tooth(1.0, False)

    elements(bottles)
    cycle(beats=16)
    cycle_beats(8, 16)
    color.uniform((1.0, 1.0, 1.0))
    effect.saw_tooth(1.0, False)

    elements(cup_cakes)
    cycle(beats=16)
    cycle_beats(10, 16)
    color.uniform(orange_string)
    effect.saw_tooth(1.0, False)

    elements(lifas)
    cycle(beats=16)
    cycle_beats(12, 16)
    color.uniform(pink_strip)
    effect.saw_tooth(1.0, False)

    elements(papers)
    cycle(beats=16)
    cycle_beats(14, 16)
    color.uniform(coral)
    effect.saw_tooth(1.0, False)

episode(1)
coloropening()

def clapping(clapping_lights):

    elements(clapping_lights)
    cycle(beats=2)

    cycle_beats(1.0, 1.37)
    effect.saw_tooth(0.5, False)
    color.uniform(coral)

    cycle_beats(1.37, 2.0)
    effect.saw_tooth(1.0, False)
    color.uniform(orange_strip)





episode(2)
clapping(all)

def violin1(stick_to_light):

    elements(stick_to_light.stand(3))
    cycle(beats=8)
    cycle_beats(0.0, 0.55)
    color.gradient(orange_strip[0], yellow_strip[0])
    effect.snake(1.0)


    elements(stick_to_light.stand(1))
    cycle(beats=8)
    cycle_beats(0.55, 1.0)
    color.gradient(orange_strip[0], yellow_strip[0])
    effect.snake(1.0)

    elements(stick_to_light.stand(2))
    cycle(beats=8)
    cycle_beats(1.0, 1.75)
    color.gradient(orange_strip[0], yellow_strip[0])
    effect.snake(1.0)

    elements(stick_to_light.stand(5))
    cycle(beats=8)
    cycle_beats(1.75, 2.07)
    color.gradient(orange_strip[0], yellow_strip[0])
    effect.snake(1.0)


    elements(stick_to_light.stand(2))
    cycle(beats=8)
    cycle_beats(2.07, 2.48)
    color.gradient(orange_strip[0], yellow_strip[0])
    effect.snake(1.0)

    elements(stick_to_light.stand(4))
    cycle(beats=8)
    cycle_beats(2.48, 3.0)
    color.gradient(orange_strip[0], yellow_strip[0])
    effect.snake(1.0)

    elements(stick_to_light.stand(3))
    cycle(beats=8)
    cycle_beats(3.0, 3.55)
    color.gradient(orange_strip[0], yellow_strip[0])
    effect.snake(1.0)

    elements(stick_to_light.stand(4))
    cycle(beats=8)
    cycle_beats(3.55, 4.0)
    color.gradient(orange_strip[0], yellow_strip[0])
    effect.snake(1.0)


    elements(stick_to_light.stand(3))
    cycle(beats=8)
    cycle_beats(4.0, 4.5)
    color.gradient(orange_strip[0], yellow_strip[0])
    effect.snake(1.0)


    elements(stick_to_light.stand(1))
    cycle(beats=8)
    cycle_beats(4.5, 5.0)
    color.gradient(orange_strip[0], yellow_strip[0])
    effect.snake(1.0)

    elements(stick_to_light.stand(2))
    cycle(beats=8)
    cycle_beats(5.0, 5.71)
    color.gradient(orange_strip[0], yellow_strip[0])
    effect.snake(1.0)

    elements(stick_to_light.stand(5))
    cycle(beats=8)
    cycle_beats(5.71, 6.07)
    color.gradient(orange_strip[0], yellow_strip[0])
    effect.snake(1.0)


    elements(stick_to_light.stand(2))
    cycle(beats=8)
    cycle_beats(6.07, 6.6)
    color.gradient(orange_strip[0], yellow_strip[0])
    effect.snake(1.0)

    elements(stick_to_light.stand(4))
    cycle(beats=8)
    cycle_beats(6.6, 7.0)
    color.gradient(orange_strip[0], yellow_strip[0])
    effect.snake(1.0)

    elements(stick_to_light.stand(3))
    cycle(beats=8)
    cycle_beats(7.0, 8.0)
    color.gradient(orange_strip[0], yellow_strip[0])
    effect.snake(1.0)

def violin2 (lifa_to_light):

    elements(lifa_to_light.stand(3))
    cycle(beats=8)
    cycle_beats(0.0, 0.55)
    color.gradient(purple_strip[0], indigo[0])
    effect.snake(1.0)

    elements(lifa_to_light.stand(1))
    cycle(beats=8)
    cycle_beats(0.55, 1.0)
    color.gradient(purple_strip[0], indigo[0])
    effect.snake(1.0)

    elements(lifa_to_light.stand(2))
    cycle(beats=8)
    cycle_beats(1.0, 1.55)
    color.gradient(purple_strip[0], indigo[0])
    effect.snake(1.0)

    elements(lifa_to_light.stand(5))
    cycle(beats=8)
    cycle_beats(1.55, 2.07)
    color.gradient(purple_strip[0], indigo[0])
    effect.snake(1.0)


    elements(lifa_to_light.stand(2))
    cycle(beats=8)
    cycle_beats(2.07, 2.48)
    color.gradient(purple_strip[0], indigo[0])
    effect.snake(1.0)

    elements(lifa_to_light.stand(4))
    cycle(beats=8)
    cycle_beats(2.48, 3.0)
    color.gradient(purple_strip[0], indigo[0])
    effect.snake(1.0)

    elements(lifa_to_light.stand(3))
    cycle(beats=8)
    cycle_beats(3.0, 3.55)
    color.gradient(purple_strip[0], indigo[0])
    effect.snake(1.0)

    elements(lifa_to_light.stand(4))
    cycle(beats=8)
    cycle_beats(3.55, 4.0)
    color.gradient(purple_strip[0], indigo[0])
    effect.snake(1.0)

    elements(lifa_to_light.stand(3))
    cycle(beats=8)
    cycle_beats(4.0, 4.55)
    color.gradient(purple_strip[0], indigo[0])
    effect.snake(1.0)

    elements(lifa_to_light.stand(1))
    cycle(beats=8)
    cycle_beats(4.55, 5.0)
    color.gradient(purple_strip[0], indigo[0])
    effect.snake(1.0)

    elements(lifa_to_light.stand(2))
    cycle(beats=8)
    cycle_beats(5.0, 5.55)
    color.gradient(purple_strip[0], indigo[0])
    effect.snake(1.0)

    elements(lifa_to_light.stand(5))
    cycle(beats=8)
    cycle_beats(5.55, 6.07)
    color.gradient(purple_strip[0], indigo[0])
    effect.snake(1.0)

    elements(lifa_to_light.stand(3))
    cycle(beats=8)
    cycle_beats(6.0, 6.55)
    color.gradient(purple_strip[0], indigo[0])
    effect.snake(1.0)

    elements(lifa_to_light.stand(2))
    cycle(beats=8)
    cycle_beats(6.55, 7.00)
    color.gradient(purple_strip[0], indigo[0])
    effect.snake(1.0)

    elements(lifa_to_light.stand(3))
    cycle(beats=8)
    cycle_beats(7.0, 8.0)
    color.gradient(purple_strip[0], indigo[0])
    effect.snake(1.0)


episodes(3, 7)
violin1(sticks3)

episodes(4, 7)
violin1(sticks8)

episodes(4, 7)
violin1(sticks7)

episodes(5, 7)
violin2(lifas5)
violin2(lifas1)
violin2(lifas4)


episodes(5, 7)
clapping(cabbages)


def small_bit():
    effect.hue_breath(0.2)
    cycle(beats=16)

    elements(flower6)
    cycle_beats(0.12, 0.5)
    color.gradient(red[0], blue[0])

    elements(cabbage1)
    cycle_beats(0.5, 1.0)
    color.gradient(aquamarine[0], indigo[0])

    elements(paper5)
    cycle_beats(1.0, 1.37)
    color.gradient(green[0], indigo[0])

    elements(cup_cake4)
    cycle_beats(1.37, 1.75)
    color.gradient(purple_string[0], aquamarine[0])

    elements(brain7)
    cycle_beats(1.75, 2.0)
    color.gradient(turquoise_string[0], yellow_string[0])

    elements(paper2)
    cycle_beats(2.0, 2.55)
    color.gradient(orange_string[0], purple_string[0])

    elements(lifas5.stand(2))
    cycle_beats(2.55, 3.0)
    color.gradient(blue[0], magenta[0])

    elements(donut3)
    cycle_beats(3.0, 3.34)
    color.gradient(green[0], indigo[0])

    elements(cabbage5)
    cycle_beats(3.34, 3.66)
    color.gradient(coral[0], yellow_string[0])

    elements(sticks7.stand(1))
    cycle_beats(3.66, 4.12)
    color.gradient(blue[0], magenta[0])

    elements(flower6)
    cycle_beats(4.12, 4.5)
    color.gradient(purple_strip[0], red[0])

    elements(bottle4)
    cycle_beats(4.5, 5.0)
    color.gradient(aquamarine[0], indigo[0])

    elements(sticks7.stand(1))
    cycle_beats(5.0, 5.37)
    color.gradient(green[0], indigo[0])

    elements(cup_cake4)
    cycle_beats(5.37, 5.75)
    color.gradient(orange_string[0], purple_string[0])

    elements(brain7)
    cycle_beats(5.75, 6.0)
    color.gradient(turquoise_string[0], yellow_string[0])

    elements(paper2)
    cycle_beats(6.0, 6.55)
    color.gradient(orange_string[0], aquamarine[0])

    elements(lifas5)
    cycle_beats(6.55, 7.0)
    color.gradient(blue[0], magenta[0])

    elements(donut3)
    cycle_beats(7.0, 7.34)
    color.gradient(green[0], indigo[0])

    elements(cabbage5)
    cycle_beats(7.34, 7.66)
    color.gradient(coral[0], yellow_string[0])

    elements(sticks7.stand(1))
    cycle_beats(7.66, 8.12)
    color.gradient(blue[0], yellow_string[0])

    elements(flower6)
    cycle_beats(8.12, 8.5)
    color.gradient(red[0], blue[0])

    elements(cabbage1)
    cycle_beats(8.5, 9.0)
    color.gradient(aquamarine[0], indigo[0])

    elements(paper5)
    cycle_beats(9.0, 9.37)
    color.gradient(green[0], indigo[0])

    elements(cup_cake4)
    cycle_beats(9.37, 9.75)
    color.gradient(purple_string[0], aquamarine[0])

    elements(brain7)
    cycle_beats(9.75, 10.0)
    color.gradient(turquoise_string[0], yellow_string[0])

    elements(paper2)
    cycle_beats(10.0, 10.55)
    color.gradient(orange_string[0], purple_string[0])

    elements(sticks8.stand(1))
    cycle_beats(10.55, 11.0)
    color.gradient(blue[0], magenta[0])

    elements(lifas5.stand(1))
    cycle_beats(11.0, 11.34)
    color.gradient(green[0], indigo[0])

    elements(donut1)
    cycle_beats(11.34, 11.66)
    color.gradient(coral[0], yellow_string[0])

    elements(sticks7.stand(2))
    cycle_beats(11.66, 12.12)
    color.gradient(green[0], yellow_string[0])

    elements(flower1)
    cycle_beats(12.12, 12.5)
    color.gradient(red[0], yellow_string[0])

    elements(cabbage5)
    cycle_beats(12.5, 13.0)
    color.gradient(aquamarine[0], indigo[0])

    elements(paper5)
    cycle_beats(13.0, 13.37)
    color.gradient(green[0], indigo[0])

    elements(cup_cake4)
    cycle_beats(13.37, 13.75)
    color.gradient(purple_string[0], yellow_string[0])

    elements(brain7)
    cycle_beats(13.75, 14.0)
    color.gradient(turquoise_string[0], yellow_string[0])

    elements(paper2)
    cycle_beats(14.0, 14.55)
    color.gradient(orange_string[0], purple_string[0])

    elements(lifas5)
    cycle_beats(14.55, 15.0)
    color.gradient(blue[0], magenta[0])

    elements(donut3)
    cycle_beats(15.0, 15.34)
    color.gradient(aquamarine[0], indigo[0])

    elements(cabbage5)
    cycle_beats(15.34, 15.66)
    color.gradient(coral[0], yellow_string[0])

    elements(sticks7.stand(1))
    cycle_beats(15.66, 16.0)
    color.gradient(turquoise_string[0], yellow_string[0])

episode(7)
small_bit()




send_to_mqtt("essoteric")
start_song("essoteric")



