#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        add = 0
        num = 0
        for i, j in my_list:
            add = add + (i * j)
            num = num + j
        result = add / num
        return result
    else:
        return 0
