from animations.animation import Animation
from animations.animations_common import hsv_to_json


class ConstColorAnimation(Animation):

    name = "const"

    def __init__(self, timing, hsv):
        super(ConstColorAnimation, self).__init__(timing)
        self.hsv = hsv

    def get_params_json(self):
        return {"hsv": hsv_to_json(self.hsv) }
