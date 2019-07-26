import json
import paho.mqtt.client as mqtt
from thing_to_obj_map import obj_to_thing

def send_to_mqtt():
    host_name = "10.0.0.200"
    client = mqtt.Client("leds-seq-creator")
    client.connect(host_name)

    for led_object, thing_name in obj_to_thing.items():
        animations_json = [an.to_json_obj() for an in led_object.animations]
        json_str = json.dumps(animations_json, separators=(',', ':')) + '\0'
        print("sending json of size {} to thing {}".format(len(json_str), thing_name))
        client.publish("animations/{}/alterego".format(thing_name), json_str)