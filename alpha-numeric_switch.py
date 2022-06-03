def correct(word: str): # Verify the function input type.
    word = word.replace("0", "O") # Set our data of word equal to the revision.
    word = word.replace("1", "I")
    word = word.replace("5", "S")# Verify our data type.
    return word # Return our revised word.

# Another way...?

def correct(string):
    return string.translate(str.maketrans("501", "SOI"))
