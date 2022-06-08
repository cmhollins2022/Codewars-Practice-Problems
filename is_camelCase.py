def solution(word: str):  # Type our input
    empty_list = []  # Let's make an empty list
    for letter in word:  # Iterate through our string
        if letter.islower():  # If the letter is lowercase...
            empty_list.append(letter)  # Add the letter to our list, which we will ultimately "join"
        elif letter.isupper():  # If the letter is uppercase...
            empty_list.append(" ")  # Add a space to our list, which we will ultimately "join"
            empty_list.append(letter)  # Add the letter
        else:  # If it's anything else...
            continue
    return ''.join(empty_list)  # Join our list together by "", or nothing
