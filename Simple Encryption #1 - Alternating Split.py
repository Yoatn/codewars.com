# --------------------------------------------------
# Programm by Yoatn
#
# Start date   13.01.2018   22:08
# End date     
#  
# Description:
#For building the encrypted string:
# Take every 2nd char from the string, then the other chars, that are not every 2nd char, and concat them as new String.
# Do this n times!
#
# Examples:
#
# "This is a test!", 1 -> "hsi  etTi sats!"
# "This is a test!", 2 -> "hsi  etTi sats!" -> "s eT ashi tist!"
# Write two methods:
#
# def encrypt(text, n)
# def decrypt(encrypted_text, n)
# For both methods:
# If the input-string is null or empty return exactly this value!
# If n is <= 0 then return the input text.
#
# This kata is part of the Simple Encryption Series:
# Simple Encryption #1 - Alternating Split
# Simple Encryption #2 - Index-Difference
# Simple Encryption #3 - Turn The Bits Around
# Simple Encryption #4 - Qwerty
#
# Have fun coding it and please don't forget to vote and rank this kata! :-)

# --------------------------------------------------
#
# import datetime
# print(datetime.datetime.now().strftime("%d.%m.%Y   %H:%M"))


# def dec


SrtIn = 'This is a test!'
# print(len(SrtIn))
n = 1


# for i in range(len(SrtIn) :

print(SrtIn[1::2] + SrtIn[0::2])
print(SrtIn[3::2])