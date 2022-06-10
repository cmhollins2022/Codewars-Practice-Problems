def min_max(prices: list): # Accepts a list
    new_list = [] # Make a new list for our returning value
    prices.sort() # Sort our list
    new_list.append(prices[0]) # Access the first(lowest) value of the list
    new_list.append(prices[-1]) # Access the last(greatest) value of the list
    return new_list
