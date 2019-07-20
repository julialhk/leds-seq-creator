import paho.mqtt.client as mqtt
import json

from timing import Timing

import colors
import animations.rainbow as rainbow
import animations.const_color as const_color
import animations.hue_shift as hue_shift
import animations.brightness as brightness

an_list = []

# 0 - 32
an_list.append(rainbow.slow_colors_mess(Timing(bpm=123, start_beat_index=0, number_of_beats=32, cycle=4)))
an_list.append(brightness.fade_in(Timing(bpm=123, start_beat_index=0, number_of_beats=32)))

# 32 - 64
an_list.append(rainbow.moving_full_rainbow(Timing(bpm=123, start_beat_index=32, number_of_beats=32, cycle=8)))
an_list.append(hue_shift.hue_shift_jump_on_cycle(Timing(bpm=123, start_beat_index=32, number_of_beats=32, cycle=1), 2))

# 64 - 96
an_list.append(rainbow.monochrome_to_colorful(Timing(bpm=123, start_beat_index=64, number_of_beats=32, cycle=4), hue=0.0, amp=0.5))

# 96 - 128
an_list.append(rainbow.very_colorful(Timing(bpm=123, start_beat_index=96, number_of_beats=32, cycle=4)))

# 128 - 160
an_list.append(rainbow.static_full_rainbow(Timing(bpm=123, start_beat_index=128, number_of_beats=32, cycle=4)))
an_list.append(brightness.on_cycle_sin(Timing(bpm=123, start_beat_index=128, number_of_beats=32, cycle=4)))

# 160 - 192
const_red_animation = const_color.const_color_by_name(Timing(bpm=123, start_beat_index=160, number_of_beats=32, cycle=4), colors.red)

#hue_shift_animation = hue_shift.hue_shift_smooth(Timing(bpm=123, start_beat_index=0, number_of_beats=512, cycle=16))
hue_shift_animation = hue_shift.hue_shift_jump_on_cycle(Timing(bpm=123, start_beat_index=0, number_of_beats=512, cycle=1), 2)

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

animation_alternate = {
    "animation_name": "alternate",
    "pixels_name": "rand",
    "start_time": 0,
    "end_time": 120000 * 4,
    "animation_params": {
        "alternate_state": {
            "type": "equal_spreads",
            "params": {
                "num_of_spreads": 123 * 4,
                "initial_state": True
            }
        },
        "num_of_pixels": 10,
        "hue_shift": {
            "type": "const",
            "params": {
                "value": 0.1
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
