from led_objects.led_object import LedObject

flowers = []


class Flower(LedObject):

    def __init__(self, num_pixels):
        super(Flower, self).__init__(total_pixels=num_pixels)
        flowers.append(self)


flower1 = Flower(50)
flower2 = Flower(50)

bottle1 = Flower(50)
bottle2 = Flower(50)

paper1 = Flower(50)
paper2 = Flower(50)

cup_cake = Flower(100)

rug1 = Flower(11)
rug2 = Flower(11)
