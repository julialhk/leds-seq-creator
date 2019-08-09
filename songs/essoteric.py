from animations import brightness
from infra.animations_factory import color, effect
from infra.length import short, medium, long, soft, hard, total
from infra.stored_animations import save, beat, load
from led_objects.cabbages import cabbage1, cabbage6, brain7, brain4, cabbage5, cabbages, brains, donut1, donut3
from led_objects.groups import group4, group2, group6, group1, group8, group3, group7, group5
from led_objects.led_object import all
from led_objects.flowers import flower6, flowers, paper5
from led_objects.objects_selector import elements
from led_objects.stands import sticks8, single_sticks, sticks7, sticks3, lifas5, lifas1, lifas4
from network.send_to_mqtt import send_to_mqtt
from infra.timing import song_settings, episodes, episode, cycle, cycle_beats
from infra.colors import *

song_settings(bpm=73.5, beats_per_episode=16)

episode(0)
elements(group5)
cycle(beats=16)

cycle_beats(0, 1)
color.uniform(light_yellow_strip)
effect.saw_tooth(1.0, True)

episode(0)
elements(group1)
cycle(beats=16)

cycle_beats(2, 3)
color.uniform(light_yellow_strip)
effect.saw_tooth(1.0, True)

episode(0)
elements(group6)
cycle(beats=16)

cycle_beats(4, 5)
color.uniform(light_yellow_strip)
effect.saw_tooth(1.0, True)

episode(0)
elements(group2)
cycle(beats=16)

cycle_beats(6, 7)
color.uniform(light_yellow_strip)
effect.saw_tooth(1.0, True)

episode(0)
elements(group4)
cycle(beats=16)

cycle_beats(8, 9)
color.uniform(light_yellow_strip)
effect.saw_tooth(1.0, True)

episode(0)
elements(group7)
cycle(beats=16)

cycle_beats(10, 11)
color.uniform(light_yellow_strip)
effect.saw_tooth(1.0, True)

episode(0)
elements(group3)
cycle(beats=16)

cycle_beats(12, 13)
color.uniform(light_yellow_strip)
effect.saw_tooth(1.0, True)

episode(0)
elements(group8)
cycle(beats=16)

cycle_beats(14, 15)
color.uniform(light_yellow_strip)
effect.saw_tooth(1.0, True)

episode(1)
elements(group5)
cycle(beats=16)

cycle_beats(0, 16)
color.uniform(light_orange_strip)
effect.saw_tooth(1.0, True)

episode(1)
elements(group1)
cycle(beats=16)

cycle_beats(2, 16)
color.uniform(light_coral)
effect.saw_tooth(1.0, True)

episode(1)
elements(group6)
cycle(beats=16)

cycle_beats(4, 16)
color.uniform(light_pink_strip)
effect.saw_tooth(1.0, True)

episode(1)
elements(group2)
cycle(beats=16)

cycle_beats(6, 16)
color.uniform(light_purple_string)
effect.saw_tooth(1.0, True)

episode(1)
elements(group4)
cycle(beats=16)

cycle_beats(8, 16)
color.uniform(purple_string)
effect.saw_tooth(1.0, True)

episode(1)
elements(group7)
cycle(beats=16)

cycle_beats(10, 16)
color.uniform(blue)
effect.saw_tooth(1.0, True)

episode(1)
elements(group3)
cycle(beats=16)

cycle_beats(12, 16)
color.uniform(light_blue)
effect.saw_tooth(1.0, True)

episode(1)
elements(group8)
cycle(beats=16)

cycle_beats(14, 16)
color.uniform(aquamarine)
effect.saw_tooth(1.0, True)

episode(2)
elements(all)
cycle(beats=2)

cycle_beats(1.0 + 0.3/0.8, 1.0 + 0.4/0.8)
color.gradient(blue[0], aquamarine[0])
effect.saw_tooth(1.0)

cycle_beats(1.0 , 1.3)
color.gradient(green[0], blue[0])
effect.saw_tooth(1.0)

