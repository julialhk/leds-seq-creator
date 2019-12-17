import random

from led_objects.led_object import LedObject, SegmentProxy


class They(LedObject):

    def __init__(self):
        super(They, self).__init__(total_pixels=432)

        random_index = list(range(self.total_pixels))
        random.shuffle(random_index)

        self.mapping["r"] = random_index

        self.mapping["1"] = list(range(0, 217))
        self.mapping["2"] = list(reversed(range(217, 432)))

        left_top = 117

        self.mapping["1l"] = list(range(0, left_top))
        self.mapping["1r"] = list(reversed(range(left_top, 217)))

        right_top = 333

        self.mapping["2l"] = list(range(217, right_top))
        self.mapping["2r"] = list(reversed(range(right_top, 432)))

    def random(self):
        return SegmentProxy(self, "r")

    def first(self):
        return SegmentProxy(self, "1")

    def second(self):
        return SegmentProxy(self, "2")

    def first_left(self):
        return SegmentProxy(self, "1l")

    def first_right(self):
        return SegmentProxy(self, "1r")

    def second_left(self):
        return SegmentProxy(self, "2l")

    def second_right(self):
        return SegmentProxy(self, "2r")


they = They()

