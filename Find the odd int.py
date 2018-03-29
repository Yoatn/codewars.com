# --------------------------------------------------
# Programm by Yoatn
#
# Start date   30.12.2017   09:52
# End date     00.00.2017   00:00
#  
# Description:
# Given an array, find the int that
# appears an odd number of times.
#
# There will always be only one integer
# that appears an odd number of times.
# test.assert_equals(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)
# --------------------------------------------------


def find_it(seq):
    ListOut = []
    for i in StrIn:
        if StrIn.count(i) % 3 == 0:
            if i not in ListOut:
                ListOut.append(i)
    for i in ListOut:
        return i



StrIn = [20,1,-1,2,-1,3,3,5,1,2,4,20,4,-1,-2,5]
ListOut = []
for i in StrIn:
    if StrIn.count(i) % 3 == 0:
        if i not in ListOut:
            ListOut.append(i)
for i in ListOut:
    print(i, end=' ')

print(find_it(StrIn))

# print(lambda i, StrIn: )