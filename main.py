import paho.mqtt.client as mqtt
import json

from timing import Timing, TimingFactory

import colors
import animations.rainbow as rainbow
import animations.const_color as const_color
import animations.hue_shift as hue_shift
import animations.brightness as brightness
import animations.alternate as alternate

tf = TimingFactory(123, 32)

an_list = []

# 0 - 32
an_list.append(rainbow.slow_colors_mess(tf.single_episode(episode_index=0, beats_per_cycle=4)))
an_list.append(brightness.fade_in(tf.single_episode(episode_index=0, beats_per_cycle=None)))

# 32 - 64
an_list.append(rainbow.moving_full_rainbow(tf.single_episode(episode_index=1, beats_per_cycle=8)))
an_list.append(hue_shift.hue_shift_jump_on_cycle(tf.single_episode(episode_index=1, beats_per_cycle=1), 2))

# 64 - 96
an_list.append(rainbow.monochrome_to_colorful(tf.single_episode(episode_index=2, beats_per_cycle=4), hue=0.0, amp=0.5))

# 96 - 128
an_list.append(rainbow.very_colorful(tf.single_episode(episode_index=3, beats_per_cycle=4)))

# 128 - 160
timing = tf.single_episode(episode_index=4, beats_per_cycle=4)
an_list.append(rainbow.static_full_rainbow(timing))
an_list.append(brightness.on_cycle_sin(timing))

# 160 - 192
timing = tf.single_episode(episode_index=5, beats_per_cycle=2)
an_list.append(const_color.const_color_by_name(timing, colors.red))
an_list.append(alternate.change_on_cycle_adjacent_hues(timing))

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
# thing_name = "bigler"
thing_name = "amir"

animations_json = [an.to_json_obj() for an in an_list]


client = mqtt.Client("leds-seq-creator")
client.connect(host_name)

json_str = json.dumps(animations_json, separators=(',',':')) + '\0'
print(len(json_str))
print(json_str)

client.publish("animations/{}/alterego".format(thing_name), json_str)
