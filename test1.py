#Let's say we have an array of the ages of all the people that live in a street.

#What is the 75. percentile?


import numpy

ages=[5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

percentile_test=numpy.percentile(ages, 75)

print(percentile_test)


#The answer is 43, meaning that 75% of the people are 43 or younger.

#The NumPy module has a method for finding the specified percentile:
