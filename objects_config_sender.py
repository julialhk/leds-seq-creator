import paho.mqtt.client as mqtt
import json

from led_objects.coral_flowers import CoralFlower1
from led_objects.cabbages import Cabbage1

host_name = "10.0.0.200"
mqtt_client_id = "objects_map_sender"

obj_to_thing = {
    "amir": CoralFlower1,
    "bigler": Cabbage1
}

def ledObjectToJson(led_object):
    return {
        "total_pixels": led_object.total_pixels,
        "objects": led_object.mapping
    }


client = mqtt.Client(mqtt_client_id)
client.connect(host_name)

for obj_with_thing in obj_to_thing.items():
    thing_name = obj_with_thing[0]
    led_object = obj_with_thing[1]
    json_str = json.dumps(ledObjectToJson(led_object))
    topic = "objects-config/" + thing_name
    print("sending config to thing '{}'".format(thing_name))
    client.publish(topic, json_str + '\0')


