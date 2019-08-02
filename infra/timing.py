
""" global object - accessed from other modules """
import copy

from infra import stored_animations

tf_global = None
time_frame_factory = None


def get_timing():
    global tf_global
    return copy.deepcopy(tf_global)


class TimeFrame:

    def __init__(self, bpm, start_beat_index, number_of_beats, beats_in_cycle = None):
        self.bpm = bpm
        self.start_beat_index = start_beat_index
        self.end_beat_index = start_beat_index + number_of_beats
        self._beats_in_cycle = beats_in_cycle

    @property
    def beats_in_cycle(self):
        return self._beats_in_cycle

    @beats_in_cycle.setter
    def beats_in_cycle(self, value):
        self._beats_in_cycle = value

    @property
    def repeats(self):
        return self.number_of_beats() / self.beats_in_cycle

    def get_start_time_ms(self):
        return self.get_beat_time_ms(self.start_beat_index)

    def get_end_time_ms(self):
        return self.get_beat_time_ms(self.end_beat_index)

    def number_of_beats(self):
        return self.end_beat_index - self.start_beat_index

    def get_beat_time_ms(self, beat_index):
        return int(beat_index * self.__get_beats_per_second() * 1000.0)

    def __get_beats_per_second(self):
        return 60.0 / self.bpm


class TimeFrameFactory:

    def __init__(self, bpm, beats_per_episode):
        self.beats_per_episode = beats_per_episode
        self.bpm = bpm

    def from_beat(self, beat_start_index, beat_end_index):
        return TimeFrame(self.bpm, beat_start_index, beat_end_index)

    def episodes_length(self, episode_start_index, num_of_episodes):
        start_beat = episode_start_index * self.beats_per_episode
        num_of_beats = num_of_episodes * self.beats_per_episode
        return TimeFrame(self.bpm, start_beat, num_of_beats)

    def episodes_index(self, episode_start_index, episode_end_index):
        start_beat = episode_start_index * self.beats_per_episode
        num_of_beats = (episode_end_index - episode_start_index) * self.beats_per_episode
        return TimeFrame(self.bpm, start_beat, num_of_beats)

    def single_episode(self, episode_index):
        return self.episodes_length(episode_index, 1)


def song_settings(bpm, beats_per_episode):
    global time_frame_factory
    time_frame_factory = TimeFrameFactory(bpm, beats_per_episode)


def episodes(episode_start_index, episode_end_index):
    global time_frame_factory
    global tf_global
    tf_global = time_frame_factory.episodes_index(episode_start_index, episode_end_index)


def episode(episode_index):
    global time_frame_factory
    global tf_global
    tf_global = time_frame_factory.single_episode(episode_index)


def repeat(beats):
    global tf_global
    tf_global.beats_in_cycle = beats


