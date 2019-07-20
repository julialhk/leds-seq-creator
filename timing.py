from copy import deepcopy


class Timing:

    def __init__(self, bpm, start_beat_index, number_of_beats, cycle = None):
        self.bpm = bpm
        self.start_beat_index = start_beat_index
        self.end_beat_index = start_beat_index + number_of_beats
        self.cycle = cycle

    def change_cycle(self, mult_factor = 1.0):
        timing_copy = deepcopy(self)
        timing_copy.cycle /= mult_factor
        return timing_copy

    def slower2(self):
        return self.change_cycle(0.5)

    def slower4(self):
        return self.change_cycle(0.25)

    def faster2(self):
        return self.change_cycle(2)

    def faster4(self):
        return self.change_cycle(4)

    def get_start_time_ms(self):
        return self.get_beat_time_ms(self.start_beat_index)

    def get_end_time_ms(self):
        return self.get_beat_time_ms(self.end_beat_index)

    def number_of_repeats(self):
        return self.number_of_beats() / self.cycle

    def number_of_beats(self):
        return self.end_beat_index - self.start_beat_index

    def get_beat_time_ms(self, beat_index):
        return int(beat_index * self.__get_beats_per_second() * 1000.0)

    def __get_beats_per_second(self):
        return 60.0 / self.bpm