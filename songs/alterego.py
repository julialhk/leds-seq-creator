
from led_objects.led_objects import AllObjects
from send_to_mqtt import send_to_mqtt
from timing import song_settings, frame

AllObjects.init()

song_settings(bpm=123, beats_per_episode=32)

frame(0, 50)
AllObjects.color.gradient(color.red, color.orange)
frame(1, 2)
AllObjects.color.uniform(0.0)



#AllObjects.add_animation(painting.color(0.0, 0.7))
# AllObjects.add_animation(cycle.snake(4, cycle.BeatFell.no_beat, 1.0))
# CoralFlower1.add_animation(painting.color(tf0, 0.8, 0.8))
#CoralFlower1.add_animation(cycle.brightness(2, cycle.BeatFell.pair_beat, 0.5))
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
