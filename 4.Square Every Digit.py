# --------------------------------------------------
# Programm by Yoatn
#
# Start date   29.12.2017   11:20
# End date     00.00.2017   00:00
#  
# Description:
#Welcome. In this kata, you are asked to square every digit of a number.
#
# For example, if we run 9119 through the function, 811181 will come out.
#
# Note: The function accepts an integer and returns an integer
# --------------------------------------------------


# def square_digits(num): # solution 1
#     StrOut = []
#     for i in str(num):
#         StrOut.append(str(int(i) ** 2))
#     return int(''.join(StrOut))


# def square_digits(num): # solution 2
#     return int(''.join(str(int(i) ** 2) for i in str(num)))

def square_digits(num): # solution 3
    return int(''.join([str(i ** 2) for i in map(int, str(num))]))



print(square_digits('123456111235'))