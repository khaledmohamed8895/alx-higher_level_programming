#!/usr/bin/python3
for count in range(0, 100):
    if count == 99:
        print("{}".format(count).zfill(2))
    else:
        print("{}".format(count).zfill(2), end=", ")
