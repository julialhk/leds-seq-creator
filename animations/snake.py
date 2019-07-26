from animations.animation import Animation


class SnakeAnimation(Animation):

    name = "snake"

    def __init__(self, timing, head_pos, length, dir):
        super(SnakeAnimation, self).__init__(timing)
        self.dir = dir
        self.length = length
        self.head_pos = head_pos

    def get_params_json(self):
        return {
            "headPos": self.head_pos.to_json_obj(),
            "length": self.length.to_json_obj(),
            "dir": self.dir.to_json_obj()
        }

