#!/usr/bin/python3
"""save_to_json_file"""


def save_to_json_file(my_obj, filename):
    """save_to_json_file"""
    import json

    with open(filename, "w") as file:
        json.dump(my_obj, file)
