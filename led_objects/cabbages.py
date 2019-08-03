from led_objects.led_object import LedObject

cabbages = []


class Cabbage(LedObject):

    def __init__(self, num_pixels):
        super(Cabbage, self).__init__(total_pixels=num_pixels)
        cabbages.append(self)


cabbage1 = Cabbage(260)
cabbage2 = Cabbage(300)
cabbage3 = Cabbage(300)

brain1 = Cabbage(299)
brain2 = Cabbage(300)

donut1 = Cabbage(296)
donut2 = Cabbage(296)
