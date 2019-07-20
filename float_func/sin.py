
class SinFloatFunc:

    def __init__(self, min_value, max_value, phase, repeats):
        """ Initialize sin function with explicit paramters """
        self.min_value = min_value
        self.max_value = max_value
        self.phase = phase
        self.repeats = repeats

    @classmethod
    def from_timing(cls, timing, min_value, max_value, phase):
        return cls(min_value, max_value, phase, timing.number_of_repeats())

    def to_json_obj(self):
        return {
            "t": "sin",

            "min": self.min_value,
            "max": self.max_value,
            "phase": self.phase,
            "rep": self.repeats
        }
