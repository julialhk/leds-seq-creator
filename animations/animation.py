import copy

from infra import timing, stored_animations
from led_objects.objects_selector import get_elements


class Animation:

    def __init__(self):
        self.timing = None
        self.repeat_params = None
        if stored_animations.is_recording():
            self.repeat_params = stored_animations.get_recording_timing()
        else:
            self.set_timing()
        self.pixels_name = None
        self.stored_elements = None

    def to_json_obj(self):

        json_obj = {
            "t": self.name,
            "p": self.pixels_name,
            "s": self.timing.get_start_time_ms(),
            "e": self.timing.get_end_time_ms(),
            "params": self.get_params_json()
        }

        if self.repeat_params:
            total_beats = self.timing.number_of_beats()
            curr_length_in_beats = self.repeat_params["curr_length_beats"]
            if not curr_length_in_beats:
                curr_length_in_beats = total_beats
            json_obj["rep_s"] = self.repeat_params["repeat_start_beat"] / float(curr_length_in_beats)
            json_obj["rep_e"] = self.repeat_params["repeat_end_beat"] / float(curr_length_in_beats)
            num_repeat = total_beats / curr_length_in_beats
            json_obj["rep_num"] = num_repeat
        return json_obj

    def set_timing(self):
        """ capture the current timing """
        self.timing = timing.get_timing()

    def set_pixels(self, pixels_name):
        self.pixels_name = pixels_name

    def apply(self):

        elements_to_apply = get_elements() if not self.stored_elements else self.stored_elements
        if stored_animations.is_recording():
            self.stored_elements = elements_to_apply
            stored_animations.store_animation(self)
        else:
            if not elements_to_apply:
                raise Exception("animation has no led objects to take effect on")

            for segment_proxy in elements_to_apply:
                segment_proxy.add_animation(copy.deepcopy(self))

    def create_from_template(self):
        self.timing = timing.get_timing()
        self.apply()