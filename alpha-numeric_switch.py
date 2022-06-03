def correct(word: str):
    word = word.replace("0", "O") # Set our data of word equal to the revision.
    word = word.replace("1", "I")
    
    return word # Return our revised word.
