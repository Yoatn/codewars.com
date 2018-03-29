# --------------------------------------------------
# Programm by Yoatn
#
# Start date   04.01.2018   16:41
# End date     00.00.2018   00:00
#  
# Description:
#Snail Sort

# Given an n x n array, return the array
# elements arranged from outermost elements
# to the middle element, traveling clockwise.
#
# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
# For better understanding, please follow
# the numbers of the next array consecutively:
#
# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]
# --------------------------------------------------

# ArIn = [[1,2],
#          [4,3]]



array = [[1,2,3],
         [8,9,4],
         [7,6,5]]



# print([i for i in range(1, 17)])

# [1, 2, 3, 4]
# [1, 2, 4, 3]

# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [1, 2, 3, 8, 9, 4, 7, 6, 5]

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# [1, 2, 3, 4, 12, 13, 14, 5, 11, 16, 15, 6, 10, 9, 8, 7]

# ArOut = [1, 2, 3, 4, 12, 13, 14, 5, 11, 16, 15, 6, 10, 9, 8, 7]



