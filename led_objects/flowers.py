from led_objects.led_object import LedObject

flowers = []


class Flower(LedObject):

    def __init__(self, num_pixels):
        super(Flower, self).__init__(total_pixels=num_pixels)
        flowers.append(self)


flower1 = Flower(50)
