# --------------------------------------------------
# Programm by Yoatn
#
# Start date   27.03.2018    18:34
# End date     
#  
# Description:
#
# --------------------------------------------------
#
# import datetime
# print(datetime.datetime.now().strftime('%d.%m.%Y    %H:%M'))

def averages(ArrIn):
    ArrOut = []
    for i in range(len(ArrIn) - 1):
        a = (ArrIn[i] + ArrIn[i + 1]) / 2
        if int(a) == float(a):
            ArrOut.append(int(a))
        else:
            ArrOut.append(a)
    return(ArrOut)

print(averages([]))