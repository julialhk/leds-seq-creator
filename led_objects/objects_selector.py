from led_objects.led_object import LedObject, SegmentProxy

stored_objects = []


def get_elements():
    global stored_objects
    return stored_objects


def elements(*args):
    global stored_objects
    stored_objects = [SegmentProxy(obj, obj.default_mapping()) if isinstance(args[0], LedObject) else obj for obj in args]
