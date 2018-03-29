# --------------------------------------------------
# Programm by Yoatn
#
# Start date   15.01.2018   21:00
# End date     
#  
# Description:
#You need to write regex that will validate a password
# to make sure it meets the following criteria:
#
# At least six characters long
# contains a lowercase letter
# contains an uppercase letter
# contains a number
# Valid passwords will only be alphanumeric characters.

# --------------------------------------------------
#
# import datetime
# print(datetime.datetime.now().strftime("%d.%m.%Y   %H:%M"))

import re

Str = 'fjd3I.'

regex = re.findall(r'(?=.*[^\W])((?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,})', Str)
print(regex)

# don't mine
# ^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[^\W_]{6,}$
