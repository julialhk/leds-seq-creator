from animations import brightness
from infra.animations_factory import color, effect
from infra.length import short, medium, long, soft, hard, total
from infra.stored_animations import save, beat, load
from led_objects.cabbages import cabbage1, cabbage6, brain7, cup_cake4, cabbage5, cabbages, donut1, donut3, \
    brains, twists, donuts
from led_objects.flood import cup_cakes, cup_cake3, rug4, rug6
from led_objects.groups import group1, group2, group3, group4, group5, group6, group7, group8
from led_objects.led_object import all
from led_objects.flowers import flower6, flowers, paper5, papers, bottles, paper2, flower1, bottle4, bottle5
from led_objects.objects_selector import elements
from led_objects.stands import sticks8, single_sticks, sticks7, sticks3, lifas5, lifas1, lifas4, sticks, lifas, stands
from network.send_to_mqtt import send_to_mqtt, start_song
from infra.timing import song_settings, episodes, episode, cycle, cycle_beats, beats
from infra.colors import *

song_settings(bpm=73.5, beats_per_episode=16)

def yellowopening():

    elements(group5)
    cycle(beats=16)
    cycle_beats(0, 3)
    color.uniform(light_yellow_strip)
    effect.saw_tooth(1.0, False)

    elements(group1)
    cycle(beats=16)
    cycle_beats(2, 5)
    color.uniform(light_yellow_strip)
    effect.saw_tooth(1.0, False)

    elements(group6)
    cycle(beats=16)
    cycle_beats(4, 7)
    color.uniform(light_yellow_strip)
    effect.saw_tooth(1.0, False)

    elements(group2)
    cycle(beats=16)
    cycle_beats(6, 9)
    color.uniform(light_yellow_strip)
    effect.saw_tooth(1.0, False)

    elements(group4)
    cycle(beats=16)
    cycle_beats(8, 11)
    color.uniform(light_yellow_strip)
    effect.saw_tooth(1.0, False)

    elements(group7)
    cycle(beats=16)
    cycle_beats(10, 14)
    color.uniform(light_yellow_strip)
    effect.saw_tooth(1.0, False)

    elements(group3)
    cycle(beats=16)
    cycle_beats(12, 16)
    color.uniform(light_yellow_strip)
    effect.saw_tooth(1.0, False)

    elements(group8)
    cycle(beats=16)
    cycle_beats(14, 16)
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

episode(1)
effect.blink(0.4)
cycle(1)
def clapping(clapping_lights):

    elements(clapping_lights)
    cycle(beats=2)

    cycle_beats(0.0, 1.0)
    effect.saw_tooth(0.2, False)
    color.uniform(red)

    cycle_beats(1.0, 1.37)
    effect.saw_tooth(0.2, False)
    color.uniform(coral)

    cycle_beats(1.37, 1.67)
    effect.saw_tooth(0.2, False)
    color.uniform(pink_strip)

    cycle_beats(1.67, 2.0)
    effect.saw_tooth(0.2, False)
    color.uniform(light_pink_strip)

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
cycle(8)
elements(flowers, cabbages, cup_cakes,papers, donuts)
color.uniform((0.11, 0.8, 0.7))
effect.breath(0.8)




