def make_negative(number: int):
    if number > 0:
        return print(number.__neg__())
    elif number <= 0:
        return print(number)


make_negative(4)
make_negative(-5)
make_negative(3)
