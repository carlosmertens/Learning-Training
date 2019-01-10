# PROJECT: Softmax Function
# PROGRAMMER: Carlos Mertens - Udacity Student
#				Udacity Instructors (Machine Learning Engineer Nanodegree)
# DATE CREATED: (DD/MM/YY) 10/01/2019
# REVISED DATE: (DD/MM/YY)
# PURPOSE: Udacity instructors show the algorithm to implement Softmax Function
#			From the scratch.
# USAGE: ...

import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def my_softmax(L):
    exp_list = np.exp(L)
    sum_exp_list = sum(exp_list)
    result = []
    for i in exp_list:
        result.append(i * 1.0 / sum_exp_list)
    return result


my_list = [5,6,7]

# Call function to get the softmax from my_list
my_list_softmax = my_softmax(my_list)

print(my_list_softmax)