from animations import brightness
from infra.animations_factory import color, effect
from infra.length import short, medium, long, soft, hard, total
from infra.stored_animations import save, beat, load
from led_objects.cabbages import cabbage1, cabbage6, brain7, cabbage5, cabbages, brains, donut1, donut3, twists, donuts
from led_objects.flood import floods
from led_objects.led_object import all
from led_objects.flowers import flower6, flowers, paper5, strings, flower1
from led_objects.objects_selector import elements
from led_objects.stands import sticks8, single_sticks, sticks7, sticks3, lifas5, lifas1, lifas4, lifas, single_lifas, \
    stands
from network.send_to_mqtt import send_to_mqtt
from infra.timing import song_settings, episodes, episode, cycle, cycle_beats
from infra.colors import *

song_settings(bpm=126, beats_per_episode=32)

episodes(0, 0.75)
elements(twists, donuts, flowers, floods, strings)
cycle(beats=2.5)
color.uniform(indigo)
effect.saw_tooth()
cycle(None)
effect.saw_tooth(edge=hard, reverse=False)

episodes(0.25, 1)
elements(stands)
cycle(beats=2)
color.uniform(red)
effect.saw_tooth()
cycle(None)
effect.saw_tooth(edge=hard, reverse=True)

episodes(1, 3)
elements(flowers)
cycle(beats=2)
color.gradient(0.61, 0.995)

cycle_beats(0, 1)
elements(flower1)
# elements(lifas1.all)
effect.blink(edge=hard)

cycle_beats(1, 2)
elements(flower6)
effect.blink(edge=hard)

episodes(1, 3)
elements(cabbages)
cycle(beats=1/3)
color.uniform(pink_strip)
effect.breath(edge=soft)


send_to_mqtt("nocturne")



