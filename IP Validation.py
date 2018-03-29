# --------------------------------------------------
# Programm by Yoatn
#
# Start date   13.01.2018   23:21
# End date     14.01.2018   01:55
#  
# Description:
#Write an algorithm that will identify valid
# IPv4 addresses in dot-decimal format. IPs
# should be considered valid if they consist
# of four octets, with values between 0..255
# (included).

# Input to the function is guaranteed to be
# a single string.
#
# Examples
#
# // valid inputs:
# 1.2.3.4
# 123.45.67.89
#
# // invalid inputs:
# 1.2.3
# 1.2.3.4.5
# 123.456.78.90
# 123.045.067.089
# --------------------------------------------------
#
import datetime
print(datetime.datetime.now().strftime("%d.%m.%Y   %H:%M"))


def is_valid_IP(strng):
    x = strng.split('.')
    try:
        if False in map(lambda i: 0 <= int(i) < 256, x):
            return False
        elif len(x) != 4 or ' ' in strng:
            return False
        for i in x:
            if (i >1 and i[0] == '0' and len(i) > 1):
                return False
        else:
            return True
    except ValueError:
        return False

a = '12.34.56.01'


# print(is_valid_IP('12.255.56.1'))
# print(is_valid_IP('abc.def.ghi.jkl'))
# print(is_valid_IP(''))
# print(is_valid_IP('0.0.0'))
# print(is_valid_IP('0.0.0.0'))
# print(is_valid_IP('0.01.0.0'))
#



