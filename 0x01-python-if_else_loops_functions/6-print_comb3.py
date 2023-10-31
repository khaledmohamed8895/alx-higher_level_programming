#!/usr/bin/python3
def islower(x):
    z = ord(x)
    if z >= 65 and z < 90:
        return False
    elif z >= 97 and z <= 122:
        return True
