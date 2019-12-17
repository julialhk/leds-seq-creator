from animations import brightness
from infra.animations_factory import color, effect
from infra.length import short, medium, long, soft, hard, total
from infra.stored_animations import save, beat, load

from network.send_to_mqtt import send_to_mqtt
from infra.timing import song_settings, episodes, episode, cycle, cycle_beats
from infra.colors import *

song_settings(bpm=120, beats_per_episode=32)



send_to_mqtt("hound")



