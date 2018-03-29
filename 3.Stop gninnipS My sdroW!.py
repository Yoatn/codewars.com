# --------------------------------------------------
# Programm by Yoatn
#
# Start date   22.14.2017   22:14
# End date     00.00.2017   00:00
#  
# Description:
#
# --------------------------------------------------


# StrIn = 'Hey fellow warriors'
def spin_words(sentence):
#     StrOut = []
    l = ''
    for i in sentence.split():
        #     if len(i) > 4:
        #         StrOut.append(i[::-1])
        #     else:
        #         StrOut.append(i)
        # for i in StrOut:
        l += ((i[::-1] + ' ') *(len(i) > 4) or (i + ' ') *(len(i) <= 4))
    return l.strip()

print(spin_words('Hey fellow warriors'))