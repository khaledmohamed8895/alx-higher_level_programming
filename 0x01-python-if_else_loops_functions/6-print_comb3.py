#!/usr/bin/python3
for count in range(0, 10):
    for a in range(1, 10):
        if count >= a:
            continue
        if count == 8 and a == 9:
            print("{}{}".format(count, a))
        else:
            print("{}{}".format(count, a), end=", ")
