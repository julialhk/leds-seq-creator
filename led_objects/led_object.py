

class LedObject:

    def __init__(self, total_pixels):
        self.total_pixels = total_pixels
        self.animations = []
        self.mapping = {"a": list(range(self.total_pixels))}

    def add_animation(self, animation):
        animation.set_pixels(self.default_mapping())
        self.animations.append(animation)

    def add_for_segment(self, segment_name, animation):

        if segment_name not in self.mapping:
            raise Exception("could not find segment with name {} in object".format(segment_name))

        animation.set_pixels(segment_name)
        self.animations.append(animation)


class SegmentProxy:

    def __init__(self, led_object, segment_name):
        self.led_object = led_object
        self.segment_name = segment_name

    def add_animation(self, animation):
        self.led_object.add_for_segment(self.segment_name, animation)
