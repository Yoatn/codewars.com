# --------------------------------------------------
# Programm by Yoatn
#
# Start date   30.12.2017   00:57
# End date     00.00.2017   00:00
#  
# Description:
#The goal of this exercise is to convert
# a wordg to a new wordg where each
# character in the new wordg is '(' if
# that character appears only once in the
# original wordg, or ')' if that character
# appears more than once in the original
# wordg. Ignore capitalization when
# determining if a character is a duplicate.
#
# Examples:
#
# "din" => "((("
#
# "recede" => "()()()"
#
# "Success" => ")())())"
#
# "(( @" => "))(("
# --------------------------------------------------

def duplicate_encode(word):
    word = word.lower()
    StrOut = ''
    for i in word:
        if word.count(i) > 1:
            StrOut += ')'
        else:
            StrOut += '('
    return StrOut


# #     Why is this code wrong?

#     def duplicate_encode(word):
#     StrOut = ''
#     for i in word.lower(): # <- In this place
#         if word.count(i) > 1:
#             StrOut += ')'
#         else:
#             StrOut += '('
#     return StrOut

print(duplicate_encode('(( @'))