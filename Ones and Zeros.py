# --------------------------------------------------
# Programm by Yoatn
#
# Start date   29.12.2017   22:55
# End date     00.00.2017   00:00
#  
# Description:
#Given an array of one's and zero's convert the equivalent binary value to an integer.
#
# Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1
#
# Examples:
#
# Testing: [0, 0, 0, 1] ==> 1
# Testing: [0, 0, 1, 0] ==> 2
# Testing: [0, 1, 0, 1] ==> 5
# Testing: [1, 0, 0, 1] ==> 9
# Testing: [0, 0, 1, 0] ==> 2
# Testing: [0, 1, 1, 0] ==> 6
# Testing: [1, 1, 1, 1] ==> 15
# Testing: [1, 0, 1, 1] ==> 11
# --------------------------------------------------

def binary_array_to_number(arr):
    return sum([i[1] * (2 ** i[0]) for i in enumerate(arr[::-1])])

print(binary_array_to_number([0, 1, 1, 0]))

# print(sum([i[1] * (2 ** i[0]) for i in enumerate(In[::-1])]))
