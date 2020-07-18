import sys
import json

config = {}

def load_config(file):
    global config
    with open(file) as config_file:
        config = json.load(config_file)