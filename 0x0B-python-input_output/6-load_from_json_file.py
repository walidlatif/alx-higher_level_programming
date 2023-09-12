#!/usr/bin/python3
'''Module : load_from_json_file '''
import json


def load_from_json_file(filename):
    '''
    Returns:
        returns an object (Python data structure)
        represented by a JSON string
    '''
    with open(filename, 'r') as f:
        json_obj = f.read()
        python_obj = json.loads(json_obj)
        return python_obj
