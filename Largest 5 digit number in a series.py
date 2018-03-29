# --------------------------------------------------
# Programm by Yoatn
#
# Start date   04.01.2018   19:47
# End date     04.01.2017   20:07
#  
# Description:
#In the following 6 digit number:

# 283910
# 91 is the greatest sequence of 2 digits.
#
# In the following 10 digit number:
#
# 1234567890
# 67890 is the greatest sequence of 5 digits.
#
# Complete the solution so that it returns
# the largest five digit number found within
# the number given. The number will be passed
# in as a string of only digits. It should
# return a five digit integer. The number
# passed may be as large as 1000 digits.
#
# Adapted from ProjectEuler.net
# --------------------------------------------------

def solution(digits):
     return max(int(digits[i:i + 5]) for i in range(len(digits)))


# StrIn = '1234567898765'
# BufferList = [0]
# for i in range(len(StrIn)):
#     number = int(StrIn[0 + i:5 + i])
#     if number > BufferList[0]:
#         BufferList[0] = number
print(solution('1234567898765'))