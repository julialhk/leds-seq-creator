
class Animation:

    def __init__(self, timing):
        self.timing = timing

    def to_json_obj(self):
        return {
            "t": self.name,
            "p": "rand",
            "s": self.timing.get_start_time_ms(),
            "e": self.timing.get_end_time_ms(),
            "params": self.get_params_json()
        }