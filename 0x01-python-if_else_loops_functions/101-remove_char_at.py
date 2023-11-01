#!/usr/bin/python3
def remove_char_at(str, n):
    s = ""
    for count in range(len(str)):
        if count != n:
            s = s + str[count]
    return (s)
