import random

from led_objects.led_object import LedObject, SegmentProxy


class They(LedObject):

    def __init__(self):
# randomize all
        super(They, self).__init__(total_pixels=432)
        random_index = list(range(self.total_pixels))
        random.shuffle(random_index)
        self.mapping["r"] = random_index

# Point mapping
        top1 = 117 # soul 1 middle
        top2 = 333 # soul 2 middle
        bottom_1out = 0
        bottom_1in_2out = 217
        bottom_2in = 432
        top_middle1 = 74  # heart top 1 ~~~~~~~~~
        low_middle1 = 167  # heart bottom 1 ~~~~~~~~~
        top_middle2 = 313  # heart top 2 ~~~~~~~~~
        low_middle2 = 378  # heart bottom 2 ~~~~~~~~~
        intersection_1o = 90  # with 2i ~~~~~~~~~
        intersection_1i = 150  # with 2o ~~~~~~~~
        intersection_2o = 270  # with 1i ~~~~~~~~~~~~
        intersection_2i = 370  # with 1o ~~~~~~~~~~~~

# souls-full
        self.mapping["1"] = list(range(0, 217))
        self.mapping["2"] = list(reversed(range(217, 432)))

# soul 1 - sides
        self.mapping["1o"] = list(range(0, top1))
        self.mapping["1i"] = list(reversed(range(top1, 217)))

# soul 2 - sides
        self.mapping["2o"] = list(range(217, top2))
        self.mapping["2i"] = list(reversed(range(top2, 432)))

# heart - sides
        self.mapping["h1"] = list(range(top_middle1, low_middle1))
        self.mapping["h2"] = list(range(top_middle2, low_middle2))
        self.mapping["h"] = self.mapping["h1"]+list(reversed(self.mapping["h2"])) #full heart
        self.mapping["rh"] = self.mapping["h"][:]  # randomize heart
        random.shuffle(self.mapping["rh"])  # randomize heart

# flame
        self.mapping["f1o"] = list(range(bottom_1out, top_middle1))
        self.mapping["f2o"] = list(range(bottom_1in_2out, top_middle2))
        self.mapping["f1i"] = list(reversed(range(low_middle1, bottom_1in_2out)))
        self.mapping["f2i"] = list(reversed(range(low_middle2, bottom_2in)))

# kite
        self.mapping["ka"] = list(reversed(range(intersection_2i, low_middle2)))
        self.mapping["kb"] = list(range(intersection_1o, top_middle1))
        self.mapping["kc"] = list(reversed(range(intersection_2o, top_middle2)))
        self.mapping["kd"] = list(range(intersection_1i, low_middle1))
        self.mapping["k"] = self.mapping["ka"]+self.mapping["kb"]+self.mapping["kc"]+self.mapping["kd"]  # full kite - square

# lines down kite
        self.mapping["kl1o"] = list(reversed(range(70, intersection_1o)))
        self.mapping["kl1i"] = list(range(low_middle1, 190))
        self.mapping["kl2i"] = list(range(low_middle2, 420))
        self.mapping["kl2o"] = list(reversed(range(250, intersection_2o)))

# tulip
        self.mapping["tu1o"] = list(range(bottom_1out, intersection_1o))
        self.mapping["tu2o"] = list(range(bottom_1in_2out, intersection_2o))
        self.mapping["tu1i"] = list(reversed(range(intersection_1i, bottom_1in_2out)))
        self.mapping["tu2i"] = list(reversed(range(low_middle2, bottom_2in)))

# all random
    def all_random(self):
        return SegmentProxy(self, "r")
# souls general
    def soul1(self):
        return SegmentProxy(self, "1")

    def soul2(self):
        return SegmentProxy(self, "2")
# soul1 - sides
    def soul1_out(self):
        return SegmentProxy(self, "1o")

    def soul1_in(self):
        return SegmentProxy(self, "1i")
# soul2 - sides
    def soul2_in(self):
        return SegmentProxy(self, "2i")

    def soul2_out(self):
        return SegmentProxy(self, "2o")
# heart
    def heart1_half(self):
        return SegmentProxy(self, "h1")
    def heart2_half(self):
        return SegmentProxy(self, "h2")
    def heart_full(self):
        return SegmentProxy(self, "h")
    def heart_random(self):
        return SegmentProxy(self, "rh")

# flame
    def flame1_out(self):
        return SegmentProxy(self, "f1o")
    def flame2_out(self):
        return SegmentProxy(self, "f2o")
    def flame1_in(self):
        return SegmentProxy(self, "f1i")
    def flame2_in(self):
        return SegmentProxy(self, "f2i")

# Kite
    def kite(self):
        return SegmentProxy(self, "k")
    def kite_line1_out(self):
        return SegmentProxy(self, "kl1o")
    def kite_line1_in(self):
        return SegmentProxy(self, "kl1i")
    def kite_line2_in(self):
        return SegmentProxy(self, "kl2i")
    def kite_line2_out(self):
        return SegmentProxy(self, "kl2o")
# tulip
    def tulip1_out(self):
        return SegmentProxy(self, "tu1o")
    def tulip1_in(self):
        return SegmentProxy(self, "tu1i")
    def tulip2_in(self):
        return SegmentProxy(self, "tu2i")
    def tulip2_out(self):
        return SegmentProxy(self, "tu2o")



they = They()

