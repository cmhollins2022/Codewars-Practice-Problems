def solution(text: str, text_ending: str):  # Type the data types
    if text.endswith(text_ending):  # Use the ".endswith()" method
        return True
    else:
        return False
    pass

# Another possible way:
def solution(string, ending):
    return string.endswith(ending)