cycle_beats(1.0 + 0.5/0.8, 1.0 + 0.65/0.8)
color.gradient(blue[0], aquamarine[0])
effect.saw_tooth(1.0)

episodes(3, 7)
elements(sticks8.stand(3))
cycle(beats=8)
cycle_beats(0.0, 0.55)
color.gradient(coral[0], orange_strip[0])
effect.breath(medium)

episodes(3, 7)
elements(sticks8.stand(1))
cycle(beats=8)
cycle_beats(0.55, 1.0)
color.gradient(coral[0], orange_strip[0])
effect.breath(medium)

episodes(3, 7)
elements(sticks8.stand(2))
cycle(beats=8)
cycle_beats(1.0, 1.67)
color.gradient(coral[0], orange_strip[0])
effect.breath(medium)


cycle(beats=2)

episodes(3, 7)
elements(sticks8.stand(5))
cycle(beats=8)
cycle_beats(1.67, 2.1)
color.gradient(coral[0], orange_strip[0])
effect.breath(medium)
episodes(5, 6)
elements(flowers)
cycle(beats=2)


episodes(3, 7)
elements(sticks8.stand(2))
cycle(beats=8)
cycle_beats(2.1, 2.37)
color.gradient(coral[0], orange_strip[0])
effect.breath(medium)

episodes(3, 7)
elements(sticks8.stand(4))
cycle(beats=8)
cycle_beats(2.37, 2.92)
color.gradient(coral[0], orange_strip[0])
effect.breath(medium)

episodes(3, 7)
elements(sticks8.stand(3))
cycle(beats=8)
cycle_beats(2.92, 3.47)
color.gradient(coral[0], orange_strip[0])
effect.breath(medium)


episodes(3, 7)
elements(sticks8.stand(4))
cycle(beats=8)
cycle_beats(3.47, 4.0)
color.gradient(coral[0], orange_strip[0])
effect.breath(medium)

episodes(5, 7)
elements(sticks7.stand(3))
cycle(beats=8)
cycle_beats(0.0, 0.55)
color.gradient(coral[0], orange_strip[0])
effect.breath(medium)

episodes(5, 7)
elements(sticks7.stand(1))
cycle(beats=8)
cycle_beats(0.0 + 0.55, 1.0)
color.gradient(coral[0], orange_strip[0])
effect.breath(medium)

episodes(5, 7)
elements(sticks7.stand(2))
cycle(beats=8)
cycle_beats(1.0, 1.0 + 0.37)
color.gradient(coral[0], orange_strip[0])
effect.breath(medium)

episodes(5, 7)
elements(sticks7.stand(3))
cycle(beats=8)
cycle_beats(1.37, 1.67)
color.gradient(coral[0], orange_strip[0])
effect.breath(medium)

episodes(5, 7)
elements(sticks7.stand(3))
cycle(beats=8)
cycle_beats(1.65, 2.0)
color.gradient(coral[0], orange_strip[0])
effect.breath(medium)

episodes(5, 7)
elements(sticks7.stand(2))
cycle(beats=8)
cycle_beats(2.0, 2.37)
color.gradient(coral[0], orange_strip[0])
effect.breath(medium)

episodes(5, 7)
elements(sticks7.stand(4))
cycle(beats=8)
cycle_beats(2.37, 2.92)
color.gradient(coral[0], orange_strip[0])
effect.breath(medium)

episodes(5, 7)
elements(sticks7.stand(3))
cycle(beats=8)
cycle_beats(2.92, 3.47)
color.gradient(coral[0], orange_strip[0])
effect.breath(medium)


episodes(5, 6)
elements(flowers)
cycle(beats=2)
cycle_beats(1.0 + 0.3/0.8, 1.0 + 0.4/0.8)
color.gradient(blue[0], aquamarine[0])
effect.saw_tooth(1.0)

cycle_beats(1.0 , 1.3)
color.gradient(green[0], blue[0])
effect.saw_tooth(1.0)

cycle_beats(1.0 + 0.5/0.8, 1.0 + 0.65/0.8)
color.gradient(blue[0], aquamarine[0])
effect.saw_tooth(1.0)




send_to_mqtt("essoteric")



