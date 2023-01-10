#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    """
    Function that returns the JSON representation of an object (string)
    """
    with open(filename, mode='w') as my_json:
        json.dump(my_obj, my_json)
