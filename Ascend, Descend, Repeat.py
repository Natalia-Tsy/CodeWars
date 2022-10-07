def ascend_descend(length, minimum, maximum):
    list1 = list(range(minimum, maximum +1))
    list2 = list(range(maximum -1, minimum -1, -1))
    list3 = (list1 + list2[:-1])

    return ''.join(map(str,list3 * length)) [:length]