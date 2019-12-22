import random

from led_objects.led_object import LedObject, SegmentProxy


class Gate(LedObject):

    def __init__(self):
# randomize all
        super(Gate, self).__init__(total_pixels=333)


gate1 = Gate()
gate2 = Gate()

