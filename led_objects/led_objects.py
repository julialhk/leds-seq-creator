from infra.painting import ColorEffects
from thing_to_obj_map import all_objects


class AllObjects:

    @classmethod
    def init(cls):
        AllObjects.color = ColorEffects(cls)

    @classmethod
    def add_animation(cls, animation):
        for led_object in all_objects:
            led_object.add_animation(animation)

