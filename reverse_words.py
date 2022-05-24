def reverse_words(text: str):
    for character in text:
        if character == " ":
            continue
        else:
            text = character[::-1]
    return text
