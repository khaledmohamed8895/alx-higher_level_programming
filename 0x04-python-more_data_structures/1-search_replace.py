#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    i = new_list.count(search)
    if i == 1:
        new_list[new_list.index(search)] = replace
        return new_list
    else:
        x = 0
        while x != i:
            new_list[new_list.index(search)] = replace
            x += 1
        return new_list
