# Your code will determine if the number passed is even (or not).
# The function needs to return either a true or false.
# Numbers may be positive or negative, integers or floats.

def is_even(n: int): 
    if n % 2 == 0: # Use Modulo in order to determine if the number is divisible by 2
        return True
    else: # Anything else would be false
        return False
