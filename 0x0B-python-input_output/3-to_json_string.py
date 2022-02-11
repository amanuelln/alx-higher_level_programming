#!/usr/bin/python3
"""from_json_string module.
Contains a function that returns an object represented by a JSON string.
"""
import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure)
    """
    return json.dumps(my_str)
