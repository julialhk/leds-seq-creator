from animations.animation import Animation


class ConstColorAnimation(Animation):

    name = "const"

    def __init__(self, timing, hue, sat, val):
        super(ConstColorAnimation, self).__init__(timing)
        self.val = val
        self.sat = sat
        self.hue = hue

    def get_params_json(self):
        return {"color": { "hue": self.hue, "sat": self.sat, "val": self.val } }


def const_color(timing, hue = 0.0, sat = 1.0, val = 1.0):
    return ConstColorAnimation(timing, hue, sat, val)

def const_color_by_name(timing, color):
    return ConstColorAnimation(timing, color["hue"], color["sat"], color["val"])
