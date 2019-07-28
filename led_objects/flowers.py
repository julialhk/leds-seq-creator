

class CoralFlower1:
    total_pixels = 50
    mapping = {
        "rand": list(range(50))
        # "rand": [47, 0, 48, 30, 32, 49, 6, 29, 42, 7, 37, 36, 41, 17, 35, 43, 13, 31, 22, 23, 28, 20, 15, 5, 2, 27, 34,
        #          24, 4, 19, 8, 16, 14, 46, 9, 26, 45, 21, 40, 33, 38, 18, 1, 25, 11, 3, 39, 10, 44, 12]
    }

    @classmethod
    def default_mapping(cls):
        return "rand"

    animations = []
    @classmethod
    def add_animation(cls, animation):
        animation.set_pixels(cls.default_mapping())
        cls.animations.append(animation)