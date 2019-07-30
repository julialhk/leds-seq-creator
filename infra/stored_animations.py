

curr_an_name = None
curr_length_in_beats = None
stored_animations = {}
# tuple (start_beat, end_beat)
curr_beat = None


def is_recording():
    return curr_an_name is not None


def save(name, length_in_beats = None):

    global curr_an_name, curr_length_in_beats
    if name is not None and curr_an_name is not None and name != curr_an_name:
        raise Exception("cannot save animation '{}' while editing animation {}".format(name, curr_an_name))

    if not is_recording():
        if name in stored_animations:
            raise Exception("trying to save animation '{}' but already have one with this name stored".format(name))
        print("starting to save animation '{}' with {} beats".format(name, length_in_beats))
        curr_an_name = name
        curr_length_in_beats = length_in_beats
        stored_animations[name] = list()
    else:
        if length_in_beats is not None and length_in_beats != curr_length_in_beats:
            raise Exception("animation save called with length_in_beats {} which is differe from previous {}".format(length_in_beats, curr_length_in_beats))
        print("done saving animation '{}'".format(name))
        curr_an_name = None
        curr_length_in_beats = None


def get_recording_timing():
    global curr_length_in_beats
    return {
        "repeat_start_beat": curr_beat[0],
        "repeat_end_beat": curr_beat[1],
        "curr_length_beats": curr_length_in_beats
    }


def beat(start_beat, end_beat):
    global curr_beat, curr_length_in_beats
    if end_beat <= start_beat:
        raise Exception("end beat ({}) should be larger then start beat ({})".format(end_beat, start_beat))
    if start_beat < 0:
        raise Exception("start beat ({}) should be > 0".format(start_beat))
    if curr_length_in_beats and end_beat > curr_length_in_beats:
        raise Exception("start beat ({}) and end beat ({}) should be in range [0-{}]".format(start_beat, end_beat, curr_length_in_beats))
    curr_beat = (start_beat, end_beat)


def store_animation(animation):
    """
    appending an animation on elements on the current stored animations
    :param animation: animation to store for the current stored save
    :return:
    """
    global stored_animations, curr_an_name
    stored_animations[curr_an_name].append(animation)


def load(name):
    global stored_animations
    if name not in stored_animations:
        raise Exception("trying to load(\"{}\") but animation of that name was never saved".format(name))
    for animation in stored_animations[name]:
        animation.create_from_template()

