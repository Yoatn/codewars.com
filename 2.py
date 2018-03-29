# --------------------------------------------------
# Programm by Yoatn
#
# Start date   00.00.2017   00:00
# End date     00.00.2017   00:00
#  
# Description:
#Your task is to sort a given string. Each word in
# the String will contain a single number. This
# number is the position the word should have in the result.
#
# Note: Numbers can be from 1 to 9. So 1 will be
# the first word (not 0).
#
# If the input String is empty, return an empty
# String. The words in the input String will only
# contain valid consecutive numbers.
#
# For an input: "is2 Thi1s T4est 3a" the function
# should return "Thi1s is2 3a T4est"
# --------------------------------------------------
# import re
#
# def order(StrIn):
#     DictIn = {}
#     StrOut = ''
#     for i in StrIn.split():
#         f = re.findall(r'[1-9]', i)
#         DictIn.setdefault(f[0], i)
#     for i in sorted(DictIn):
#         StrOut += ' ' + DictIn[i]
#     return StrOut.strip()
#
# # print(order('is2 Thi1s T4est 3a'))
#
# print(order(input()))

def order(sentence):
    return " ".join(sorted(sentence.split()))


print(order('1 4 5 6 1 1 7 4 5 2 8'))