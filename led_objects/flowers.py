from led_objects.led_object import LedObject


class Flower(LedObject):

    def __init__(self, num_pixels):
        super(Flower, self).__init__(total_pixels=num_pixels)

    @classmethod
    def default_mapping(cls):
        return "a"


flower1 = Flower(50)