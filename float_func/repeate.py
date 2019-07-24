
class RepeateFloatFunc:

    def __init__(self, num_of_times, func_to_repeate):
        self.num_of_times = num_of_times
        self.func_to_repeate = func_to_repeate

    @classmethod
    def from_timing(cls, timing, cycles_per_repeate, func_to_repeate):
        return cls(timing.number_of_repeats() / cycles_per_repeate, func_to_repeate)

    def to_json_obj(self):
        return {
            "t": "repeate",
            "num": self.num_of_times,
            "func": self.func_to_repeate.to_json_obj()
        }
