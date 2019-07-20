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
        if not self.cycle:
            return 1
        return self.number_of_beats() / self.cycle

    def number_of_beats(self):
        return self.end_beat_index - self.start_beat_index

    def get_beat_time_ms(self, beat_index):
        return int(beat_index * self.__get_beats_per_second() * 1000.0)

    def __get_beats_per_second(self):
        return 60.0 / self.bpm


class TimingFactory:

    def __init__(self, bpm, beats_per_episode):
        self.beats_per_episode = beats_per_episode
        self.bpm = bpm

    def from_beat(self, beat_start_index, beat_end_index, cycle):
        return Timing(self.bpm, beat_start_index, beat_end_index, cycle)

    def episodes_length(self, episode_start_index, num_of_episodes, beats_per_cycle = 1):
        start_beat = episode_start_index * self.beats_per_episode
        num_of_beats = num_of_episodes * self.beats_per_episode
        return Timing(self.bpm, start_beat, num_of_beats, beats_per_cycle)

    def episodes_index(self, episode_start_index, episode_end_index, beats_per_cycle = 1):
        start_beat = episode_start_index * self.beats_per_episode
        num_of_beats = (episode_end_index - episode_start_index) * self.beats_per_episode
        return Timing(self.bpm, start_beat, num_of_beats, beats_per_cycle)

    def single_episode(self, episode_index, beats_per_cycle = 1):
        return self.episodes_length(episode_index, 1, beats_per_cycle)