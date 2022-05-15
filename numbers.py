def sum_mix(arr):
    # make a new list to store the values to be added.
    new_list = []
    # iterate
    for x in arr:
        if type(x) == str:  # if x is a string
            converted_x = int(x)  # change  x into a type "int"
            new_list.append(converted_x)  # add x to the new list
        elif type(x) == int:  # if it's already an int
            new_list.append(x)  # add x to the new list
            continue

    return print(sum(new_list))  # add the items in the list


