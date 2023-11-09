#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    _items = a_dictionary.items()
    x = [(key, val * 2) for key, val in _items]
    new_dict = dict(x)
    return new_dict