def small_bit():
    effect.hue_breath(0.4)

    elements(flower6)
    beats((16 * 7) + 0.12, (16*7) + 32)
    color.uniform(red)

    elements(cabbage1)
    beats((16*7) +0.5, (16*7) + 32)
    color.uniform(aquamarine)

    elements(lifas5.stand(3))
    beats((16*7) +1.0, (16*7) + 32)
    color.uniform(blue)

    elements(cup_cake4)
    beats((16*7) +1.37, (16*7) + 32)
    color.uniform(purple_string)

    elements(lifas4.stand(4))
    beats((16*7) +1.75, (16*7) + 32)
    color.uniform(yellow_strip)

    elements(paper2)
    beats((16*7) +2.0, (16*7) + 32)
    color.uniform(orange_string)

    elements(lifas5.stand(2))
    beats((16*7) +2.55, (16*7) + 32)
    color.uniform(light_blue)

    elements(donut3)
    beats((16*7) +3.0, (16*7) + 32)
    color.uniform(light_green)

    elements(cabbage5)
    beats((16*7) +3.34, (16*7) + 32)
    color.uniform(coral)

    elements(sticks7.stand(1))
    beats((16*7) +3.66, (16*7) + 32)
    color.uniform(blue)

    elements(flower1)
    beats((16*7) +4.12, (16*7) + 32)
    color.uniform(light_purple_string)

    elements(bottle4)
    beats((16*7) +4.5, (16*7) + 32)
    color.uniform(aquamarine)

    elements(sticks8.stand(2))
    beats((16*7) +5.0, (16*7) + 32)
    color.uniform(magenta)

    elements(cup_cake3)
    beats((16*7) +5.37, (16*7) + 32)
    color.uniform(light_pink_strip)

    elements(lifas1.stand(3))
    beats((16*7) +5.75, (16*7) + 32)
    color.uniform(light_turquoise_string)

    elements(sticks3.stand(3))
    beats((16*7) +6.0, (16*7) + 32)
    color.uniform(light_orange_strip)

    elements(lifas5. stand(1))
    beats((16*7) +6.55, (16*7) + 32)
    color.uniform(blue)

    elements(lifas4.stand(2))
    beats((16*7) +7.0, (16*7) + 32)
    color.uniform(yellow_strip)

    elements(rug4)
    beats((16*7) +7.34, (16*7) + 32)
    color.uniform(coral)

    elements(sticks7. stand(2))
    beats((16*7) +7.66, (16*7) + 32)
    color.uniform(blue)

    elements(bottle5)
    beats((16*7) +8.12, (16*7) + 32)
    color.uniform(magenta)

    elements(lifas5.stand(4))
    beats((16*7) +8.5, (16*7) + 32)
    color.uniform(aquamarine)

    elements(lifas1.stand(5))
    beats((16*7) +9.0, (16*7) + 32)
    color.uniform(turquoise_string)

    elements(sticks7.stand(6))
    beats((16*7) +9.37, (16*7) + 32)
    color.uniform(blue)

    elements(rug6)
    beats((16*7) +9.75, (16*7) + 32)
    color.uniform(turquoise_string)

    elements(sticks3.stand(1))
    beats((16*7) +10.0, (16*7) + 32)
    color.uniform(orange_string)

    elements(brain7)
    beats((16*7) +10.55, (16*7) + 32)
    color.uniform(blue)

    elements(paper5)
    beats((16*7) +11.0, (16*7) + 32)
    color.uniform(light_green)

    elements(sticks8.stand(4))
    beats((16*7) +11.34, (16*7) + 32)
    color.uniform(magenta)

    elements([sticks7.stand(2), sticks7.stand(4)])
    beats((16*7) +11.66, (16*7) + 32)
    color.uniform(blue)

    elements(lifas4.stand(1))
    beats((16*7) +12.12, (16*7) + 32)
    color.uniform(yellow_string)

    elements(sticks3.stand(2))
    beats((16*7) +12.5, (16*7) + 32)
    color.uniform(orange_string)

    elements(lifas1.stand(2))
    beats((16*7) +13.0, (16*7) + 32)
    color.uniform(turquoise_string)

    elements([sticks7.stand(3), sticks7.stand(5)])
    beats((16*7) +13.37, (16*7) + 32)
    color.uniform(blue)

    elements([sticks8.stand(3), sticks8.stand(5)])
    beats((16*7) +13.75, (16*7) + 32)
    color.uniform(magenta)

    elements(lifas4.stand(5))
    beats((16*7) +14.0, (16*7) + 32)
    color.uniform(yellow_strip)

    elements(sticks3.stand(5), sticks3.stand(4))
    beats((16*7) +14.55, (16*7) + 32)
    color.uniform(orange_string)

    elements([lifas1.stand(1), lifas1.stand(4)])
    beats((16*7) +15.0, (16*7) + 32)
    color.uniform(turquoise_string)

    elements(sticks8.stand(1))
    beats((16*7) +15.34, (16*7) + 32)
    color.uniform(magenta)

    elements(lifas4.stand(3))
    beats((16*7) +15.66, (16*7) + 32.0)
    color.uniform(yellow_strip)

episodes(7, 9)
small_bit()

episode(8)
cycle(2)
elements(all)
effect.hue_saw_tooth(0.4, True)


def quickgroupcolorchange():
    cycle(4)
    effect.breath(0.1)

    elements(group3)
    color.alternate(pink_strip, purple_strip, 5)
    cycle_beats(0.0, 0.5)

    elements(group6)
    color.alternate(indigo, magenta, 5)
    cycle_beats(0.50, 1.0)

    elements(group1)
    color.alternate(green, yellow_string, 5)
    cycle_beats(1.0, 1.5)

    elements(group4)
    color.alternate(red, purple_strip, 5)
    cycle_beats(1.5, 2.0)

    elements(group8)
    color.alternate(aquamarine, dark_blue, 5)
    cycle_beats(2.0, 2.5)

    elements(group5)
    color.alternate(orange_strip, magenta, 5)
    cycle_beats(2.5, 3.0)

    elements(group2)
    color.alternate(turquoise_string, purple_strip, 5)
    cycle_beats(3.0, 3.5)

    elements(group7)
    color.alternate(coral, yellow_string, 5)
    cycle_beats(3.5, 4.0)


episode(9)
quickgroupcolorchange()

episode(9)
cycle(4)
elements(all)
effect.hue_breath(0.4)

def wave():
    cycle(1)

    elements(flower1)
    cycle_beats(0.0, 0.05)
    effect.snake(0.4)
    color.uniform(light_green)

    elements(lifas1, cabbage1)
    cycle_beats(0.05, 0.1)
    effect.snake(0.4)
    color.uniform(light_green)

    elements(donut1)
    cycle_beats(0.1, 0.15)
    effect.snake(0.4)
    color.uniform(light_green)

    elements(sticks8, paper2, flower1)
    cycle_beats(0.15, 0.2)
    effect.snake(0.4)
    color.uniform(light_green)

    elements(cup_cake3, cabbage6, rug6)
    cycle_beats(0.2, 0.25)
    effect.snake(0.4)
    color.uniform(light_green)

    elements(sticks3, donut3, brain7)
    cycle_beats(0.25, 0.3)
    effect.snake(0.4)
    color.uniform(light_green)

    elements(sticks7, lifas4, rug4)
    cycle_beats(0.3, 0.35)
    effect.snake(0.4)
    color.uniform(light_green)

    elements(paper5)
    cycle_beats(0.35, 0.4)
    effect.snake(0.4)
    color.uniform(light_green)

    elements(cabbage6, bottle5)
    cycle_beats(0.4, 0.45)
    effect.snake(0.4)
    color.uniform(light_green)

    elements(paper5, lifas5, bottle5)
    cycle_beats(0.45, 0.5)
    effect.snake(0.4)
    color.uniform(light_green)



episode(10)
wave()
cycle(8)

send_to_mqtt("essoteric")
start_song("essoteric", 120* 1000)



