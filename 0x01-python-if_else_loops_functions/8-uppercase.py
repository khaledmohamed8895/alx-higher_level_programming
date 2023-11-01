#!/usr/bin/python3
def uppercase(str):
    new_String = ""
    for x in str:
        i = ord(x)
        if i >= 97 and i <= 122:
            new_String += chr(i-32)
        else:
            new_String += chr(i)
    print("{}".format(new_String)
