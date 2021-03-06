def switch_it_up(number: int): # Specify our type.
    numbers_dict = { # Create a dictionary for all of the key-value pairs.
        0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four",
        5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"
    }
    return numbers_dict.get(number) # Index our function input from the dictionary.
  
  # Another way...
def switch_it_up(n):
    return ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine'][n]
