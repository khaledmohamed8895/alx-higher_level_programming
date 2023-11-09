#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a = sorted(a_dictionary.items())
    for k, v in a:
        print(f"{k}: {v}")
