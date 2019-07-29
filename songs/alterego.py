from infra.animations_factory import color, effect, BeatFeel
from led_objects.cabbages import cabbage1
from led_objects.flowers import flower1
from led_objects.objects_selector import elements
from led_objects.sticks import sticks1
from network.send_to_mqtt import send_to_mqtt
from infra.timing import song_settings, episodes
from infra.colors import *

song_settings(bpm=123, beats_per_episode=32)

# save("example")
#
# beat(1.5, 2)
#
# color.uniform(red)
# effect.snake(8)
# effect.brightness(4, BeatFeel.drama_beat, 1.0)
#
# save("example")
#
#
# episodes(0, 5)
# load("example", 4)
#
# save("amit", 50*32)
#
# beat(1.5, 2)
# color.uniform(blue)
# effect.fade_out()
#
# beat(2.5, 3)
# color.uniform(red)
# effect.fade_out()
#
# save("amit")
#
#
# episodes(0, 13)
# load("amit")


episodes(0, 50)
elements(flower1)
color.alternate(red, green)

# elements(sticks1)
# effect.brightness(beats_per_cycle=2, beat_feel=BeatFeel.drama_beat, energy=1.0)

# episodes(1, 2)
# elements(sticks1)
# color.uniform(red)

for i in range(10):
    episodes(i, i+1)
    elements(sticks1.stick(1), flower1, cabbage1)
    color.uniform(((i / 30.0), 1.0, 1.0))
    effect.snake(2)
    #effect.hue_shift(4 + (i % 2) * 4, BeatFeel.background_beat, 0.5)

# CoralFlower1.add_animation(cycle.hue_shift(4, cycle.BeatFell.background_beat, 0.1))
#CoralFlower1.cycle.brightness(2, cycle.BeatFell.pair_beat, 0.2)


#AllObjects.add_animation(painting.color(0.0, 0.7))
# AllObjects.add_animation(cycle.snake(16, cycle.BeatFell.no_beat, 0.2))
# CoralFlower1.add_animation(cycle.hue_shift(2, cycle.BeatFell.pair_beat, 0.5))
# CoralFlower1.add_animation(painting.color(tf0, 0.8, 0.8))
# AllObjects.add_animation(cycle.brightness(2, cycle.BeatFell.background_beat, 0.5))
# Coral_1.add_brightness(tf0, 2, pair_beat, 0.5)

# CoralFlower1.add_animation(cycle.brightness(2, tf0, cycle.BeatFell.pair_beat, 0.5))
# CoralFlower1.add_animation(cycle.hue_shift(2, tf0, cycle.BeatFell.pair_beat, 0.2))

# tf1 = tf.single_episode(episode_index=1)
# CoralFlower1.add_animation(painting.gradient(tf1, 0.1, 0.3))
# CoralFlower1.add_animation(cycle.brightness(2, tf1, cycle.BeatFell.background_beat))
#
# tf2 = tf.single_episode(episode_index=2)
# CoralFlower1.add_animation(painting.gradient(tf2, 0.5, 0.6))
# CoralFlower1.add_animation(cycle.brightness(4, tf2, cycle.BeatFell.drama_beat))

send_to_mqtt("alterego")
