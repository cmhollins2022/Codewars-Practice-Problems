def make_negative(number: int):
    if number > 0: # Check to see if the number is greater than 0
        return print(number.__neg__())
    elif number <= 0: # Check to see if the number is less than or equal to 0
        return print(number)


make_negative(4)
make_negative(-5)
make_negative(3)
