#!/usr/bin/python3
"""to_json_string"""


def to_json_string(my_obj):
    """to_json_string"""
    import json

    json_string = json.dumps(my_obj)
    return json_string
