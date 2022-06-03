# Return the number (count) of vowels in the given string.
def get_count(sentence: str): # Type our inputing method
    vowels_list = ["a","e","i","o","u"] # Make a vowel list
    count = 0 # Be prepared to count the vowels
    for letter in sentence: # Iterate through our string
        if letter in vowels_list: # If the letter is a vowel...
            count = count + 1 # Increase our count by +1
    return count
