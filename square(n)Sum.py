def square_sum(numbers):
    new_list = []  # New list for numbers to be added into
    for item in numbers:  # iterate through each item in the list
        item_squared = item ** 2  # square the item
        new_list.append(item_squared)  # add the newly squared item into the new list

    return print(sum(new_list))  # return the sum of the new list


square_sum([1, 2, 3])
square_sum([5, 5, 5])
