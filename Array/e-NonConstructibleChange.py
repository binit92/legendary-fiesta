# Given an array of positive integers represeting the values of coins in your possession, 
# Write a function that return the minimum amount of change( the minimum sum of money)
# that you cannot create. The given coins can have any positive integer value 
# and aren't necessarily unique

coins  = [5, 7, 1, 1, 2, 3 ,22]
# output = 20

# Approach is : 
# 1 - 1 = 2
# [1, 2]  [1, 2, 1+2]  = 4
# [1, 1, 2] [1, 2, 3, 4] = 5
# [7] = 1 

# Bruteforce approach is to 
# check all the change from 1 that cannot be created 

# Another approach is to 
# sort the array 
# then 