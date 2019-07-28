from led_objects.led_object import LedObject, SegmentProxy


class Sticks(LedObject):

    def __init__(self, last_index_per_stick):
        super(Sticks, self).__init__(total_pixels=last_index_per_stick[-1])

        self.num_of_sticks = len(last_index_per_stick)

        last_index_per_stick.insert(0, 0)
        self.mapping.update({ str(i): list(range(last_index_per_stick[i-1], last_index_per_stick[i])) for i in range(1, len(last_index_per_stick))})

    @classmethod
    def default_mapping(cls):
        return "a"

    def stick(self, index):
        if index < 1 or index > self.num_of_sticks:
            raise Exception("stick index {} not valid".format(index))
        return SegmentProxy(self, str(index))


sticks1 = Sticks([11, 30, 45, 55, 67])
