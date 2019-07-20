

class Cabbage1:
    name = "cabbage-1"
    total_pixels = 260
    mapping = {
        "rand": list(range(total_pixels))
    }

    @classmethod
    def default_mapping(cls):
        return "rand"

    animations = []
    @classmethod
    def add_animation(cls, animation):
        animation.set_pixels(cls.default_mapping())
        cls.animations.append(animation)
