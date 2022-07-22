def lovefunc( flower1: int, flower2: int ): # Type our function inputs
    if (flower1 + flower2) % 2 == 0: # If they can be added together and equally divided...
        return False # ...we know the answer is false.
    else: return True # Any other case is True
