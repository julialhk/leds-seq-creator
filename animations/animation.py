
class Animation:

    def __init__(self, timing):
        self.timing = timing
        self.pixels_name = None

    def to_json_obj(self):
        return {
            "t": self.name,
            "p": self.pixels_name,
            "s": self.timing.get_start_time_ms(),
            "e": self.timing.get_end_time_ms(),
            "params": self.get_params_json()
        }

    def set_pixels(self, pixels_name):
        self.pixels_name = pixels_name