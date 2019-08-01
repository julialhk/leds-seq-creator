import itertools

from led_objects.led_object import LedObject, SegmentProxy

stored_objects = []


def get_elements():
    global stored_objects
    return stored_objects


def should_unapack(elems):
    return any(isinstance(el, list) for el in elems)

def unpack_elements(elems):
    new_elems = []
    for elem in elems:
        if isinstance(elem, list):
            new_elems.extend(elem)
        else:
            new_elems.append(elem)
    return new_elems


def elements(*args):
    global stored_objects
    new_args = unpack_elements(args)
    while should_unapack(new_args):
        new_args = unpack_elements(new_args)
    stored_objects = [SegmentProxy(obj, obj.default_mapping()) if isinstance(args[0], LedObject) else obj for obj in new_args]
