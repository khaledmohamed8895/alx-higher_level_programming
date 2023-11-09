#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    _keys_to_delete = []
    for k, v in a_dictionary.items():
        if v == value:
            _keys_to_delete.append(k)

    for k in _keys_to_delete:
        del a_dictionary[k]

    return a_dictionary
