from led_objects.led_object import LedObject

cabbages = []


class Cabbage(LedObject):

    def __init__(self, num_pixels):
        super(Cabbage, self).__init__(total_pixels=num_pixels)
        cabbages.append(self)


cabbage1 = Cabbage(300)


# class Cabbage1:
#     name = "cabbage-1"
#     total_pixels = 260
#     mapping = {
#         "rand": list(range(total_pixels))
#     }
#
#     @classmethod
#     def default_mapping(cls):
#         return "rand"
#
#     animations = []
#     @classmethod
#     def add_animation(cls, animation):
#         animation.set_pixels(cls.default_mapping())
#         cls.animations.append(animation)
