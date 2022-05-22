def index(numbers_list: list, n: int):
    try: # Check to see if "n" is an index within the list
        i = numbers_list[n]**n # if so, ** to the power of n
        return i # return the exponential value
    


# def index(numbers_list: list, n: int):
#     for i in numbers_list: # iterate through the list
#         try:
#             i = numbers_list[n] # select the n'th index from the list
#             squared_n = i**n # square the index value by n
#             return squared_n # return the squared value
#         except:
#             return -1

# def index(numbers_list: list, n: int):
#     if numbers_list[n]:
#         i = numbers_list[n]
#         squared_n = i**n # square the index value by n
#         return squared_n # return the squared value
#     elif not numbers_list[n]:
#         return -1
