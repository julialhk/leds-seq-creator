from led_objects.led_object import LedObject, SegmentProxy

sticks = []
single_sticks = []


class Sticks(LedObject):

    def __init__(self, last_index_per_stick):
        super(Sticks, self).__init__(total_pixels=last_index_per_stick[-1])

        self.num_of_sticks = len(last_index_per_stick)

        last_index_per_stick.insert(0, 0)
        self.mapping.update({ str(i): list(range(last_index_per_stick[i-1], last_index_per_stick[i])) for i in range(1, len(last_index_per_stick))})
        sticks.append(self)
        single_sticks.append(self.all)

    def stick(self, index):
        if index < 1 or index > self.num_of_sticks:
            raise Exception("stick index {} not valid".format(index))
        return SegmentProxy(self, str(index))

    @property
    def all(self):
        return [SegmentProxy(self, str(i)) for i in range(1, self.num_of_sticks + 1)]


sticks1 = Sticks([11, 30, 45, 55, 67])
sticks2 = Sticks([17, 31, 53, 70, 91, 107])
sticks3 = Sticks([55, 107, 151, 191, 228])

lifa1 = Sticks([46, 84, 125, 159, 193])
lifa2 = Sticks([19, 47, 80, 119, 165])
lifa3 = Sticks([79, 146, 202, 257, 307]) # missing 7 - 307
