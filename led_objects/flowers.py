from led_objects.led_object import LedObject

flowers = []


class Flower(LedObject):

    def __init__(self, num_pixels):
        super(Flower, self).__init__(total_pixels=num_pixels)
        flowers.append(self)


flower6 = Flower(50)
flower1 = Flower(50)

flowers = [flower1, flower6]

bottle5 = Flower(50)
bottle4 = Flower(50)

bottles = [bottle4, bottle5]

paper5 = Flower(50)
paper2 = Flower(50)

papers = [paper2, paper5]


class Fllod(LedObject):

    def __init__(self, num_pixels):
        super(Fllod, self).__init__(total_pixels=num_pixels)
        flowers.append(self)

cup_cake3 = Fllod(100)

cup_cakes = [cup_cake3]

rug6 = Fllod(11)
rug4 = Fllod(11)

rugs = [rug4, rug6]

floods = [cup_cakes, rugs]