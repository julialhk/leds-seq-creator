import paho.mqtt.client as mqtt
import json

from led_objects.cabbages import Cabbage1
from led_objects.coral_flowers import CoralFlower1
from led_objects.led_objects import AllObjects
from thing_to_obj_map import obj_to_thing
from timing import Timing, TimingFactory

import colors
import animations.rainbow as rainbow
import animations.const_color as const_color
import animations.hue_shift as hue_shift
import animations.brightness as brightness
import animations.alternate as alternate

tf = TimingFactory(123, 32)

CoralFlower1.add_animation(rainbow.slow_colors_mess(tf.single_episode(episode_index=0, beats_per_cycle=4)))
CoralFlower1.add_animation(brightness.fade_in(tf.single_episode(episode_index=0, beats_per_cycle=None)))

AllObjects.add_animation(rainbow.moving_full_rainbow(tf.single_episode(episode_index=1, beats_per_cycle=8)))
AllObjects.add_animation(hue_shift.hue_shift_jump_on_cycle(tf.single_episode(episode_index=1, beats_per_cycle=1), 2))

CoralFlower1.add_animation(rainbow.monochrome_to_colorful(tf.single_episode(episode_index=2, beats_per_cycle=4), hue=0.0, amp=0.5))

CoralFlower1.add_animation(rainbow.very_colorful(tf.single_episode(episode_index=3, beats_per_cycle=4)))

timing = tf.single_episode(episode_index=4, beats_per_cycle=4)
Cabbage1.add_animation(rainbow.static_full_rainbow(timing))
Cabbage1.add_animation(brightness.on_cycle_sin(timing))

timing = tf.single_episode(episode_index=5, beats_per_cycle=1)
AllObjects.add_animation(const_color.const_color_by_name(timing, colors.red))
AllObjects.add_animation(alternate.change_on_cycle_adjacent_hues(timing))

timing = tf.single_episode(episode_index=6, beats_per_cycle=1)
CoralFlower1.add_animation(const_color.const_color_by_name(timing, colors.blue))
CoralFlower1.add_animation(alternate.colors_colide(timing))

timing = tf.single_episode(episode_index=7, beats_per_cycle=4)
CoralFlower1.add_animation(const_color.const_color_by_name(timing, colors.blue))
CoralFlower1.add_animation(alternate.alternate_color_move(timing))

timing = tf.single_episode(episode_index=8, beats_per_cycle=4)
CoralFlower1.add_animation(const_color.const_color_by_name(timing, colors.blue))
CoralFlower1.add_animation(hue_shift.hue_shift_jump_on_cycle(timing))
CoralFlower1.add_animation(brightness.on_cycle_sin(timing, -0.25))


steps_on_beat_0_1 = {
    "type": "repeate",
    "params": {
        "num_of_times": 123,
        "func": {
            "type": "steps",
            "params": {
                "num_steps": 32,
                "value_diff": 1.0 / 31.0,
                "first_step_value": 0.0
            }
        }
    }
}

saw_teeth_on_beat = {
    "animation_name": "set_brightness",
    "pixels_name": "rand",
    "start_time": 0,
    "end_time": 120000 * 4,
    "animation_params": {
        "brightness": {
            "type": "repeate",
            "params": {
                "num_of_times": 123 * 2,
                "func": {
                    "type": "linear",
                    "params": {
                        "start": 1.0,
                        "end": 0.0
                    }
                }
            }
        }
    }
}

animation_fill = {
    "animation_name": "fill",
    "pixels_name": "rand",
    "start_time": 0,
    "end_time": 120000 * 4,
    "animation_params": {
        "fill_start_pos": {
            "type": "const",
            "params": {
                "value": 0.0
            }
        },
        "fill_end_pos": steps_on_beat_0_1
    }
}

#animations = [animation_rand_hue, animation_hue_shift_on_beat]
#animations = [animation_const, hue_shift_smooth, animation_brightness_on_beat]
#animations = [animation_const, animation_alternate, animation_hue_shift_on_8beat]
#animations = [animation_const, animation_hue_shift_on_beat]
#animations = [animation_const, saw_teeth_on_beat]
#animations = [rainbow_animation.to_json_obj()]

host_name = "10.0.0.200"
client = mqtt.Client("leds-seq-creator")
client.connect(host_name)

for led_object, thing_name in obj_to_thing.items():
    animations_json = [an.to_json_obj() for an in led_object.animations]
    json_str = json.dumps(animations_json, separators=(',',':')) + '\0'
    print("sending json of size {} to thing {}".format(len(json_str), thing_name))
    client.publish("animations/{}/alterego".format(thing_name), json_str)
