# Write a function that takes an array of numbers and returns the sum of the numbers.
# The numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0.

def sum_array(a: list):
    return print(sum(a))

# # Alternatively... (Still in progress)
# def sum_array_2(a: list):
#     for number in a:
#         while number is True:
#             a[0] = number + a
#     return a[0]

sum_array([])
sum_array([1, 2, 3])
