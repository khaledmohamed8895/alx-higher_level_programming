def uniq_add(my_list=[]):
    result = set(my_list)
    result = list(result)
    sum = 0
    for x in result:
        sum = sum + x
    return sum
