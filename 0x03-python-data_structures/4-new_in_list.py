#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)

    if idx < 0 or idx > (length - 1):
        return (my_list)

    else:
        new_list = my_list[:]
        new_list[idx] = element
    return (new_list)


    # length = len(my_list)

    # new_list = my_list[:]

    # if 0 <= idx < length:
    #     new_list[idx] = element

    # return (new_list)
