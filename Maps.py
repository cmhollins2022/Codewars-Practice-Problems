def maps(a):
    new_list = []  # make a new list to store the values to be added
    for x in a:  # iterate
        doubled_x = x * 2  # double x
        new_list.append(doubled_x)  # add doubled x to new list
    return print(new_list)

maps([1, 2, 3])  # should be [2, 4, 6]
