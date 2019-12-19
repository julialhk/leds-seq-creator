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

        top1 = 117

        self.mapping["1o"] = list(range(0, top1))
        self.mapping["1i"] = list(reversed(range(top1, 217)))

        top2 = 333

        self.mapping["2o"] = list(range(217, top2))
        self.mapping["2i"] = list(reversed(range(top2, 432)))

        top_middle1 = 102
        low_middle1 = 170

        top_middle2 = 290
        low_middle2 = 390

        self.mapping["h1"] = list(reversed(range(top_middle1, low_middle1)))
        self.mapping["h2"] = list(reversed(range(top_middle2, low_middle2)))
        self.mapping["rh"] = self.mapping["h1"]+self.mapping["h2"]
        random.shuffle(self.mapping["rh"])

    def random(self):
        return SegmentProxy(self, "r")

    def first(self):
        return SegmentProxy(self, "1")

    def second(self):
        return SegmentProxy(self, "2")

    def first_out(self):
        return SegmentProxy(self, "1o")

    def first_in(self):
        return SegmentProxy(self, "1i")

    def second_in(self):
        return SegmentProxy(self, "2i")

    def second_out(self):
        return SegmentProxy(self, "2o")

    def half1_heart(self):
        return SegmentProxy(self, "h1")

    def half2_heart(self):
        return SegmentProxy(self, "h2")

    def heart_random(self):
        return SegmentProxy(self, "rh")


they = They()

