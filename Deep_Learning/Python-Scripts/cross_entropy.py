# PROJECT: Cross-Entropy Script
# PROGRAMMER: Carlos Mertens - Udacity Student
#				Udacity Instructors (Machine Learning Engineer Nanodegree)
# DATE CREATED: (DD/MM/YY) 10/01/2019
# REVISED DATE: (DD/MM/YY)
# PURPOSE: To show the algorithm to implement Cross-Entropy from the scratch.
# USAGE: ...

import numpy as np


# Write a function that takes as input two lists Y, P,
# and returns the float corresponding to their cross-entropy.
def cross_entropy(y, p):
    y = np.float_(y)
    p = np.float_(p)
    result = -np.sum(y * np.log(p) + (1 - y) * np.log(1 - p))
    return result


y = [1,0,1,1]
p = [0.4,0.6,0.1,0.5]

# Call function to calculate the cross-entropy
my_cross_entropy = cross_entropy(y, p)

print(my_cross_entropy)
